#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
pnpm typecheck
pnpm test
(cd api-gateway && go test ./...)
PYTHONPATH=booking-api python3 -m unittest discover -s booking-api/tests -v
python3 -m compileall -q booking-api/app
git diff --check
for file in README.md DESIGN.md SUMMARY.md coverage-matrix.md docs/git-history.md; do test -f "$file"; done
for id in R01 R02 R03 R04 R05 R06 R07 R08 R09 R10 R11 R12; do test -f "docs/issues/$id.md"; test -f "solutions/$id.md"; done
