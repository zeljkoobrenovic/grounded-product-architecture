echo "[1/7] CODEX: Starting update round for $1 by reviewing the content and improving it based on the review."
codex exec "Review $1 using the gpa-product-domain-review skill."

echo "[2/7] CLAUDE: Improving the content based on the review."
claude -p "Improve $1 based on REVIEW.md." --allowedTools "Read,Edit,Bash"

echo "[3/7] CODEX: Updating review of $1 based on recent changes and improving the content based on the review."
codex exec "Update review of $1 based on recent changes using the gpa-product-domain-review skill. Expand review with the in-depth review using gpa-product-bricks-review skil."

echo "[4/7] CLAUDE: Improving $1 based on the updated review."
claude -p "Improve $1 based on the updated REVIEW.md" --allowedTools "Read,Edit,Bash"

echo "[5/7] CODEX: Updating review of $1 based on recent changes and improving the content based on the review."
codex exec "Update review of $1 based on recent changes. Expand review with the in-depth review gpa-teams-review skil."

echo "[6/7] CLAUDE: Improving $1 based on the updated review."
claude -p "Improve $1 based on the updated REVIEW.md" --allowedTools "Read,Edit,Bash"

echo "[7/7] CLAUDE: Polishing $1 for better understandability, readability, flows, and overall quality."
claude -p "Make one more pass in $1 of lightweight edits and polishing to improve understandability, readability, flows, and overall quality." --allowedTools "Read,Edit,Bash"

