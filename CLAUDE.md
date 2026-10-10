# AI-Hard

This project tests an AI-easy / AI-hard hypothesis, a stronger form of LIMA's Superficial Alignment Hypothesis:
- **AI-easy:** resolvable by recombining existing definitions and theorems.
- **AI-hard:** needs a *jump*, i.e. a eureka step or non-analytic cut.

The corpus is OpenAI's Oct 6, 2026 math release (`openai/math`, 372 families / 719 manuscripts), pinned at commit `fd4aeeb`. The full plan and codebook are in `docs/PLAN.md`; read it first.

## Setup (fresh clone or cloud session)
- `bash scripts/fetch_release.sh` fetches the release into `data/raw/openai-math`. It is not committed.
- `python scripts/build_catalog.py` rebuilds `data/catalog_*.csv`.
- `python scripts/extract_lean.py` regenerates `data/items/`. That output is not committed (~117 MB).
- Python on Windows: use `sys.stdout.reconfigure(encoding="utf-8")` when printing Unicode.

## The jump definition is STRICT
- Bringing a known concept from another field is **transfer (N0), not a jump**.
- Novelty is judged against ALL existing mathematics (Mathlib plus the literature, every field). Never judge it against the home field or the theorem statement.
- The anchor example is PHP in extended resolution. Cook–Reckhow extension variables are syntactically tiny but hard to construct, and they turn exponential proofs polynomial. Syntactic size is irrelevant.
- Grades:
  - N2 = a close variant.
  - A "new bridge" between fields is measured separately and is not automatically a jump.
  - N3 = eureka *candidate* only.
- **Confirmed eureka step** = N3 *plus* a downstream speedup test: the item makes OTHER theorems provable with much less budget. A corollary of the item's own theorem is not reuse of the device. None is confirmed yet.
- The speedup and discoverability tests run **in Lean** (Mathlib d13f23b plus the OAI library at fd4aeeb, toolchain v4.34.1). Only Lean-formalized items are on the shortlist.

## Where things are
- `docs/`: PLAN.md and the agent briefs. The briefs cover the trace, family, novelty, F1 transfer and downstream agents.
- `data/pilot/<fid>/`: per-family agent outputs: paper, family, lean, trace, novelty, f1_*, downstream (.json + .md).
- `data/eureka_shortlist.json`: priority tiers of Lean-formalized N3 items, F1 review verdicts, and `excluded_no_lean`.
- `data/random_batch_1.json`: random sample of 10 families (seed 20261009).
- `scripts/build_dashboard_data.py` → `data/dashboard/*.json`. Then `scripts/publish_dashboard.py data/dashboard/assets.json` builds the store docs for the Claude artifact dashboard (https://claude.ai/artifact/8BWuJsxoZqHYLFncNeZ9Mi). Its page is `dashboard/index.html`.
- `scripts/api_pipeline.py`: an Anthropic API version of the family and novelty agents. It needs `ANTHROPIC_API_KEY`; never commit a key.

## Working style
- The user thinks in proof-complexity / SAT terms. Record analogies quantitatively, e.g. CDCL backtracks, restarts and learned clauses in the reasoning traces.
- The user adds requirements incrementally; fold each one into `docs/PLAN.md`.
