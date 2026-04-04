#!/bin/bash

set -eu

bash generate-source-code-evidence.sh
bash generate-gcp-evidence.sh
bash generate-aws-evidence.sh
bash generate-workday-evidence.sh

python3 aggregate-evidence.py
