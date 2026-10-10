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

v3 changes (family 103 bug, 2026-10-10):
  * generalized field notation `x.foo` now follows Lean: if `x` is a local whose binder type
    has a head constant `C` (signature binders, section `variable`s, or `have`/`fun`/`∀`/`∃`
    binders in the body), `x.foo` resolves to `C.foo` exactly. An external `C` (ℕ, ℝ, Finset,
    Mathlib predicates ...) gives no edge. v2 linked `x.foo` to any unique in-tree decl with
    short name `foo`, e.g. `T.factorial` (`T : ℕ`, i.e. `Nat.factorial`) -> `Hie.factorial`
    in 103, which gave Hie.residual/substochastic/factorial 912 spurious dependents. Locals of
    unknown type (no binder type, a type variable, `h : H.Good`) keep the v2 heuristic;
  * locals shadow globals: a bound name is not looked up as a global constant (a body binder
    only from its binding position on);
  * a capitalized head that is not a bound local (e.g. `Nat.`, `Pi.`, `Fin.`, `Relation.`) is
    a namespace: the token resolves only to a decl whose full name ends with the whole dotted
    token, never by its last component (v2: `Pi.add_apply` -> `Hie.add_apply`);
  * `open B` also resolves `B` through namespaces opened earlier (`open SiteX` then
    `open Line` opens `SiteX.Line`), as Lean 4 does, and `open _root_.A.B` is handled.
  Regression checks: scripts/test_extract_lean.py.

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
NAME = r"[^\W\d][\w'!?₀-₉ₐ-ₜ]*"
NOTATION_TYPES = {"ℕ": "Nat", "ℤ": "Int", "ℚ": "Rat", "ℝ": "Real", "ℂ": "Complex", "ℝ≥0": "NNReal", "ℝ≥0∞": "ENNReal"}
# a type with one of these at bracket depth 0 is not `C args`: its head constant is not read off the text
TYPE_INFIX = set("≤<≥>=≠∈∉⊆⊂⊇⊃∣∧∨↔→×∘•+*/^⁻∀∃λ|")
BINDER_RE = re.compile(r"[\(\{⦃\[]\s*(%s(?:\s+%s)*)\s*(:(?!=)|[\)\}⦄\]])" % (NAME, NAME))
BODY_TYPED_RE = re.compile(r"(?:\bfun|λ|∀|∃!?|\bhave|\blet|\bset)\s*\(?\s*(%s(?:\s+%s)*)\s*:(?!=)" % (NAME, NAME))
# untyped binders of plain names: `let A := ..`, `fun x y =>`, `intro x y`, `∀ x y, ..`
BODY_UNTYPED_RE = re.compile(
    r"(?:\bfun|λ|∀|∃!?|\bintros?|\brintro|\blet|\bhave|\bset)[ \t]+((?:%s[ \t]*)+)(?=:=|=>|[,↦\n]|$)" % NAME
)
BODY_BOUND_RE = re.compile(
    r"(?:\bfun|λ|∀|∃!?|\bintros?|\brintro|\bobtain|\brcases|\bwith|\bchoose|\bgeneralize|\bhave|\blet|\bset|^\s*\|)"
    r"([^\n:=↦,]*)", flags=re.M
)
ANON_BOUND_RE = re.compile(r"(?<=[⟨,])\s*(%s)\s*(?=[,⟩])" % NAME)


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


def binder_part_end(sig):
    """Index of the first `:` at bracket depth 0 (start of the declared type), else len(sig)."""
    depth = 0
    for i, c in enumerate(sig):
        if c in "([{⟨⦃":
            depth += 1
        elif c in ")]}⟩⦄":
            depth = max(0, depth - 1)
        elif c == ":" and depth == 0 and not sig.startswith(":=", i):
            return i
    return len(sig)


def type_extent(text, i):
    """End of a binder type starting at text[i]: an unmatched close bracket, or `,` `:=` `=>` `↦`
    or a newline at depth 0."""
    depth, j, n = 0, i, len(text)
    while j < n:
        c = text[j]
        if c in "([{⟨⦃":
            depth += 1
        elif c in ")]}⟩⦄":
            if depth == 0:
                return j
            depth -= 1
        elif depth == 0 and (c in ",\n" or text.startswith((":=", "=>", "↦"), j)):
            return j
        j += 1
    return n


