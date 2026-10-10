#!/usr/bin/env bash
# Re-create data/raw/openai-math: the openai/math release pinned at fd4aeeb.
# Partial clone (no blobs until needed) with a sparse checkout that skips PDFs except the reasoning traces.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/raw
if [ ! -d data/raw/openai-math/.git ]; then
  git clone --filter=blob:none --no-checkout https://github.com/openai/math.git data/raw/openai-math
fi
cd data/raw/openai-math
git sparse-checkout init --no-cone
printf '/*\n!*.pdf\n/reasoning_traces/*.pdf\n' > .git/info/sparse-checkout
git checkout fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb
echo "openai/math at $(git rev-parse --short HEAD)"
