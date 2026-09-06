# Next review batch: 60 existing knowls

Status: planned, not executed. The exact, nonoverlapping ownership manifest is
`../knowlpedia-content/reviews/next-batch.json`: five lanes of twelve knowls.

| Lane | Reading question |
|---|---|
| Linear geometry | How do inner products produce orthogonality, projections, and operator norms? |
| Ring conventions | Which results require a multiplicative identity or preservation of it? |
| Metric foundations | How do convergence, completeness, and continuity fit together? |
| Integration foundations | Which partition definition and integrator hypotheses support each theorem? |
| Functions and quotients | Are domains, inverse images, and equivalence classes distinguished consistently? |

Each author reads its assigned pages and the prerequisites needed to understand
them before editing. Neighboring pages are read-only unless the coordinator
reassigns ownership. The coordinator owns shared runtime, redirects, indexes,
and the ledger; authors return per-ID findings and evidence. Useful unchanged
pages stay unchanged. Do not create a new example or section merely to record a
correction. Record inaccessible sources and unresolved claims explicitly.

Run the five author lanes concurrently. Then assign two independent review
passes across the proposed changes: one for hypotheses/conventions and one for
reading flow and duplicate scope. Reviewers report findings to the owners;
they do not concurrently rewrite the same files. The coordinator resolves
cross-lane conventions, checks two-prerequisite reading exercises, runs source,
unit, browser and rendered-output checks, and refreshes the cumulative diff.

For each assigned ID report full, targeted, or dependency-only review; corrected,
reviewed unchanged, or redirected outcome; inspected source locators; and any
remaining assumptions. Only completed full reviews receive a current-source
SHA-256 in the ledger. A blocked or targeted review remains in the backlog.
New pages and redirects are separate statistics, not extra corrections.

After the batch, regenerate `docs/refactor-progress.md` and publish the exact
number assigned, fully reviewed, corrected, unchanged, deferred, and returned
for rework. Measure actual review time before estimating throughput; this first
small, selected batch does not justify a completion date for the entire corpus.
At sixty completed full reviews per batch, the current backlog needs roughly
58 further batches; deferrals and later source changes can increase that number.
Select subsequent batches from `scripts/review_progress.py --json`, prioritizing
frequently used prerequisites and demonstrated inconsistencies rather than
alphabetical coverage. Stop expanding parallelism if integration or mathematical
review becomes the bottleneck.
