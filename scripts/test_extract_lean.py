"""Regression checks for scripts/extract_lean.py name resolution.

Run: python scripts/test_extract_lean.py   (or: pytest scripts/test_extract_lean.py)

The synthetic tree reproduces the family-103 bug (2026-10-10): in
OAI/Computability/Logspace/ProbabilityHierarchy.lean, `def kOK (T : ℕ) := ... T.factorial ...`
means Nat.factorial, but v2 linked it to the local lemma Hie.factorial (the only in-tree decl
with short name `factorial`), giving Hie.residual / substochastic / factorial 912 dependents.
If the release is fetched (data/raw/openai-math, or $OPENAI_MATH_REPO), the real 103 file is
checked too.
"""

import os
import sys
import tempfile
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_lean import build  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REAL_REPO = Path(os.environ.get("OPENAI_MATH_REPO", ROOT / "data" / "raw" / "openai-math"))

FAKE = {
    "OAI/Fake/Hie.lean": """
namespace OAI
namespace Hie

structure Stg where
  D : ℕ
  f : ℕ

def residual (n : ℕ) : ℕ := n + 1

lemma factorial (S : ℕ) (T : ℕ) : residual T ≤ residual T * T.factorial := by
  simp [residual]

lemma add_apply (x : ℕ) : residual x = x + 1 := rfl

def A : ℕ := 5

def kOK (T : ℕ) := 0 < T ∧ (5 / A) ^ T / T.factorial ≤ 1

def kOK2 (n : ℕ) := Nat.factorial n ≤ 1 ∧ (fun i => (Pi.add_apply i)) = id

def stgUse (p : Stg) : ℕ := p.D + p.f

def P (n : ℕ) : ℕ := n

theorem letShadow (x : ℕ) : x = x := by
  let P := P x
  have h : P = P := rfl
  rfl

theorem letInStatement (x : ℕ) : x = let P := P x
    P := rfl

end Hie

namespace Line
def width : ℕ := 3
end Line
end OAI
""",
    "OAI/Fake/Main.lean": """
import OAI.Fake.Hie

namespace OAI
namespace Top
open Hie

theorem main (T : ℕ) (h : kOK T) : stgUse ⟨T, T⟩ = T + T := by
  have hA : A = 5 := rfl
  let A := T.succ
  exact (A.factorial_pos).trans_le le_rfl

end Top
end OAI

namespace Outer
open OAI
open Line

theorem chained : width = 3 := rfl

end Outer
""",
}


def build_fake(tmp):
    for rel, src in FAKE.items():
        p = Path(tmp) / "lean" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(src, encoding="utf-8")
    cat = pd.DataFrame([{
        "family_id": "999",
        "lean_dirs": "OAI/Fake",
        "lean_declarations": "OAI.Top.main;Outer.chained",
    }])
    res = build("999", Path(tmp), cat)
    return {d["name"]: d for d in res["declarations"]}


def test_local_field_notation_on_external_type():
    with tempfile.TemporaryDirectory() as tmp:
        by = build_fake(tmp)
    # `T.factorial` with `T : ℕ` is Nat.factorial, not the local Hie.factorial
    assert by["OAI.Hie.kOK"]["uses"] == ["OAI.Hie.A"], by["OAI.Hie.kOK"]["uses"]
    # v2: main -> kOK -> factorial -> residual made both look load-bearing for main
    assert by["OAI.Hie.residual"]["n_dependents"] == 0
    assert by["OAI.Hie.factorial"]["n_dependents"] == 0


def test_qualified_names_are_not_matched_by_last_component():
    with tempfile.TemporaryDirectory() as tmp:
        by = build_fake(tmp)
    # `Nat.factorial`, `Pi.add_apply` are Mathlib names, not Hie.factorial / Hie.add_apply
    assert by["OAI.Hie.kOK2"]["uses"] == [], by["OAI.Hie.kOK2"]["uses"]


def test_positive_controls():
    with tempfile.TemporaryDirectory() as tmp:
        by = build_fake(tmp)
    # field notation on an in-tree structure resolves to it
    assert by["OAI.Hie.stgUse"]["uses"] == ["OAI.Hie.Stg"], by["OAI.Hie.stgUse"]["uses"]
    # unqualified names resolve through `open Hie`; `A` in `have hA : A = 5` is still Hie.A
    assert set(by["OAI.Top.main"]["uses"]) == {"OAI.Hie.kOK", "OAI.Hie.stgUse", "OAI.Hie.A"}, by["OAI.Top.main"]["uses"]
    # `open OAI` then `open Line` opens OAI.Line (Lean 4 resolves opens through earlier opens)
    assert by["Outer.chained"]["uses"] == ["OAI.Line.width"], by["Outer.chained"]["uses"]


def test_local_shadows_global():
    src = FAKE["OAI/Fake/Main.lean"]
    with tempfile.TemporaryDirectory() as tmp:
        FAKE["OAI/Fake/Main.lean"] = src.replace("  have hA : A = 5 := rfl\n", "")
        try:
            by = build_fake(tmp)
        finally:
            FAKE["OAI/Fake/Main.lean"] = src
    # `let A := T.succ` binds A: `A.factorial_pos` is field notation on the local, not Hie.A
    assert "OAI.Hie.A" not in by["OAI.Top.main"]["uses"], by["OAI.Top.main"]["uses"]


def test_let_rhs_is_global():
    with tempfile.TemporaryDirectory() as tmp:
        by = build_fake(tmp)
    # in `let P := P x` the right-hand `P` is the global Hie.P (358: `let P := P δ ..` -> Cometric.P)
    assert by["OAI.Hie.letShadow"]["uses"] == ["OAI.Hie.P"], by["OAI.Hie.letShadow"]["uses"]
    # same inside a statement, where the signature is cut at the let's own `:=`
    assert by["OAI.Hie.letInStatement"]["uses"] == ["OAI.Hie.P"], by["OAI.Hie.letInStatement"]["uses"]


def test_real_family_103():
    if not (REAL_REPO / "lean" / "OAI").is_dir():
        print("  (skipped: release not fetched; run bash scripts/fetch_release.sh)")
        return
    cat = pd.read_csv(ROOT / "data" / "catalog_families.csv", dtype={"family_id": str})
    res = build("103", REAL_REPO, cat)
    by = {d["name"]: d for d in res["declarations"]}
    hie = "OAI.ExactDerandomization.Hie."
    assert hie + "factorial" not in by[hie + "kOK"]["uses"], by[hie + "kOK"]["uses"]
    n_thms = res["summary"]["n_proof_dag_theorems"]
    for n in ("residual", "substochastic", "factorial"):
        frac = by[hie + n]["n_dependents"] / n_thms
        assert frac < 0.2, (n, by[hie + n]["n_dependents"], n_thms)  # v2: 912 / 2579 = 0.35


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
