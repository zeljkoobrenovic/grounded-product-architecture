#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

scripts=(
  "generate-start-docs.py"
  "generate-customers-docs.py"
  "generate-products-docs.py"
  "generate-product-bricks-docs.py"
  "generate-teams-docs.py"
  "generate-competition-docs.py"
)

domains=(
"digital-medication-management|Online Retail Marketplace|The Online Retail Marketplace domain covers the shopper, Prime, seller, fulfillment, retail-media, trust, and shared-commerce workflows required to run a scaled digital retail marketplace across first-party retail, third-party"
)

for script in "${scripts[@]}"; do
  for domain in "${domains[@]}"; do
    IFS='|' read -r domain_id domain_name domain_description <<< "$domain"
    python3 "$script" "$domain_id" "$domain_name" "$domain_description"
  done
done