def type_head(ty):
    """Head constant of a binder type written `C args` (ℕ, ℝ, ... mapped to Nat, Real, ...);
    None for arrows, relations, binders and anything else whose head is not read off the text."""
    ty = " ".join(ty.split()).lstrip("@")
    if ty in NOTATION_TYPES:
        return NOTATION_TYPES[ty]
    depth = 0
    for c in ty:
        if c in "([{⟨⦃":
            depth += 1
        elif c in ")]}⟩⦄":
            depth -= 1
        elif depth == 0 and c in TYPE_INFIX:
            return None
    m = IDENT_RE.match(ty)
    return NOTATION_TYPES.get(m.group(0), m.group(0)) if m else None


def binder_info(binder_part, var_text, body):
    """Locals of one declaration: (strong, weak, types, bind_pos).
    strong = names bound by a binder group at depth 0 of the signature's binder part or of the
    section `variable`s, or by a `fun`/`∀`/`∃`/`have`/`let`/`set`/`intro` binder in the body;
    weak = strong plus names bound by intro/obtain/rcases/with/`|`/⟨..⟩ patterns;
    types = {name: head constant of its binder type, or None if unknown or conflicting}.
    Signature binders win over section variables, which win over body binders.
    bind_pos = {name: (scope start, binder spans)} for names bound only in the body: the scope
    starts at the end of the line of the first binding, so earlier occurrences and the binder's
    own right-hand side (`let P := P δ x`) are not shadowed (`have : A = 5` ... `let A := ..`)."""
    levels = []
    for text in (binder_part, var_text):
        lv, depth, pos = defaultdict(set), 0, 0
        for m in BINDER_RE.finditer(text):
            for c in text[pos : m.start()]:
                depth += c in "([{⟨⦃"
                depth -= c in ")]}⟩⦄"
            pos = m.start()
            if depth != 0:
                continue  # nested group: a type ascription inside a binder type, not a binder
            opener, typed = text[m.start()], m.group(2) == ":"
            if opener == "[" and not typed:
                continue  # anonymous instance binder `[C α]` binds nothing
            head = type_head(text[m.end() : type_extent(text, m.end())]) if typed else None
            for n in m.group(1).split():
                lv[n].add(head)
        levels.append(lv)
    lv, first, spans = defaultdict(set), {}, defaultdict(list)
    for head, m in [(None, m) for m in BODY_UNTYPED_RE.finditer(body)] + \
            [(type_head(body[m.end() : type_extent(body, m.end())]), m) for m in BODY_TYPED_RE.finditer(body)]:
        # scope starts after the line holding the binder's `:=` (which may follow a line break:
        # split_signature cuts `.. = let P\n:= P δ x` at the let's own `:=`)
        rest = body[m.end(1) :]
        j = m.end(1) + len(rest) - len(rest.lstrip())
        eol = body.find("\n", j + 2 if body.startswith(":=", j) else m.end(1))
        for n in m.group(1).split():
            lv[n].add(head)
            if n not in first or m.start(1) < first[n][0]:
                first[n] = (m.start(1), len(body) if eol < 0 else eol)
            spans[n].append((m.start(1), m.end(1)))
    levels.append(lv)
    types = {}
    for lv in levels:
        for n, heads in lv.items():
            if n not in types:
                types[n] = next(iter(heads)) if len(heads) == 1 else None
    strong = set(types)
    weak = set(strong)
    for m in BODY_BOUND_RE.finditer(body):
        weak.update(t for t in IDENT_RE.findall(m.group(1)) if "." not in t)
    weak.update(ANON_BOUND_RE.findall(body))
    bind_pos = {}
    for n, (_, scope) in first.items():
        if n not in levels[0] and n not in levels[1]:
            bind_pos[n] = (scope, spans[n])
    return strong, weak, types, bind_pos


