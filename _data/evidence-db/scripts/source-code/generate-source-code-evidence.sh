#!/usr/bin/env sh


set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
export SOKRATES_REPORT_URL_PREFIX=https://d3axxy9bcycpv7.cloudfront.net/aws
# SOKRATES_REPORT_URL_PREFIX="${1:?Usage: ./generate-source-code-evidence.sh <sokrates-report-url-prefix>}"

python3 "$SCRIPT_DIR/generate-source-code-evidence.py" \
  --input "$SCRIPT_DIR/../../../data/sokrates/repositories.json" \
  --output "$SCRIPT_DIR/../../database/evidence-files/source-code.json" \
  --sokrates-report-url-prefix "$SOKRATES_REPORT_URL_PREFIX"
