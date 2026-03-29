#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir"

for script in \
    generate-start-docs.py \
    generate-customers-docs.py \
    generate-products-docs.py \
    generate-product-bricks-docs.py \
    generate-objectives-docs.py \
    generate-delivery-docs.py \
    generate-teams-docs.py
do
    python3 "$script"
done
