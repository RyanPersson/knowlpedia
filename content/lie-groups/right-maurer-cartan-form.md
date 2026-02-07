---
title: "Right Maurer–Cartan form"
description: "The canonical g-valued 1-form on a Lie group obtained by translating tangent vectors to the identity on the right."
---

Let $G$ be a Lie group with Lie algebra $\mathfrak g=\mathrm{Lie}(G)$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}). The **right Maurer–Cartan form** is the $\mathfrak g$-valued 1-form $\theta^R\in\Omega^1(G;\mathfrak g)$ defined by
\[
\theta^R_g \;:=\; (dR_{g^{-1}})_g : T_gG \longrightarrow T_eG \cong \mathfrak g,
\]
where $R_{g^{-1}}$ is {{< knowl id="right-translation" text="right translation" >}} by $g^{-1}$.

Key properties:

- **Right invariance:** $(R_h)^*\theta^R=\theta^R$ for all $h\in G$, so $\theta^R$ is a canonical example of a {{< knowl id="right-invariant-differential-form" text="right-invariant form" >}}.
- **Left equivariance:** under left translation, $\theta^R$ transforms by the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint action" >}}:
  \[
  (L_h)^*\theta^R = \mathrm{Ad}_h\circ \theta^R.
  \]
- **Maurer–Cartan equation (right form):**
  \[
  d\theta^R - \tfrac12[\theta^R,\theta^R]=0,
  \]
  where the bracket is induced from the {{< knowl id="lie-bracket" text="Lie bracket" section="fiber-bundles">}} on $\mathfrak g$ (compare {{< knowl id="maurer-cartan-equation" text="Maurer–Cartan equation" >}} and the {{< knowl id="left-maurer-cartan-form" text="left Maurer–Cartan form" >}}).

If $X$ is a {{< knowl id="right-invariant-vector-field" text="right-invariant vector field" >}}, then $\theta^R(X)$ is constant in $G$ and recovers the corresponding element of $\mathfrak g$. This is one way to see the tight relationship between invariant vector fields, {{< knowl id="one-parameter-subgroup" text="one-parameter subgroups" >}}, and the {{< knowl id="exponential-map-lie-group" text="exponential map" >}}.
