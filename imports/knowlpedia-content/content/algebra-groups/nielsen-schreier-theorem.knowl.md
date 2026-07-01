+++
id = "algebra-groups/nielsen-schreier-theorem"
title = "Nielsen–Schreier Theorem"
kind = "knowl"
summary = "Every subgroup of a free group is free (with a rank formula in finite index)"
aliases = ["nielsen-schreier-theorem", "Nielsen–Schreier Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/nielsen-schreier-theorem.md"
+++

**Nielsen–Schreier Theorem.**
Let $F$ be a [[algebra-groups/free-group|free group]] and let $H \le F$ be a [[algebra-groups/subgroup|subgroup]]. Then $H$ is a free group.

If $F$ has finite rank $n$ and the [[algebra-groups/index-of-subgroup|index]] $[F:H]$ is finite, then $H$ has finite rank and satisfies the Schreier index formula
$$
\operatorname{rank}(H) = 1 + [F:H]\,(n-1).
$$

This theorem is proved by constructing an explicit free generating set for $H$ from a transversal of cosets; [[algebra-groups/schreiers-lemma|Schreier's lemma]] provides the standard generating set used in the proof. It is a foundational result in combinatorial group theory.
