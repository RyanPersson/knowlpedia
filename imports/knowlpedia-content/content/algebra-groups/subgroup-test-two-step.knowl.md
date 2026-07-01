+++
id = "algebra-groups/subgroup-test-two-step"
title = "Subgroup Test (two-step)"
kind = "knowl"
summary = "A nonempty subset of a group is a subgroup iff it is closed under products and inverses"
aliases = ["subgroup-test-two-step", "Subgroup Test (two-step)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/subgroup-test-two-step.md"
+++

**Subgroup Test (two-step)**: Let $G$ be a [[algebra-groups/group|group]] and let $H$ be a nonempty [[shared-foundations/subset|subset]] of $G$. Then $H$ is a [[algebra-groups/subgroup|subgroup]] of $G$ if and only if:

1. for all $x,y\in H$ one has $xy\in H$ (closure under the group operation), and
2. for all $x\in H$ one has $x^{-1}\in H$ (closure under inverses).

This criterion is equivalent to the [[algebra-groups/subgroup-test-one-step|one-step subgroup test]]; use whichever closure condition is easier to verify in a given situation.
