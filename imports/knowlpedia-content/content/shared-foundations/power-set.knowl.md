+++
id = "shared-foundations/power-set"
title = "Power set"
kind = "knowl"
summary = "The set of all subsets of a given set."
aliases = ["power-set", "Power set"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/power-set.md"
+++

A **power set** of a set $A$ is the set
$$
\mathcal{P}(A)=\{B : B\subseteq A\}.
$$

Thus $\mathcal{P}(A)$ collects all [[shared-foundations/subset|subsets]] of $A$ into a single [[shared-foundations/set|set]]. Power sets are central when forming collections of sets, such as families indexed by an index set.

**Examples:**
- If $A=\varnothing$, then $\mathcal{P}(A)=\{\varnothing\}$.
- If $A=\{1,2\}$, then $\mathcal{P}(A)=\{\varnothing,\{1\},\{2\},\{1,2\}\}$.
