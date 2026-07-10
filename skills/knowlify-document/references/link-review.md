# Candidate-link review

Use the scanner for recall and an agent or human for meaning. A lexical match is evidence that a link may be missing, not permission to insert one.

## Decision policy

Accept when the phrase is the first pedagogically useful introduction of a dependency, hypothesis, ambient category, defining construction, or essential contrast.

Reject when the match is incidental, generic, repeated after the target is already introduced, the wrong mathematical sense, or only part of a more specific compound.

Defer when the concept should be linked but the candidate span or target is not the best one. Record the preferred full phrase and target.

Prefer:

- `finite field extension` over a contained `finite field`;
- `group scheme` over bare `scheme` when a matching group-scheme knowl exists;
- `small étale site` or the full phrase `étale site` over bare `site`;
- one useful `sheaf` link over linking every occurrence in a short definition.

## Reason codes

Useful acceptance codes include `definition_dependency`, `definition_domain`, `hypothesis_dependency`, `core_characterization`, `core_example`, `essential_contrast`, and `structural_analogy`.

Useful rejection codes include `already_linked`, `too_generic`, `wrong_sense`, `ambiguous_target`, `partial_compound`, `incidental_mention`, `overlap_longer_phrase`, `link_density`, and `target_content_mismatch`.

## Required record

Retain candidate ID, source ID/path/hash, line and surface, possible targets, score/features, context, disposition, reason, reviewer, and timestamp. A changed source hash makes the decision stale and requires review again.

The historical experiments that motivated this split are preserved at `docs/archive/legacy-knowl-generation/`. They are noncanonical evidence; use them to design benchmarks, not as live instructions.

## Known recall limits

The scanner is deliberately lexical. Supplement it with an agent pass for:

- longer concepts that cross an existing link boundary, such as `algebraic [[...|field extension]]`;
- concepts expressed by non-title language, such as “Frobenius” naming a Frobenius endomorphism;
- theorem-level claims whose wording does not resemble the theorem title;
- ambiguous aliases that need setting and nearby mathematical context;
- corpus duplicates or near-duplicates that make target selection unstable.

Do not solve these cases by lowering the score until noise dominates. Add curated semantic aliases, context features, or explicit agent decisions with regression examples.
