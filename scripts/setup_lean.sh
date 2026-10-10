#!/usr/bin/env bash
# Install Lean v4.34.1 and prepare the openai/math Lean project (data/raw/openai-math/lean) for building.
# Also works where releases.lean-lang.org, reservoir.lean-lang.org and the Mathlib cache hosts are blocked
# (as in Claude cloud sessions): the toolchain comes from GitHub release assets, dependencies are
# resolved from lake-manifest.json without `lake update` (whose Mathlib hook runs `cache get`), and
# the lakefile's post_update compatibility patches are applied by hand with the same checks.
# Finally it tries `lake exe cache get` for prebuilt Mathlib, falling back to a source build.
# Build only the modules you need, e.g.
#   (cd data/raw/openai-math/lean && lake build OAI.GroupTheory.Thompson.Main)
# Run scripts/fetch_release.sh first.
set -euo pipefail
cd "$(dirname "$0")/.."
LEAN_DIR=data/raw/openai-math/lean
VER=4.34.1
TC="leanprover/lean4:v$VER"

if [ ! -x "$HOME/.elan/bin/elan" ]; then
  curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh
  bash /tmp/elan-init.sh -y --default-toolchain none
fi
export PATH="$HOME/.elan/bin:$PATH"

if ! elan toolchain list | grep -q "v$VER"; then
  dest="$HOME/.elan/toolchains/manual-lean-$VER"
  if [ ! -x "$dest/bin/lean" ]; then
    tmp=$(mktemp -d)
    curl -sSfL -o "$tmp/lean.zip" "https://github.com/leanprover/lean4/releases/download/v$VER/lean-$VER-linux.zip"
    unzip -q "$tmp/lean.zip" -d "$tmp"
    mkdir -p "$(dirname "$dest")"
    mv "$tmp/lean-$VER-linux" "$dest"
    rm -rf "$tmp"
  fi
  elan toolchain link "$TC" "$dest"
fi
lean --version

cd "$LEAN_DIR"
# Clones every git dependency at its manifest revision; the lakefile's run_cmd patches 11 packages here.
lake env true

# The other 12 patches are applied by the lakefile's post_update hook, which only runs on `lake update`.
for name in fixed-point-theorems PrimeNumberTheoremAnd Zeta3Irrational rellich-kondrachov carleson \
    StrongPNT AbsorptionCutoff AINTLIB ClassFieldTheory schoenflies-lean SphereEversion gromov; do
  patch="$PWD/patches/$name-lean4341.patch"
  dir=".lake/packages/$name"
  if git -C "$dir" apply --check --reverse "$patch" 2>/dev/null; then
    echo "$name: patch already applied"
  elif git -C "$dir" apply --check "$patch" 2>/dev/null; then
    git -C "$dir" apply --whitespace=nowarn "$patch"
    git -C "$dir" apply --check --reverse "$patch"
    echo "$name: patch applied"
  else
    echo "$name: patch CONFLICTS with local changes" >&2
    exit 1
  fi
done

# Prebuilt Mathlib (needs cache.mathlib.org and lakecache.blob.core.windows.net in the network allowlist).
if lake exe cache get; then
  echo "Mathlib cache downloaded."
else
  echo "Mathlib cache unavailable; Mathlib will compile from source on the first build." >&2
fi
