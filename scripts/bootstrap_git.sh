#!/usr/bin/env bash
set -euo pipefail

repo_name="${1:-industrial-controls-learning-lab}"

if [[ -d .git ]]; then
  echo "A Git repository already exists in $(pwd)." >&2
  exit 1
fi

git init
git add .
git commit -m "chore: initialize ${repo_name}"
git branch -M main

cat <<MSG
Local Git repository created on branch main.

Next steps:
  1. Create an empty public GitHub repository named: ${repo_name}
  2. Replace maintainer/contact/URL placeholders listed in MAINTAINERS.md
  3. Add the remote and push:

     git remote add origin https://github.com/parthoece/industrial-controls-learning-lab.git
     git push -u origin main
MSG
