#!/bin/bash
# usage: sync_push.sh "notes commit msg" "content commit msg"
set -e
cd /home/codex/code/knowlpedia-root
rsync -a --delete --exclude 'corpus-index.tsv' --exclude 'prompts' --exclude '*.parts' --exclude '*.body.md' --exclude 'concepts-merged.json' --exclude 'unresolved-*.tsv' documents/riemann2/ knowlpedia/docs/riemann2/
git -C knowlpedia add -A; git -C knowlpedia commit -q -m "$1" || true; git -C knowlpedia push -q
git -C knowlpedia-content add -A; git -C knowlpedia-content commit -q -m "$2" || true; git -C knowlpedia-content push -q
git -C knowlpedia-content log --oneline | head -1
