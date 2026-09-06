# Complete the remaining review backlog

Started from app `73c9369`, content `8d94a2f7`, with both branches clean.
The user requests full review and correction of the entire remaining corpus.
The fixed baseline stays `ea7256bd`: 1,049 reviewed and 2,442 pending at start.
The exact nonoverlapping assignment manifest is
`../knowlpedia-content/reviews/remainder-plan.json`.

Review every pending entry, including the 64 earlier deferrals, existing
redirects, source collections and navigation containers. Use bounded subject
lanes of at most 50 entries and approximately 14,000 source words; the long
convex lecture document is its own assignment. Each author owns only its
listed sources. Root owns integration, boundary edits, audit disposition,
progress evidence, validation and the cumulative diff.

Accept full reviews only after the entire page and actual direct prerequisite
bodies have been read and all claims checked. Require early per-ID checkpoints.
Elementary direct reasoning can be evidence without external citations;
advanced or uncertain claims need inspected relevant primary sources. Resolve
unsupported claims before completing the backlog. Preserve useful unchanged
content and avoid redundant metadata edits to already-reviewed lists.

Independent integration audits check substantive changes, prerequisite
removals and claim-specific evidence. Restore necessary antecedents if an
attempted DAG repair removed them. Maintain zero prerequisite cycles, complete
source hashes and an explicit unresolved queue throughout. Do not treat
partial reports, metadata edits, or successful builds as full math reviews.

Integrate accepted batches into the existing ledger and regenerate progress.
Commit validated content and app changes on their existing branches. Rebuild
the existing port-8015 preview and refresh the cumulative diff from `ea7256bd`
after integrated batches. Finish only when the remaining full-review count is
zero and source, rendering and browser checks pass.
