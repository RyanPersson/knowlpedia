+++
id = "lie-groups/right-maurer-cartan-form"
title = "Right Maurer–Cartan form"
kind = "knowl"
summary = "The canonical g-valued 1-form on a Lie group obtained by translating tangent vectors to the identity on the right."
aliases = ["right-maurer-cartan-form", "Right Maurer–Cartan form"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/right-maurer-cartan-form.md"
+++

Let $G$ be a Lie group with Lie algebra $\mathfrak g=\mathrm{Lie}(G)$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]). The **right Maurer–Cartan form** is the $\mathfrak g$-valued 1-form $\theta^R\in\Omega^1(G;\mathfrak g)$ defined by
\[
\theta^R_g \;:=\; (dR_{g^{-1}})_g : T_gG \longrightarrow T_eG \cong \mathfrak g,
\]
where $R_{g^{-1}}$ is [[lie-groups/right-translation|right translation]] by $g^{-1}$.

Key properties:

- **Right invariance:** $(R_h)^*\theta^R=\theta^R$ for all $h\in G$, so $\theta^R$ is a canonical example of a [[lie-groups/right-invariant-differential-form|right-invariant form]].
- **Left equivariance:** under left translation, $\theta^R$ transforms by the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]]:
  \[
  (L_h)^*\theta^R = \mathrm{Ad}_h\circ \theta^R.
  \]
- **Maurer–Cartan equation (right form):**
  \[
  d\theta^R - \tfrac12[\theta^R,\theta^R]=0,
  \]
  where the bracket is induced from the [[fiber-bundles/lie-bracket|Lie bracket]] on $\mathfrak g$ (compare [[lie-groups/maurer-cartan-equation|Maurer–Cartan equation]] and the [[lie-groups/left-maurer-cartan-form|left Maurer–Cartan form]]).

If $X$ is a [[lie-groups/right-invariant-vector-field|right-invariant vector field]], then $\theta^R(X)$ is constant in $G$ and recovers the corresponding element of $\mathfrak g$. This is one way to see the tight relationship between invariant vector fields, [[lie-groups/one-parameter-subgroup|one-parameter subgroups]], and the [[lie-groups/exponential-map-lie-group|exponential map]].
