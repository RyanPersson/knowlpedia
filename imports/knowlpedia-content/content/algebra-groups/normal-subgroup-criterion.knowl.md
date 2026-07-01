+++
id = "algebra-groups/normal-subgroup-criterion"
title = "Normal Subgroup Criterion"
kind = "knowl"
summary = "A subgroup is normal iff it is stable under conjugation by every group element"
aliases = ["normal-subgroup-criterion", "Normal Subgroup Criterion"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/normal-subgroup-criterion.md"
+++

**Normal Subgroup Criterion**: Let $G$ be a [[algebra-groups/group|group]] and let $N\le G$ be a [[algebra-groups/subgroup|subgroup]]. Then $N$ is a [[algebra-groups/normal-subgroup|normal]] subgroup of $G$ if and only if for every $g\in G$ and every $n\in N$ one has $gng^{-1}\in N$.

Equivalently, $N$ is normal if and only if $gNg^{-1}=N$ for all $g\in G$ (where $gNg^{-1}=\{gng^{-1}:n\in N\}$). This says precisely that $N$ is invariant under the [[algebra-groups/conjugation-action|conjugation action]] of $G$ on itself.
