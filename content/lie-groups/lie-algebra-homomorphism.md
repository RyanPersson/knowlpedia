---
title: "Lie algebra homomorphism"
description: "A linear map between Lie algebras that preserves the Lie bracket."
---

Let $\mathfrak g,\mathfrak h$ be {{< knowl id="lie-algebra" text="Lie algebras" >}} over a field $\Bbbk$ (typically $\Bbb R$ or $\Bbb C$), with {{< knowl id="lie-bracket" text="Lie brackets" section="fiber-bundles">}} $[\ ,\ ]_{\mathfrak g}$ and $[\ ,\ ]_{\mathfrak h}$.

A **Lie algebra homomorphism** is a $\Bbbk$-linear map $\varphi:\mathfrak g\to\mathfrak h$ such that for all $X,Y\in\mathfrak g$,
$$
\varphi([X,Y]_{\mathfrak g})=[\varphi(X),\varphi(Y)]_{\mathfrak h}.
$$

Equivalently, $\varphi$ is a morphism in the category of Lie algebras: it intertwines the brackets.

## Basic consequences
- The kernel $\ker(\varphi)$ is an {{< knowl id="ideal-lie-algebra" text="ideal" >}} in $\mathfrak g$.
- The image $\operatorname{im}(\varphi)$ is a {{< knowl id="lie-subalgebra" text="Lie subalgebra" >}} of $\mathfrak h$.
- There is an induced injective homomorphism $\overline\varphi:\mathfrak g/\ker(\varphi)\to \operatorname{im}(\varphi)$, giving an isomorphism of Lie algebras
  $$
  \mathfrak g/\ker(\varphi)\cong \operatorname{im}(\varphi)
  $$
  (an instance of the first isomorphism theorem, formulated using {{< knowl id="quotient-lie-algebra" text="quotients of Lie algebras" >}}).

## Context
If $f:G\to H$ is a {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}, then its differential at the identity,
$df_e:\operatorname{Lie}(G)\to \operatorname{Lie}(H)$, is a Lie algebra homomorphism (see {{< knowl id="differential-is-lie-algebra-homomorphism" text="the differential–bracket compatibility" >}}). This is the bridge between global group structure and infinitesimal algebra structure.
