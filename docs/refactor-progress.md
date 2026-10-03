# Refactor progress

Fixed content baseline: `ea7256bd`. Counts come from the review ledger and Git sources.

| Measure | Count |
|---|---:|
| Knowls in the fixed starting corpus | 3,491 |
| Starting knowls with a recorded content correction | 151 |
| Starting knowls fully reviewed at their current source revision | 2,115 |
| Starting knowls still requiring full review | 1,376 |
| Starting knowls consolidated into compatibility redirects | 61 |
| Full reviews invalidated by subsequent source changes | 1,378 |
| Current canonical knowls (including collections) | 4,886 |
| New knowls added since the baseline | 1,457 |
| Current prerequisite lists with a recorded review | 4,518 |

Corrections, full reviews, prerequisite reviews, and consolidations overlap; do not add them together. A targeted correction does not complete a full review. Metadata-only changes do not count as corrected content. New knowls do not reduce the fixed backlog. A full review counts only while its recorded source hash matches; later edits return it to the pending queue. These are recorded AI editorial reviews, not mathematical certification.

Regenerate with `python3 scripts/review_progress.py --output docs/refactor-progress.md`. Use `--json` for the exact pending/reviewed ID lists. The evidence ledger is `../knowlpedia-content/reviews/refactor-ledger.json`.
