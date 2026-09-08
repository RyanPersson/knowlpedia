# Reasons in the content comparison

The comparison generator displays a **Why this changed** section above each
source diff. Its explanations come from the content repository's versioned
`reviews/dependency-structure/*.json` ledgers, using the `changes`, `reason`,
`evidence`, and `sources` fields in `reviews` records. It does not infer reasons
from the diff or publish `triage_records` as reviews.

For a comparison between Git refs, the generator reads the ledgers from the
proposed ref, alongside that ref's content. Uncommitted ledger changes cannot
alter explanations for an older committed comparison. Working-tree comparisons
use the working-tree ledgers.

A record's `source_sha256` must match the displayed proposed source to appear
as a matching note. Deleted knowls use the displayed baseline source instead.
Other records remain available under **Notes for other source versions**;
they can explain earlier decisions but may describe changes later revised.
Missing explanations are stated explicitly. Review notes describe a knowl as
a whole and are not guaranteed to explain every diff line separately.

Each comparison also lists prerequisite additions and removals from the two
displayed sources. **Download original review records** exports the original
records, ledger paths, zero-based record indices, ledger revision, and source
matching status as JSON under the generated comparison's `notes/` directory.

Generate the complete dependency comparison with:

```bash
python3 scripts/generate_content_review.py \
  --content-repo ../knowlpedia-content \
  --left-ref develop --right-ref HEAD \
  --output public-imported/review/dependency-structure \
  --include-added --include-deleted \
  --heading 'Dependency structure review'
```

When improving an explanation, update the content ledger with the actual
reason and evidence. Retain older decisions as historical records; do not
relabel their hashes to make them appear to verify a different source.
