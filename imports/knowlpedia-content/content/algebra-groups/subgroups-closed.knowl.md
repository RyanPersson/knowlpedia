+++
id = "algebra-groups/subgroups-closed"
title = "Subgroups are closed under inverses and products"
kind = "knowl"
summary = "A subgroup contains the identity and is closed under multiplication and inversion"
aliases = ["subgroups-closed", "Subgroups are closed under inverses and products"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/subgroups-closed.md"
+++

**Proposition (Closure properties of subgroups).**
Let $H$ be a [[algebra-groups/subgroup|subgroup]] of a [[algebra-groups/group|group]] $G$. Then:

1. The identity element $e$ of $G$ lies in $H$.
2. If $h\in H$, then $h^{-1}\in H$.
3. If $h_1,h_2\in H$, then $h_1h_2\in H$.
4. Consequently, if $h_1,h_2\in H$, then $h_1h_2^{-1}\in H$.

**Context.**
The reverse implication (a nonempty subset closed under $h_1h_2^{-1}$ is a subgroup) is packaged as a [[algebra-groups/subgroup-test-one-step|subgroup test]], so this proposition is the "easy direction" used constantly in computations.
