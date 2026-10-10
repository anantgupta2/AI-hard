"""Extract declarations, imports and an approximate dependency DAG for one family's Lean code.

Text-level parse (no Lean build): tracks namespaces / sections / `open`s, splits files into
declarations, and links declarations by Lean-style name resolution. Good enough to rank
items by how load-bearing they are; an exact DAG would need the compiled environment.

v2 changes (family 287 analysis, 2026-10-09):
  * follows `import OAI.*` transitively, so families whose code imports another OAI dir
    (e.g. 287: InterpolatedFactors -> FreeGroupFactor) are analysed as one unit;
  * declarations indented by one space (common in some OAI files) are recognised;
    `local instance`, multiple attributes and `@[...]` before modifiers are handled;
  * the signature is cut at the first `:=` / `where` / `|` at bracket depth 0, so named
    arguments such as `(G := G)` no longer truncate signatures;
  * name resolution follows Lean: enclosing namespaces of the declaration's full name,
    then every `open`ed namespace (resolved relative to the current namespace), then root;
    structure fields and inductive constructors resolve to their parent type;
    generalized field notation `x.foo` falls back to a unique, non-generic short name;
  * the proof DAG is computed from the comparator target(s) only (`target_*` fields) and
    separately with the sibling theorems of the target file (`*_with_siblings`);
  * new fields: `in_target_signature_closure` (definitions reached by unfolding the target
    statement = analytic by test 2), `dominated_share` (fraction of the target DAG that is
    reachable only through the item), `n_tokens`, `occurrences_in_dag`, `plumbing` +
    `plumbing_reason`;
  * the candidate filter excludes plumbing and items inside the target-statement closure,
    ranks definitions by dominated share / statement use rather than raw closure share, and
    also emits lemma candidates (`candidate_lemmas`).

Usage: python scripts/extract_lean.py 173 [179 132 ...] [--repo ...] [--out data/items]
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

DECL_KINDS = ("theorem", "lemma", "def", "abbrev", "structure", "inductive", "class", "instance", "opaque", "axiom")
DEF_KINDS = {"def", "abbrev", "structure", "inductive", "class", "opaque"}
THM_KINDS = {"theorem", "lemma"}
MODIFIERS = ("private", "protected", "noncomputable", "partial", "unsafe", "nonrec", "local", "scoped")
DECL_RE = re.compile(
    r"^ ?(?:@\[[^\]]*\]\s*)*(?:(?:%s)\s+)*(%s)\b\s*([^\s:(\[{]*)" % ("|".join(MODIFIERS), "|".join(DECL_KINDS))
)
# Lean identifiers: unicode letters, digits, subscripts, _ ' ! ?, dotted components.
IDENT_RE = re.compile(r"@?[^\W\d][\w'!?₀-₉ₐ-ₜ]*(?:\.[^\W\d][\w'!?₀-₉ₐ-ₜ]*)*")
TOKEN_RE = re.compile(r"[\w'!?₀-₉ₐ-ₜ.]+|[^\s\w]")
COMMAND_STARTS = ("namespace ", "section", "noncomputable section", "end", "open ", "variable", "set_option",
                  "attribute", "universe", "include ", "omit ", "local notation", "notation", "#")
# Generic field names that also exist all over Mathlib: never resolve `x.foo` to a family decl by these.
GENERIC_FIELDS = {
    "symm", "trans", "refl", "mp", "mpr", "le", "lt", "ne", "comp", "toFun", "invFun", "map", "apply", "injective",
    "surjective", "continuous", "ext", "mono", "val", "property", "coe", "one", "zero", "mul", "add", "sub", "inv",
    "neg", "eq", "elim", "choose", "choose_spec", "some", "none", "inl", "inr", "fst", "snd", "out", "1", "2",
    "left", "right", "trans_le", "trans_lt", "le_trans", "lt_of_le", "norm", "inner", "star", "smul", "pos",
    "nonneg", "ne'", "bot", "top", "of", "single", "sum", "prod", "support", "mem", "subset", "isClosed", "isOpen",
    "map_mul", "map_one", "map_add", "map_zero", "isSelfAdjoint", "isIdempotentElem", "toStarAlgHom", "bijective",
}


def strip_comments(src):
    src = re.sub(r"/-.*?-/", lambda m: "\n" * m.group(0).count("\n"), src, flags=re.S)
    return re.sub(r"--[^\n]*", "", src)


def split_signature(text):
    """Return index where the signature ends: first `:=`, ` where`, or `\\n|` at bracket depth 0."""
    depth, i, n = 0, 0, len(text)
    while i < n:
        c = text[i]
        if c in "([{⟨⦃":
            depth += 1
        elif c in ")]}⟩⦄":
            depth = max(0, depth - 1)
        elif depth == 0:
            if text.startswith(":=", i):
                return i
            if text.startswith(" where", i) and (i + 6 == n or not (text[i + 6].isalnum() or text[i + 6] == "_")):
                return i
            if text.startswith("\n", i) and text[i + 1 :].lstrip(" ").startswith("|"):
                return i
        i += 1
    return n


def parse_file(path, rel):
    raw = path.read_text(encoding="utf-8", errors="replace")
    docs = {}  # line index -> preceding docstring
    for m in re.finditer(r"/--(.*?)-/", raw, flags=re.S):
        end_line = raw[: m.end()].count("\n")
        docs[end_line + 1] = " ".join(m.group(1).split())
    lines = strip_comments(raw).split("\n")
    imports = [l.split()[1] for l in lines if l.startswith("import ")]
    # scope stack: list of dicts {kind, parts, opens}
    stack, decls, cur = [], [], None

    def cur_ns():
        return [p for fr in stack if fr["kind"] == "namespace" for p in fr["parts"]]

    def cur_opens():
        out = []
        for fr in stack:
            out.extend(fr["opens"])
        return out

    file_opens = []  # opens at file top level
    for i, line in enumerate(lines):
        s = line.strip()
        top = not line.startswith(("  ", "\t"))
        if top and s.startswith("namespace "):
            stack.append({"kind": "namespace", "parts": s.split()[1].split("."), "opens": []})
            cur = None
            continue
        if top and (s.startswith("section") or s.startswith("noncomputable section")):
            stack.append({"kind": "section", "parts": [], "opens": []})
            cur = None
            continue
        if top and (s == "end" or s.startswith("end ")):
            if stack:
                name = s.split()[1] if len(s.split()) > 1 else None
                # pop the innermost frame matching the name (or the innermost frame)
                if name is None:
                    stack.pop()
                else:
                    for j in range(len(stack) - 1, -1, -1):
                        if ".".join(stack[j]["parts"]) == name or (stack[j]["parts"] and stack[j]["parts"][-1] == name):
                            del stack[j:]
                            break
                    else:
                        stack.pop()
            cur = None
            continue
        if top and s.startswith("open "):
            body = s[5:]
            body = re.split(r"\bin\b|\bhiding\b|\brenaming\b|\(", body)[0]
            names = [t for t in body.split() if t not in ("scoped",)]
            ns_here = cur_ns()
            target = stack[-1]["opens"] if stack else file_opens
            for t in names:
                target.append((tuple(ns_here), t))
            cur = None
            continue
        m = DECL_RE.match(line) if top else None
        if m:
            kind, name = m.group(1), m.group(2)
            if kind == "lemma":
                kind = "theorem"
            ns = cur_ns()
            if name.startswith("_root_."):
                full = name[len("_root_.") :]
            elif name:
                full = ".".join(ns + [name])
            else:
                full = ".".join(ns + [f"<anon:{kind}:{rel}:{i+1}>"])
            cur = {
                "name": full,
                "short": full.split(".")[-1],
                "kind": kind,
                "file": rel,
                "line": i + 1,
                "namespace": ".".join(ns),
                "opens": [list(o) for o in file_opens + cur_opens()],
                "doc": docs.get(i, docs.get(i - 1, "")),
                "text": [line],
                "local": "local " in line.split(kind)[0],
            }
            decls.append(cur)
        elif cur is not None:
            if top and s and s.startswith(COMMAND_STARTS):
                cur = None
            else:
                cur["text"].append(line)
    for d in decls:
        text = "\n".join(d.pop("text")).rstrip()
        sig_end = split_signature(text)
        d["signature"] = " ".join(text[:sig_end].split())
        d["body"] = text[sig_end:]
        d["n_lines"] = text.count("\n") + 1
        d["n_tokens"] = len(TOKEN_RE.findall(text))
        d["n_body_tokens"] = len(TOKEN_RE.findall(d["body"]))
        # structure fields / inductive constructors become aliases of the type
        aliases = []
        if d["kind"] == "inductive":
            aliases = re.findall(r"\|\s*([^\W\d][\w']*)", d["body"])
        elif d["kind"] in ("structure", "class"):
            aliases = re.findall(r"^\s{2,4}([^\W\d][\w']*)\s*:", d["body"], flags=re.M)
        d["aliases"] = [d["name"] + "." + a for a in aliases]
    return imports, decls


def lean_dirs_for(fid, catalog):
    row = catalog[catalog.family_id == fid]
    if row.empty or not isinstance(row.iloc[0].lean_dirs, str):
        return [], []
    r = row.iloc[0]
    return r.lean_dirs.split(";"), r.lean_declarations.split(";")


def module_to_path(mod, repo):
    return repo / "lean" / (mod.replace(".", "/") + ".lean")


def collect_files(dirs, repo, follow_imports=True):
    """Files of the family dirs, plus (transitively) every imported OAI module outside them."""
    paths = []
    for d in dirs:
        base = repo / "lean" / d
        paths += sorted(base.rglob("*.lean")) if base.is_dir() else []
        if base.with_suffix(".lean").exists():
            paths.append(base.with_suffix(".lean"))
    seen = {p.resolve() for p in paths}
    extra_dirs = set()
    if follow_imports:
        queue = list(paths)
        while queue:
            p = queue.pop()
            for l in p.read_text(encoding="utf-8", errors="replace").split("\n"):
                if l.startswith("import OAI."):
                    q = module_to_path(l.split()[1], repo)
                    if q.exists() and q.resolve() not in seen:
                        seen.add(q.resolve())
                        paths.append(q)
                        queue.append(q)
                        extra_dirs.add(q.parent.relative_to(repo / "lean").as_posix())
    own = {(repo / "lean" / d).resolve() for d in dirs}
    extra_dirs = sorted(d for d in extra_dirs if (repo / "lean" / d).resolve() not in own)
    return paths, extra_dirs


def build(fid, repo, catalog, follow_imports=True, keep_body=False):
    dirs, targets = lean_dirs_for(fid, catalog)
    if not dirs:
        return None
    paths, extra_dirs = collect_files(dirs, repo, follow_imports)
    files, imports, decls = [], {}, []
    for p in paths:
        rel = p.relative_to(repo / "lean").as_posix()
        imps, ds = parse_file(p, rel)
        files.append(rel)
        imports[rel] = imps
        decls.extend(ds)
    # declaration order: files in import-topological order, then line. Lean only resolves a
    # name to declarations that already exist, so later declarations must not shadow.
    mod_of = {f: f[:-5].replace("/", ".") for f in files}
    rank, temp = {}, set()

    def visit(f):
        if f in rank or f in temp:
            return
        temp.add(f)
        for imp in imports[f]:
            g = imp.replace(".", "/") + ".lean"
            if g in imports:
                visit(g)
        rank[f] = len(rank)

    for f in files:
        visit(f)
    for d in decls:
        d["_pos"] = (rank[d["file"]], d["line"])
    by_name = {}
    for d in decls:
        by_name.setdefault(d["name"], d)
    alias_of = {}
    for d in decls:
        for a in d["aliases"]:
            alias_of.setdefault(a, d["name"])
    names = set(by_name) | set(alias_of)
    short_index = defaultdict(set)
    for n in names:
        short_index[n.split(".")[-1]].add(alias_of.get(n, n))

    def lookup(full, d):
        r = full if full in by_name else alias_of.get(full)
        if r and (by_name[r]["_pos"] < d["_pos"]):
            return r
        return None

    def visible(cands, d):
        return {c for c in cands if by_name[c]["_pos"] < d["_pos"]}

    def resolve(tok, d):
        tok = tok.lstrip("@")
        if tok.startswith("_root_."):
            return lookup(tok[7:], d), "root"
        ns = d["name"].split(".")[:-1]  # namespaces of the decl's own full name
        for k in range(len(ns), -1, -1):
            r = lookup(".".join(ns[:k] + [tok]), d)
            if r:
                return r, "ns"
        for ctx, o in d["opens"]:
            ctx = list(ctx)
            for k in range(len(ctx), -1, -1):
                r = lookup(".".join(ctx[:k] + [o, tok]), d)
                if r:
                    return r, "open"
        parts = tok.split(".")
        # projection on a declared constant: `foo.exists`, `foo.le.trans` -> edge to `foo`
        # (the longest dotted prefix that resolves as a declaration in scope)
        for k in range(len(parts) - 1, 0, -1):
            head = ".".join(parts[:k])
            for j in range(len(ns), -1, -1):
                r = lookup(".".join(ns[:j] + [head]), d)
                if r:
                    return r, "proj"
            for ctx, o in d["opens"]:
                ctx = list(ctx)
                for j in range(len(ctx), -1, -1):
                    r = lookup(".".join(ctx[:j] + [o, head]), d)
                    if r:
                        return r, "proj"
        # generalized field notation: x.foo / x.foo.bar where x is a local
        for k in range(1, len(parts)):
            suffix = parts[k]
            if suffix in GENERIC_FIELDS:
                continue
            c = visible(short_index.get(suffix, set()), d)
            if len(c) == 1:
                return next(iter(c)), "field"
        return None, None

    mathlib_refs = Counter()
    n_field = 0
    pending = {}  # decl name -> unresolved field-notation tokens (suffix, count, in_sig)
    for d in decls:
        sig_toks = Counter(IDENT_RE.findall(d["signature"]))
        all_toks = Counter(IDENT_RE.findall(d["signature"] + "\n" + d["body"]))
        # `.foo` after `)`/space: anonymous constructor or field access on a parenthesised term
        for t in re.findall(r"(?<![\w.'])\.([^\W\d][\w']*)", d["signature"] + "\n" + d["body"]):
            all_toks["\u0000." + t] += 1
        uses_all, uses_sig, occ = set(), set(), Counter()
        unresolved = []
        for t, cnt in all_toks.items():
            if t.startswith("\u0000."):
                suffix = t[2:]
                c = visible(short_index.get(suffix, set()), d)
                tgt = next(iter(c)) if len(c) == 1 and suffix not in GENERIC_FIELDS else None
                how = "dot"
                if tgt is None and len(c) > 1 and suffix not in GENERIC_FIELDS:
                    unresolved.append((suffix, cnt, ("." + suffix) in d["signature"]))
            else:
                tgt, how = resolve(t, d)
                if tgt is None and "." in t:
                    suffix = t.split(".")[-1]
                    if suffix not in GENERIC_FIELDS and len(visible(short_index.get(suffix, ()), d)) > 1:
                        unresolved.append((suffix, cnt, t in sig_toks))
            if tgt and tgt != d["name"]:
                uses_all.add(tgt)
                occ[tgt] += cnt
                if t in sig_toks or (t.startswith("\u0000.") and ("." + t[2:]) in d["signature"]):
                    uses_sig.add(tgt)
                n_field += how in ("field", "dot")
            elif not tgt and not t.startswith("\u0000") and "." in t:
                head = t.lstrip("@").split(".")[0]
                if len(head) >= 3 and head[0].isascii() and head[0].isupper():
                    mathlib_refs[head] += cnt
        d["uses"] = uses_all
        d["uses_in_signature"] = uses_sig
        d["occ"] = occ
        pending[d["name"]] = unresolved
    # second pass: disambiguate field notation by the types mentioned in this decl and in the
    # signatures of the decls it uses (e.g. `(parameterModel r).trace` -> `Model.trace`).
    n_ctx = 0
    for d in decls:
        if not pending[d["name"]]:
            continue
        ctx = set(d["uses"])
        for u in list(d["uses"]):
            ctx |= by_name[u]["uses_in_signature"]
        for suffix, cnt, in_sig in pending[d["name"]]:
            c = [x for x in visible(short_index[suffix], d) if x.rsplit(".", 1)[0] in ctx and x != d["name"]]
            if len(c) == 1:
                d["uses"].add(c[0])
                d["occ"][c[0]] += cnt
                if in_sig:
                    d["uses_in_signature"].add(c[0])
                n_ctx += 1
    for d in decls:
        d["uses"] = sorted(d["uses"])
        d["uses_in_signature"] = sorted(d["uses_in_signature"])
        d["occ"] = dict(d["occ"])

    # ---- reachability ---------------------------------------------------------------
    target_names = [t for t in targets if t in by_name]
    target_files = {by_name[t]["file"] for t in target_names}
    sibling_roots = {d["name"] for d in decls if d["file"] in target_files and d["kind"] == "theorem"}

    def reach_from(roots):
        seen, st = set(), list(roots)
        while st:
            n = st.pop()
            if n in seen:
                continue
            seen.add(n)
            st.extend(by_name[n]["uses"])
        return seen

    reach = reach_from(target_names)
    reach_sib = reach_from(set(target_names) | sibling_roots)

    # forward closures as bitsets over all decls (cycles handled by fixpoint iteration)
    idx = {n: i for i, n in enumerate(by_name)}
    names_list = list(by_name)
    clo = {n: 0 for n in by_name}
    order = []
    state = {}
    for root in by_name:  # iterative post-order DFS
        if root in state:
            continue
        st = [(root, iter(by_name[root]["uses"]))]
        state[root] = 1
        while st:
            n, it = st[-1]
            nxt = next(it, None)
            if nxt is None:
                st.pop()
                state[n] = 2
                order.append(n)
            elif nxt not in state:
                state[nxt] = 1
                st.append((nxt, iter(by_name[nxt]["uses"])))
    for _ in range(3):  # post-order handles DAGs in one pass; extra passes settle cycles
        changed = False
        for n in order:
            b = 0
            for u in by_name[n]["uses"]:
                b |= clo[u] | (1 << idx[u])
            if b != clo[n]:
                clo[n], changed = b, True
        if not changed:
            break

    reach_thms = {n for n in reach if by_name[n]["kind"] == "theorem"}
    reach_sib_thms = {n for n in reach_sib if by_name[n]["kind"] == "theorem"}
    # dependents (reverse closure) restricted to the reachable theorems: sum the closure
    # bit-vectors of those theorems (numpy, so this stays fast on large families)
    nbytes = (len(by_name) + 7) // 8

    def count_vec(thms):
        acc = np.zeros(nbytes * 8, dtype=np.int32)
        for t in thms:
            acc += np.unpackbits(np.frombuffer(clo[t].to_bytes(nbytes, "little"), dtype=np.uint8), bitorder="little")
        return acc

    cv, cv_sib = count_vec(reach_thms), count_vec(reach_sib_thms)
    dep_count = {n: int(cv[idx[n]]) for n in by_name}
    dep_count_sib = {n: int(cv_sib[idx[n]]) for n in by_name}

    # target-statement closure: unfold the target signature through definitions only
    sig_closure = set()
    st = [u for t in target_names for u in by_name[t]["uses_in_signature"]]
    while st:
        n = st.pop()
        if n in sig_closure:
            continue
        sig_closure.add(n)
        if by_name[n]["kind"] in DEF_KINDS | {"instance"}:
            st.extend(by_name[n]["uses"])

    # dominated share: fraction of the target DAG lost when the item is deleted, i.e. the size
    # of the item's subtree in the dominator tree rooted at the target(s) (Cooper-Harvey-Kennedy).
    dom = dominated_shares(target_names, reach, by_name)

    files_using = defaultdict(set)
    occ_in_dag = Counter()
    for d in decls:
        for u in d["uses"]:
            files_using[u].add(d["file"])
        if d["name"] in reach:
            for u, c in d["occ"].items():
                occ_in_dag[u] += c
    used_in_sig_of = defaultdict(set)
    for d in decls:
        if d["name"] in reach_thms:
            for u in d["uses_in_signature"]:
                used_in_sig_of[u].add(d["name"])

    for d in decls:
        n = d["name"]
        d["in_proof_dag"] = n in reach
        d["in_proof_dag_with_siblings"] = n in reach_sib
        d["n_dependents"] = dep_count[n]
        d["frac_dag_dependents"] = round(dep_count[n] / max(1, len(reach_thms) - (n in reach_thms)), 4)
        d["frac_dag_dependents_with_siblings"] = round(dep_count_sib[n] / max(1, len(reach_sib_thms)), 4)
        d["dominated_share"] = dom.get(n, 0.0)
        d["n_files_using"] = len(files_using[n] - {d["file"]})
        d["n_thm_signatures_using"] = len(used_in_sig_of[n])
        d["occurrences_in_dag"] = occ_in_dag[n]
        d["in_target_signature_closure"] = n in sig_closure
        d["is_target"] = n in target_names
        d["plumbing"], d["plumbing_reason"] = classify_plumbing(d)
        if not keep_body:
            d.pop("body")
            d.pop("occ")
        d.pop("opens")
        d.pop("_pos")

    # ---- imports ----------------------------------------------------------------------
    ext = defaultdict(set)
    own_prefixes = [dd for dd in dirs]
    for f, imps in imports.items():
        for imp in imps:
            if imp.startswith("Mathlib."):
                key = ".".join(imp.split(".")[:2])
            elif imp.startswith("OAI."):
                own = any(imp.replace(".", "/").startswith(dd) for dd in own_prefixes)
                key = "OAI(own)" if own else "OAI." + ".".join(imp.split(".")[1:3])
            elif imp == "Mathlib":
                key = "Mathlib(all)"
            else:
                key = imp.split(".")[0]
            ext[key].add(imp)

    defs = [d for d in decls if d["kind"] in DEF_KINDS]
    cand_defs = [
        d for d in defs
        if d["in_proof_dag"] and not d["plumbing"] and not d["in_target_signature_closure"]
        and d["n_files_using"] >= 1 and d["n_thm_signatures_using"] >= 1
    ]
    cand_defs.sort(key=lambda d: (-d["dominated_share"], -d["n_thm_signatures_using"]))
    thms = [d for d in decls if d["kind"] == "theorem" and d["in_proof_dag"] and not d["is_target"]]
    cand_lemmas = [d for d in thms if d["dominated_share"] >= 0.02 and d["n_files_using"] >= 1]
    cand_lemmas.sort(key=lambda d: -d["dominated_share"])
    summary = {
        "family_id": fid,
        "lean_dirs": dirs,
        "imported_oai_dirs": extra_dirs,
        "targets": targets,
        "targets_found": target_names,
        "n_files": len(files),
        "n_decls": len(decls),
        "kind_counts": pd.Series([d["kind"] for d in decls]).value_counts().to_dict(),
        "n_proof_dag": len(reach),
        "n_proof_dag_theorems": len(reach_thms),
        "n_proof_dag_with_siblings": len(reach_sib),
        "n_field_notation_links": n_field,
        "n_context_disambiguated_links": n_ctx,
        "target_signature_closure": sorted(sig_closure),
        "import_groups": {k: sorted(v) for k, v in sorted(ext.items())},
        "mathlib_namespace_refs": dict(mathlib_refs.most_common(80)),
        "candidate_defs": [d["name"] for d in cand_defs],
        "candidate_lemmas": [d["name"] for d in cand_lemmas],
    }
    return {"summary": summary, "declarations": decls}


def dominated_shares(targets, reach, by_name):
    ROOT = "\u0000root"
    succ = {ROOT: list(targets)}
    for n in reach:
        succ[n] = [u for u in by_name[n]["uses"] if u in reach]
    # iterative DFS postorder from the virtual root
    post, seen, st = [], {ROOT}, [(ROOT, iter(succ[ROOT]))]
    while st:
        n, it = st[-1]
        nxt = next(it, None)
        if nxt is None:
            st.pop()
            post.append(n)
        elif nxt not in seen:
            seen.add(nxt)
            st.append((nxt, iter(succ[nxt])))
    po = {n: i for i, n in enumerate(post)}
    rpo = post[::-1]
    preds = defaultdict(list)
    for n in rpo:
        for u in succ[n]:
            preds[u].append(n)
    idom = {ROOT: ROOT}

    def intersect(a, b):
        while a != b:
            while po[a] < po[b]:
                a = idom[a]
            while po[b] < po[a]:
                b = idom[b]
        return a

    changed = True
    while changed:
        changed = False
        for n in rpo[1:]:
            ps = [p for p in preds[n] if p in idom]
            if not ps:
                continue
            new = ps[0]
            for p in ps[1:]:
                new = intersect(p, new)
            if idom.get(n) != new:
                idom[n] = new
                changed = True
    children = defaultdict(list)
    for n, d in idom.items():
        if n != ROOT:
            children[d].append(n)
    sub = {}
    stack = [(ROOT, False)]
    while stack:
        n, done = stack.pop()
        if done:
            sub[n] = 1 + sum(sub[c] for c in children[n])
        else:
            stack.append((n, True))
            stack.extend((c, False) for c in children[n])
    total = max(1, len(reach))
    return {n: round(sub[n] / total, 4) for n in reach if n in sub and n not in targets}


def classify_plumbing(d):
    """Heuristic: (is_plumbing, reason). Plumbing = instances, type aliases, renamings,
    topology/coercion transport, and trivial structural maps."""
    k, sig, n = d["kind"], d["signature"], d["short"]
    body = d["body"]
    if k == "instance":
        return True, "instance (typeclass plumbing)"
    if k == "theorem":
        if d["n_body_tokens"] <= 12:
            return True, "one-line lemma (rfl/simp/term-mode wrapper)"
        return False, ""
    if k == "abbrev":
        return True, "abbrev (type alias / notation)"
    if "TopologicalSpace" in sig.split(":")[-1] or "TopologicalSpace.induced" in body[:200]:
        return True, "topology transport (induced/product topology)"
    if re.search(r"(Congr|congr|Flatten|flatten|Cast|cast|Equiv$|equiv$|^coe|Coe|symm$|trans$|refl$)", n):
        return True, "transport map / equivalence plumbing (by name)"
    if re.search(r"(Embedding$|^linearMap$|Linear$|CLM$|Bundled$|Continuous$|LinearMap$|^proj$|Topology$)", n):
        return True, "bundling / embedding wrapper of another definition (by name)"
    ret = sig.split(":")[-1]
    if re.search(r"(≃⋆ₐ|≃ₗᵢ|≃\*|≃\+|≃ₗ|≃ |↪)", ret) and k == "def":
        return True, "isomorphism / embedding between carriers (transport)"
    btoks = d["n_body_tokens"]
    if k == "def" and btoks <= 12 and " where" not in body[:8] and "match" not in body and "\n|" not in body:
        return True, "short renaming/abbreviation (body <= 12 tokens)"
    return False, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("families", nargs="+")
    ap.add_argument("--repo", default="data/raw/openai-math")
    ap.add_argument("--catalog", default="data/catalog_families.csv")
    ap.add_argument("--out", default="data/items")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--no-follow-imports", action="store_true")
    args = ap.parse_args()
    repo, out = Path(args.repo), Path(args.out)
    catalog = pd.read_csv(args.catalog, dtype={"family_id": str})
    out.mkdir(parents=True, exist_ok=True)
    for fid in args.families:
        fid = fid.zfill(3)
        res = build(fid, repo, catalog, follow_imports=not args.no_follow_imports)
        if res is None:
            print(f"{fid}: no Lean formalization")
            continue
        (out / f"{fid}_lean.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
        s = res["summary"]
        print(f"\n=== {fid}  dirs={s['lean_dirs']} + imported {s['imported_oai_dirs']}  files={s['n_files']}  decls={s['n_decls']}  kinds={s['kind_counts']}")
        print(f"targets found {len(s['targets_found'])}/{len(s['targets'])}; proof DAG {s['n_proof_dag']} decls / {s['n_proof_dag_theorems']} theorems (with siblings {s['n_proof_dag_with_siblings']})")
        print("import groups:", {k: len(v) for k, v in s["import_groups"].items()})
        byn = {d["name"]: d for d in res["declarations"]}
        print(f"{len(s['candidate_defs'])} candidate defs (non-plumbing, outside target statement, in DAG, multi-file, in a theorem signature). Top:")
        for n in s["candidate_defs"][: args.top]:
            d = byn[n]
            print(f"   dom={d['dominated_share']:.3f} share={d['frac_dag_dependents']:.2f} sigs={d['n_thm_signatures_using']:3d} files={d['n_files_using']:2d}  {d['kind']:9s} {n}")
        print(f"{len(s['candidate_lemmas'])} candidate lemmas (dominated share >= 2%). Top:")
        for n in s["candidate_lemmas"][: args.top]:
            d = byn[n]
            print(f"   dom={d['dominated_share']:.3f} share={d['frac_dag_dependents']:.2f} files={d['n_files_using']:2d}  {n}")


if __name__ == "__main__":
    main()
