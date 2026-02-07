---
title: "Lie subalgebra"
description: "A linear subspace closed under the Lie bracket."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}} over $\Bbbk$ with bracket $[\ ,\ ]$.

A **Lie subalgebra** of $\mathfrak g$ is a $\Bbbk$-linear subspace $\mathfrak h\subseteq \mathfrak g$ such that
$$
[\mathfrak h,\mathfrak h]\subseteq \mathfrak h,
$$

i.e. $[X,Y]\in \mathfrak h$ for all $X,Y\in \mathfrak h$.

With the restricted bracket, $\mathfrak h$ is itself a Lie algebra, and the inclusion $\mathfrak h\hookrightarrow \mathfrak g$ is a {{< knowl id="lie-algebra-homomorphism" text="Lie algebra homomorphism" >}}.

## Context and examples
- If $H\subseteq G$ is a {{< knowl id="lie-subgroup" text="Lie subgroup" >}} of a Lie group, then $\operatorname{Lie}(H)\subseteq \operatorname{Lie}(G)$ is a Lie subalgebra (see {{< knowl id="lie-algebra-of-subgroup-lemma" text="the Lie algebra of a subgroup lemma" >}}).
- An {{< knowl id="ideal-lie-algebra" text="ideal" >}} is a Lie subalgebra $\mathfrak h$ satisfying $[\mathfrak g,\mathfrak h]\subseteq \mathfrak h$; ideals are exactly kernels of Lie algebra homomorphisms and allow formation of {{< knowl id="quotient-lie-algebra" text="quotient Lie algebras" >}}.
