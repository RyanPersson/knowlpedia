+++
id = "algebra-groups/normal-subgroup"
title = "Normal Subgroup"
kind = "knowl"
summary = "A subgroup invariant under conjugation"
aliases = ["normal-subgroup", "Normal Subgroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/normal-subgroup.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $H\le G$ be a [[algebra-groups/subgroup|subgroup]]. The subgroup $H$ is **normal** in $G$ (written $H\trianglelefteq G$) if for every $g\in G$,
$
gHg^{-1} = H.
$

Normality says that $H$ is stable under the [[algebra-groups/conjugation-action|conjugation action]] of $G$ on itself. Equivalently, $H$ is normal iff every left [[algebra-groups/coset|coset]] of $H$ equals the corresponding right coset, and this is exactly the hypothesis needed to form the [[algebra-groups/quotient-group|quotient group]] $G/H$.

**Examples:**
- The [[algebra-groups/center-of-group|center]] $Z(G)$ is normal in $G$.
- $A_n$ is normal in $S_n$ for all $n\ge 2$.
- Any subgroup of index $2$ is normal (see [[algebra-groups/index-2-normal|subgroup of index 2 is normal]]).
- *(Non-example)* In $S_3$, the subgroup $\{e,(12)\}$ is not normal.
