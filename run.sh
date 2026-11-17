#!/bin/sh
# usage: run.sh <repo> <arm A|B> <n>
set -u
T=$(cd "$(dirname "$0")" && pwd); R=$1; ARM=$2; N=$3
case $ARM in A) SRC=$T/fixtures/$R;; B) SRC=$T/fixtures-b/$R;; esac
D=$T/runs/$R-$ARM-$N; rm -rf "$D"; cp -c -R "$SRC" "$D"; cd "$D"
case $R in
  svelte)  ALLOW='Bash(npm run check) Bash(npm run check:*) Bash(npx svelte-kit sync) Bash(npm run db\:generate)';  CHECK='npm run check';;
  axum)    ALLOW='Bash(cargo build) Bash(cargo build:*) Bash(cargo check) Bash(cargo check:*)';                       CHECK='cargo build';;
  fastapi) ALLOW='Bash(uv run pytest) Bash(uv run pytest:*)';                                                         CHECK='uv run pytest -q';;
esac
START=$(date +%s)
claude -p "$(cat "$T/prompts/$R.txt")" --model claude-sonnet-5-5 \
  --setting-sources project --strict-mcp-config --mcp-config "$T/c7-mcp.json" \
  --disable-slash-commands --no-session-persistence --max-budget-usd 3 \
  --disallowedTools WebSearch WebFetch \
  --allowedTools Read Glob Grep Edit Write mcp__context7 $ALLOW \
  --output-format stream-json --verbose > "$T/runs/$R-$ARM-$N.jsonl" 2> "$T/runs/$R-$ARM-$N.err"
END=$(date +%s)
cd "$D"; sh -c "$CHECK" > "$T/runs/$R-$ARM-$N.check" 2>&1; echo "exit=$? wall=$((END-START))" >> "$T/runs/$R-$ARM-$N.check"
echo "$R-$ARM-$N done: $(tail -1 "$T/runs/$R-$ARM-$N.check")"
