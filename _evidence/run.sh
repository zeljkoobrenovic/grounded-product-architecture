#!/bin/bash

set -eu

bash scripts/source-code/generate-source-code-evidence.sh
bash scripts/gcp/generate-gcp-evidence.sh
bash scripts/aws/generate-aws-evidence.sh
bash scripts/workday/generate-workday-evidence.sh

python3 database/aggregate-evidence.py

# Regenerate the static Evidence Explorer page from the aggregated database.
python3 ../../_wiring/evidence-explorer/generate-evidence-explorer-docs.py
