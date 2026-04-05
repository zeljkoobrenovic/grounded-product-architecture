#!/bin/bash

set -eu

bash scripts/source-code/generate-source-code-evidence.sh
bash scripts/gcp/generate-gcp-evidence.sh
bash scripts/aws/generate-aws-evidence.sh
bash scripts/workday/generate-workday-evidence.sh
bash scripts/domain-objectives/generate-domain-objectives-evidence.sh

python3 database/aggregate-evidence.py
