+++
id = "lie-groups/homogeneous-space"
title = "Homogeneous space"
kind = "knowl"
summary = "A manifold with a transitive Lie group action; equivalently a quotient G/H by a stabilizer."
aliases = ["homogeneous-space", "Homogeneous space"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/homogeneous-space.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] acting smoothly on a manifold $M$ (see [[lie-groups/smooth-action-lie-group|smooth action]]).

**Definition (Homogeneous space).**
$M$ is a **homogeneous space** for $G$ if the action is [[lie-groups/transitive-action-lie|transitive]], i.e. for any $p,q\in M$ there exists $g\in G$ with $g\cdot p=q$.

Fix $p\in M$ and let $H=G_p$ be its [[lie-groups/stabilizer-lie-group|stabilizer]]. Then the orbit map $G\to M$, $g\mapsto g\cdot p$, induces a bijection
\[
G/H \;\longrightarrow\; M,
\]
where $G/H$ is the [[lie-groups/coset-space|coset space]]. If $H$ is a [[lie-groups/closed-subgroup-lie-group|closed]] subgroup, then $G/H$ carries a unique smooth manifold structure making the induced map a $G$-equivariant diffeomorphism (compare the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]).

**Special case.**
If the action is also [[lie-groups/free-action-lie|free]], then $H$ is trivial and $M$ is (noncanonically) identified with $G$; in the free-and-transitive case, $M$ is a [[lie-groups/principal-homogeneous-space|principal homogeneous space]].

**Context.**
Homogeneous spaces provide the basic examples of manifolds built from Lie groups (spheres, Grassmannians, flag varieties), and their geometry is controlled by the subgroup $H$ and the induced action on tangent spaces.
