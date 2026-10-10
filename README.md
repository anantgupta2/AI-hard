# AI-Hard

Do AI-produced proofs contain genuine *jumps*? This repository analyses OpenAI's Oct 6, 2026 math release ([openai/math](https://github.com/openai/math), pinned at `fd4aeeb`). It sorts the proofs into AI-easy (recombining existing definitions and theorems) and AI-hard (needing a eureka step), testing a stronger form of LIMA's Superficial Alignment Hypothesis.

- `docs/PLAN.md`: the codebook (axes A–F, novelty grades N0–N3, eureka types F1–F5), the CDCL coding of the reasoning traces, and the speedup test.
- `data/pilot/<family>/`: per-family analyses.
- `data/eureka_shortlist.json`: Lean-formalized eureka candidates, ranked. **None is a confirmed eureka step.**
- `scripts/`: catalogue, Lean extraction and dashboard builders. Run `scripts/fetch_release.sh` to fetch the release.

The analyses are model-assisted judgements on unreviewed mathematics, not results.

`data/traces/` holds text extracted from the release's reasoning-trace PDFs. The quoted Lean and LaTeX excerpts also come from the release. openai/math is licensed under Apache-2.0.
