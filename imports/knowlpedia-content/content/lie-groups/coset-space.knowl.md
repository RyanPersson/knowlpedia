+++
id = "lie-groups/coset-space"
title = "Coset space"
kind = "knowl"
summary = "The quotient space of left cosets, a smooth manifold when is a closed Lie subgroup."
aliases = ["coset-space", "Coset space"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/coset-space.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] and let $H\le G$ be a subgroup.

The **left coset space** $G/H$ is the set of left cosets
\[
G/H := \{gH : g\in G\},
\]
equipped with the quotient topology for the projection $\pi:G\to G/H$, $\pi(g)=gH$.

If $H$ is a **closed** [[lie-groups/lie-subgroup|Lie subgroup]] (equivalently, a closed subgroup that is automatically an embedded Lie subgroup by the [[lie-groups/closed-subgroup-theorem|Closed Subgroup Theorem]]), then $G/H$ carries a canonical smooth manifold structure characterized by:

- $\pi:G\to G/H$ is a smooth surjective submersion;
- the left action of $G$ on $G/H$ given by $g'\cdot (gH)=(g'g)H$ is a smooth [[lie-groups/smooth-action-lie-group|Lie group action]].

In this case, $G/H$ is a basic example of a [[lie-groups/homogeneous-space|homogeneous space]]: the action is transitive and the stabilizer of the basepoint $eH$ is exactly $H$ (compare [[lie-groups/stabilizer-lie-group|stabilizer]] and [[lie-groups/transitive-action-lie|transitive action]]).

## Tangent space identification
Let $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak h=\mathrm{Lie}(H)$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]). Then
\[
T_{eH}(G/H)\;\cong\;\mathfrak g/\mathfrak h,
\]
canonically, via the differential $d\pi_e:\mathfrak g\to T_{eH}(G/H)$ whose kernel is $\mathfrak h$.

**Context.** Many geometric objects (spheres, Grassmannians, flag varieties) arise naturally as $G/H$; understanding $G/H$ is often the first step in studying invariant tensors such as [[lie-groups/left-invariant-differential-form|left-invariant forms]] or [[lie-groups/bi-invariant-metric|bi-invariant metrics]] on $G$ and their descendants on $G/H$.