def parse_file(path, rel):
    raw = path.read_text(encoding="utf-8", errors="replace")
    docs = {}  # line index -> preceding docstring
    for m in re.finditer(r"/--(.*?)-/", raw, flags=re.S):
        end_line = raw[: m.end()].count("\n")
        docs[end_line + 1] = " ".join(m.group(1).split())
    lines = strip_comments(raw).split("\n")
    imports = [l.split()[1] for l in lines if l.startswith("import ")]
    # scope stack: list of dicts {kind, parts, opens, vars}
    stack, decls, cur = [], [], None

    def cur_ns():
        return [p for fr in stack if fr["kind"] == "namespace" for p in fr["parts"]]

    def cur_opens():
        out = []
        for fr in stack:
            out.extend(fr["opens"])
        return out

    def cur_vars():
        return file_vars + [v for fr in stack for v in fr["vars"]]

    file_opens = []  # opens at file top level
    file_vars = []  # `variable` command texts at file top level
    for i, line in enumerate(lines):
        s = line.strip()
        top = not line.startswith(("  ", "\t"))
        if top and s.startswith("namespace "):
            stack.append({"kind": "namespace", "parts": s.split()[1].split("."), "opens": [], "vars": []})
            cur = None
            continue
        if top and (s.startswith("section") or s.startswith("noncomputable section")):
            stack.append({"kind": "section", "parts": [], "opens": [], "vars": []})
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
        if top and s.startswith("variable"):
            # binder text of the command, including indented continuation lines
            j = i + 1
            while j < len(lines) and lines[j].startswith((" ", "\t")) and lines[j].strip():
                j += 1
            (stack[-1]["vars"] if stack else file_vars).append(" ".join(l.strip() for l in lines[i:j])[len("variable"):])
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
                "vars": " ".join(cur_vars()),
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
    short_index = defaultdict(set)  # last component -> decls
    suffix_index = defaultdict(set)  # dotted suffix of >= 2 components -> decls
    known_ns = set()  # every proper prefix of an in-tree name
    for n in names:
        parts = n.split(".")
        short_index[parts[-1]].add(alias_of.get(n, n))
        for i in range(1, len(parts) - 1):
            suffix_index[".".join(parts[i:])].add(alias_of.get(n, n))
        for i in range(1, len(parts)):
            known_ns.add(".".join(parts[:i]))

    def lookup(full, d):
        r = full if full in by_name else alias_of.get(full)
        if r and (by_name[r]["_pos"] < d["_pos"]):
            return r
        return None

    def visible(cands, d):
        return {c for c in cands if by_name[c]["_pos"] < d["_pos"]}

    canon_cache = {}

    def canonical_opens(opens):
        """`open B` (issued in namespace A.C) opens A.C.B, A.B, B, and P.B for every namespace P
        opened before it; keep the in-tree ones, in order."""
        key = tuple((tuple(c), o) for c, o in opens)
        if key not in canon_cache:
            out = []
            for ctx, o in key:
                if o.startswith("_root_."):
                    cands = [o[len("_root_.") :]]
                else:
                    cands = [".".join(ctx[:k] + (o,)) for k in range(len(ctx), -1, -1)] + [p + "." + o for p in out]
                out += [c for c in dict.fromkeys(cands) if c in known_ns and c not in out]
            canon_cache[key] = out
        return canon_cache[key]

    def resolve_global(tok, d):
        """Lean name resolution of a constant: enclosing namespaces of the decl, opens, root."""
        ns = d["name"].split(".")[:-1]  # namespaces of the decl's own full name
        for k in range(len(ns), -1, -1):
            r = lookup(".".join(ns[:k] + [tok]), d)
            if r:
                return r, "ns"
        for o in d["canon_opens"]:
            r = lookup(o + "." + tok, d)
            if r:
                return r, "open"
        return None, None

    def field_heuristic(parts, d):
        # field notation on a term of unknown type: a unique, non-generic short name
        for k in range(1, len(parts)):
            suffix = parts[k]
            if suffix in GENERIC_FIELDS:
                continue
            c = visible(short_index.get(suffix, set()), d)
            if len(c) == 1:
                return next(iter(c)), "field"
        return None, None

    def field_on_local(parts, d):
        """`x.foo` with x a bound local: Lean looks up `C.foo` for the head constant C of x's type."""
        ty = d["ltypes"].get(parts[0])
        if ty is None or not is_namespace_head(ty.split(".")[0], d):
            return field_heuristic(parts, d)  # unknown, a type variable, or `H.Correct` with H local
        X, _ = resolve_global(ty, d)
        if not X:  # an in-tree type behind an `open` the parser missed: unique full-name suffix
            c = {x for x in visible(suffix_index.get(ty, set()) if "." in ty else short_index.get(ty, set()), d)
                 if by_name[x]["kind"] in DEF_KINDS and x.endswith("." + ty)}
            X = next(iter(c)) if len(c) == 1 else None
        if X:  # in-tree type; fall back for parent structures / definitions that unfold
            r = lookup(X + "." + parts[1], d)
            return (r, "typed") if r else field_heuristic(parts, d)
        for c in [ty] + [o + "." + ty for o in d["canon_opens"]]:
            r = lookup(c + "." + parts[1], d)  # in-tree extension of an external type
            if r:
                return r, "typed"
        return None, "external"

    def is_namespace_head(head, d):
        return (head[0].isupper() and head not in d["weak"]
                and not re.fullmatch(r"[^\W\d][\d'!?₀-₉ₐ-ₜ]*", head))  # `T`, `A'`, `M₁` are locals

    def shadowed(head, tok, d):
        if head not in d["strong"]:
            return False
        if head not in d["bind_pos"]:
            return True  # signature binder or section variable
        scope, spans = d["bind_pos"][head]
        found = False
        for m in re.finditer(r"(?<![\w.'])%s(?![\w'!?₀-₉ₐ-ₜ]|\.[^\W\d])" % re.escape(tok), d["btext"]):
            if m.start() < scope and not any(a <= m.start() < b for a, b in spans):
                return False  # a use before the body binder is in scope: the global
            found = True
        return found  # not found: the token only occurs in the signature's binder part

    def resolve(tok, d):
        tok = tok.lstrip("@")
        if tok.startswith("_root_."):
            return lookup(tok[7:], d), "root"
        parts = tok.split(".")
        if shadowed(parts[0], tok, d):  # a bound local shadows every global of the same name
            return field_on_local(parts, d) if len(parts) > 1 else (None, None)
        r, how = resolve_global(tok, d)
        if r:
            return r, how
        # projection on a declared constant: `foo.exists`, `foo.le.trans` -> edge to `foo`
        # (the longest dotted prefix that resolves as a declaration in scope)
        for k in range(len(parts) - 1, 0, -1):
            r, _ = resolve_global(".".join(parts[:k]), d)
            if r:
                return r, "proj"
        if len(parts) == 1:
            return None, None
        if is_namespace_head(parts[0], d):
            # a qualified name (`Nat.factorial`, `Pi.add_apply`) that is not in scope: external,
            # unless one decl's full name ends with the whole token (or a dotted prefix of it,
            # then projection) - never matched by its last component alone
            for k in range(len(parts), 1, -1):
                c = visible(suffix_index.get(".".join(parts[:k]), set()), d)
                if len(c) == 1:
                    return next(iter(c)), "suffix"
            return None, "qualified"
        return field_heuristic(parts, d)

    for d in decls:
        sig = d["signature"]
        cut = binder_part_end(sig)
        d["btext"] = sig[cut:] + "\n" + d["body"]
        d["strong"], d["weak"], d["ltypes"], d["bind_pos"] = binder_info(sig[:cut], d["vars"], d["btext"])
        d["canon_opens"] = canonical_opens(d["opens"])

    mathlib_refs = Counter()
    n_field = n_typed = n_suffix = n_external = 0
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
                if tgt is None and how is None and "." in t:
                    suffix = t.split(".")[-1]
                    if suffix not in GENERIC_FIELDS and len(visible(short_index.get(suffix, ()), d)) > 1:
                        unresolved.append((suffix, cnt, t in sig_toks))
            if tgt and tgt != d["name"]:
                uses_all.add(tgt)
                occ[tgt] += cnt
                if t in sig_toks or (t.startswith("\u0000.") and ("." + t[2:]) in d["signature"]):
                    uses_sig.add(tgt)
                n_field += how in ("field", "dot")
                n_typed += how == "typed"
                n_suffix += how == "suffix"
            elif not tgt and not t.startswith("\u0000") and "." in t:
                n_external += how in ("external", "qualified")
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
        for k in ("opens", "vars", "canon_opens", "strong", "weak", "ltypes", "bind_pos", "btext", "_pos"):
            d.pop(k)

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
        "n_typed_field_links": n_typed,
        "n_qualified_suffix_links": n_suffix,
        "n_external_field_or_qualified_refs": n_external,
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
