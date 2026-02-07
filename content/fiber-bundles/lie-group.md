---
title: "Lie group"
description: "A group that is also a smooth manifold, with smooth multiplication and inversion."
---

A **Lie group** is a group $G$ equipped with the structure of a {{< knowl id="smooth-manifold" text="smooth manifold" >}} such that the group operations are {{< knowl id="smooth-map" text="smooth maps" >}}:
\[
\mu:G\times G\to G,\quad \mu(g,h)=gh,
\qquad
\iota:G\to G,\quad \iota(g)=g^{-1}.
\]
Equivalently, $G$ is a smooth manifold for which multiplication and inversion are smooth.

For each $g\in G$, the {{< knowl id="left-translation-l-g" text="left translation" >}} $L_g(h)=gh$ and the {{< knowl id="right-translation-r-g" text="right translation" >}} $R_g(h)=hg$ are {{< knowl id="diffeomorphism" text="diffeomorphisms" >}} of $G$, with inverses $L_{g^{-1}}$ and $R_{g^{-1}}$. The tangent space at the identity $T_eG$ carries a canonical Lie algebra structure, called the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of $G$" section="lie-groups">}}, and the {{< knowl id="exponential-map-lie-group-exponential" text="exponential map" >}} relates this infinitesimal structure to local group behavior near $e$.

Smooth group homomorphisms between Lie groups are {{< knowl id="lie-group-homomorphism" text="Lie group homomorphisms" section="lie-groups">}}.

## Examples

1. The additive group $(\mathbb{R}^n,+)$ is a Lie group with its standard smooth structure; multiplication is $x+y$ and inversion is $x\mapsto -x$.

2. The circle group $S^1=\{z\in\mathbb{C}:|z|=1\}$ is a $1$-dimensional Lie group under complex multiplication.

3. The general linear group $GL(n,\mathbb{R})$ of invertible $n\times n$ real matrices is an open submanifold of $\mathbb{R}^{n^2}$ and is a Lie group under matrix multiplication.
