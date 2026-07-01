+++
id = "topology/quotient-topology"
title = "Quotient topology"
kind = "knowl"
summary = "The finest topology on a codomain that makes a given surjection continuous."
aliases = ["quotient-topology", "Quotient topology"]
domains = ["topology"]
legacy_source_path = "topology/quotient-topology.md"
+++

The **quotient topology** on a set $Y$ induced by a [[shared-foundations/surjective-function|surjective function]] $q:X\to Y$ from a [[topology/topological-space|topological space]] $X$ is defined by declaring a subset $U\subseteq Y$ to be [[topology/open-set|open]] if and only if $q^{-1}(U)$ is open in $X$.

With this topology, the map $q$ is automatically [[topology/continuous-map|continuous]], and the quotient topology is the finest topology on $Y$ for which this is true. A common special case is when $Y$ is the [[shared-foundations/quotient-set|quotient set]] $X/\!\sim$ for an [[shared-foundations/equivalence-relation|equivalence relation]] $\sim$ on $X$, with $q$ the canonical projection.

**Examples:**
- Let $X=[0,1]$ (as a subspace of $\mathbb{R}$) and identify $0$ and $1$; the resulting quotient space carries the quotient topology and models a circle.
- If $A\subseteq X$ is collapsed to a single point by a surjection $q:X\to Y$, then $Y$ has the quotient topology determined by this identification map.
- If $q:X\to Y$ is a bijection, the quotient topology on $Y$ agrees with the topology transported by $q$, and $q$ is a [[topology/homeomorphism|homeomorphism]] exactly when $q^{-1}$ is also continuous.
