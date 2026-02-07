---
title: "Closed subgroup theorem"
description: "A closed subgroup of a Lie group is an embedded Lie subgroup, and the quotient G/H is a smooth manifold."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} and let $H\le G$ be a {{< knowl id="closed-subgroup-lie-group" text="closed subgroup" >}}.

**Theorem (Closed Subgroup Theorem).**
1. There is a unique smooth manifold structure on $H$ making it a Lie group such that the inclusion $\iota:H\hookrightarrow G$ is a smooth injective immersion and a homeomorphism onto its image. In particular, $H$ is an embedded {{< knowl id="lie-subgroup" text="Lie subgroup" >}} of $G$.
2. The Lie algebra of $H$ is the subalgebra
   $$
   \mathrm{Lie}(H)=\{X\in \mathfrak{g} : \exp(tX)\in H \text{ for all } t\in \mathbb{R}\},
   $$
   matching the description in {{< knowl id="lie-algebra-of-subgroup-lemma" text="the Lie algebra of a subgroup lemma" >}}.
3. The {{< knowl id="coset-space" text="coset space" >}} $G/H$ admits a unique smooth manifold structure such that the projection $\pi:G\to G/H$ is a smooth submersion, making $G/H$ into a basic example of a {{< knowl id="homogeneous-space" text="homogeneous space" >}}.

**Context.** This theorem is the bridge between “topological subgroup” and “geometric submanifold.” It is also what makes quotients by closed normal subgroups into Lie groups (compare {{< knowl id="quotient-lie-group" text="quotient Lie groups" >}}).
