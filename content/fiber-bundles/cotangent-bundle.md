---
title: "Cotangent bundle"
description: "The smooth vector bundle whose fiber at each point is the dual of the tangent space."
---

Let $M$ be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} of dimension $n$. For each $p\in M$, the {{< knowl id="tangent-space-at-a-point" text="tangent space" >}} $T_pM$ is a real vector space, and its dual space
\[
T_p^*M := (T_pM)^*
\]
is the **cotangent space** at $p$.

**Definition (cotangent bundle).** The **cotangent bundle** of $M$ is the disjoint union
\[
T^*M := \bigsqcup_{p\in M} T_p^*M,
\]
together with the projection map $\pi:T^*M\to M$ sending a covector $\alpha\in T_p^*M$ to its base point $p$.

**Smooth structure / vector bundle structure.** The set $T^*M$ carries a canonical smooth manifold structure of dimension $2n$ such that:

1. $\pi:T^*M\to M$ is a smooth map, and each fiber $\pi^{-1}(p)=T_p^*M$ is a vector space of dimension $n$.
2. For every {{< knowl id="smooth-chart-coordinate-chart" text="smooth chart" >}} $(U,x)$ on $M$, with coordinates $x=(x^1,\dots,x^n)$, there is a smooth trivialization
   \[
   \Phi_U:\pi^{-1}(U)\to U\times \mathbb{R}^n
   \]
   defined as follows: each $\alpha\in T_p^*M$ (with $p\in U$) can be written uniquely as
   \[
   \alpha=\sum_{i=1}^n a_i\, (dx^i)_p,
   \]
   and then $\Phi_U(\alpha)=(p,(a_1,\dots,a_n))$.
3. On overlaps $U\cap V$, the induced transition functions are smooth and linear in the fiber variables, so $\pi:T^*M\to M$ is a smooth vector bundle of rank $n$ (the dual bundle of the {{< knowl id="tangent-bundle" text="tangent bundle" >}}).

Smooth sections of $T^*M$ are exactly differential $1$-forms, i.e. the case $k=1$ of a {{< knowl id="differential-k-form" text="differential $k$-form" >}}.

### Examples

1. **Euclidean space.** For $M=\mathbb{R}^n$ with standard coordinates, each $T_p\mathbb{R}^n\cong \mathbb{R}^n$ canonically, hence $T_p^*\mathbb{R}^n\cong (\mathbb{R}^n)^*$. Using the standard basis $dx^1,\dots,dx^n$, one gets a global trivialization
   \[
   T^*\mathbb{R}^n \cong \mathbb{R}^n\times (\mathbb{R}^n)^* \cong \mathbb{R}^{2n}.
   \]

2. **The circle.** For $M=S^1$, the cotangent bundle is a rank-$1$ vector bundle and is trivial:
   \[
   T^*S^1 \cong S^1\times \mathbb{R}.
   \]
   Concretely, in the angle coordinate $\theta$, every covector at $p\in S^1$ is of the form $a\, d\theta|_p$ for a unique $a\in\mathbb{R}$.

3. **Lie groups.** If $G$ is a {{< knowl id="lie-group" text="Lie group" >}}, then for each $g\in G$, {{< knowl id="left-translation-l-g" text="left translation" >}} $L_g:G\to G$ identifies $T_eG$ with $T_gG$. Dualizing, $T_g^*G$ is identified with $T_e^*G\cong \mathfrak{g}^*$ where $\mathfrak{g}$ is the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of $G$" section="lie-groups">}}. This yields a (non-canonical but natural) trivialization $T^*G\cong G\times \mathfrak{g}^*$.
