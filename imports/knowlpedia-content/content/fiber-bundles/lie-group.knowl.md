+++
id = "fiber-bundles/lie-group"
title = "Lie group"
kind = "knowl"
summary = "A group that is also a smooth manifold, with smooth multiplication and inversion."
aliases = ["lie-group", "Lie group"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/lie-group.md"
+++

A **Lie group** is a group $G$ equipped with the structure of a [[fiber-bundles/smooth-manifold|smooth manifold]] such that the group operations are [[fiber-bundles/smooth-map|smooth maps]]:
\[
\mu:G\times G\to G,\quad \mu(g,h)=gh,
\qquad
\iota:G\to G,\quad \iota(g)=g^{-1}.
\]
Equivalently, $G$ is a smooth manifold for which multiplication and inversion are smooth.

For each $g\in G$, the [[fiber-bundles/left-translation-l-g|left translation]] $L_g(h)=gh$ and the [[fiber-bundles/right-translation-r-g|right translation]] $R_g(h)=hg$ are [[fiber-bundles/diffeomorphism|diffeomorphisms]] of $G$, with inverses $L_{g^{-1}}$ and $R_{g^{-1}}$. The tangent space at the identity $T_eG$ carries a canonical Lie algebra structure, called the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of $G$]], and the [[fiber-bundles/exponential-map-lie-group-exponential|exponential map]] relates this infinitesimal structure to local group behavior near $e$.

Smooth group homomorphisms between Lie groups are [[lie-groups/lie-group-homomorphism|Lie group homomorphisms]].

## Examples

1. The additive group $(\mathbb{R}^n,+)$ is a Lie group with its standard smooth structure; multiplication is $x+y$ and inversion is $x\mapsto -x$.

2. The circle group $S^1=\{z\in\mathbb{C}:|z|=1\}$ is a $1$-dimensional Lie group under complex multiplication.

3. The general linear group $GL(n,\mathbb{R})$ of invertible $n\times n$ real matrices is an open submanifold of $\mathbb{R}^{n^2}$ and is a Lie group under matrix multiplication.
