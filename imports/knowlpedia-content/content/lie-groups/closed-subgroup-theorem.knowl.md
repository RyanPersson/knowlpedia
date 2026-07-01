+++
id = "lie-groups/closed-subgroup-theorem"
title = "Closed subgroup theorem"
kind = "knowl"
summary = "A closed subgroup of a Lie group is an embedded Lie subgroup, and the quotient G/H is a smooth manifold."
aliases = ["closed-subgroup-theorem", "Closed subgroup theorem"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/closed-subgroup-theorem.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] and let $H\le G$ be a [[lie-groups/closed-subgroup-lie-group|closed subgroup]].

**Theorem (Closed Subgroup Theorem).**
1. There is a unique smooth manifold structure on $H$ making it a Lie group such that the inclusion $\iota:H\hookrightarrow G$ is a smooth injective immersion and a homeomorphism onto its image. In particular, $H$ is an embedded [[lie-groups/lie-subgroup|Lie subgroup]] of $G$.
2. The Lie algebra of $H$ is the subalgebra
   $$
   \mathrm{Lie}(H)=\{X\in \mathfrak{g} : \exp(tX)\in H \text{ for all } t\in \mathbb{R}\},
   $$
   matching the description in [[lie-groups/lie-algebra-of-subgroup-lemma|the Lie algebra of a subgroup lemma]].
3. The [[lie-groups/coset-space|coset space]] $G/H$ admits a unique smooth manifold structure such that the projection $\pi:G\to G/H$ is a smooth submersion, making $G/H$ into a basic example of a [[lie-groups/homogeneous-space|homogeneous space]].

**Context.** This theorem is the bridge between “topological subgroup” and “geometric submanifold.” It is also what makes quotients by closed normal subgroups into Lie groups (compare [[lie-groups/quotient-lie-group|quotient Lie groups]]).
