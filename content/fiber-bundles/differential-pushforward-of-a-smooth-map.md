---
title: "Differential (pushforward) of a smooth map"
description: "The linear map on tangent spaces induced by a smooth map, satisfying the chain rule."
---

Let $M,N$ be {{< knowl id="smooth-manifold" text="smooth manifolds" >}} and let $F:M\to N$ be a {{< knowl id="smooth-map" text="smooth map" >}}.

**Definition (differential at a point).** For each $p\in M$, the **differential** (or **pushforward**) of $F$ at $p$ is the linear map
\[
dF_p: T_pM \to T_{F(p)}N
\]
between {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}} defined as follows (using the derivation model of tangent vectors): if $v\in T_pM$ is a derivation at $p$, then $dF_p(v)\in T_{F(p)}N$ is the derivation given by
\[
(dF_p(v))(g) := v(g\circ F)
\]
for every smooth function $g$ defined near $F(p)$.

Equivalently, if $v$ is represented by the velocity of a smooth curve $\gamma:(-\epsilon,\epsilon)\to M$ with $\gamma(0)=p$, then $dF_p(v)$ is represented by the velocity of $F\circ\gamma$ at $0$.

**Bundle map form.** The assignments $p\mapsto dF_p$ assemble into a smooth map between total spaces of tangent bundles,
\[
dF: TM \to TN,
\]
covering $F$ (meaning $\pi_N\circ dF = F\circ \pi_M$, where $\pi_M:TM\to M$ and $\pi_N:TN\to N$ are the bundle projections). This viewpoint uses the {{< knowl id="tangent-bundle" text="tangent bundle" >}} functorially.

**Chain rule.** If $G:N\to P$ is another smooth map, then for every $p\in M$,
\[
d(G\circ F)_p = dG_{F(p)}\circ dF_p.
\]

The differential detects local rank properties: $F$ is a {{< knowl id="smooth-immersion" text="smooth immersion" >}} iff $dF_p$ is injective for all $p$, and a {{< knowl id="smooth-submersion" text="smooth submersion" >}} iff $dF_p$ is surjective for all $p$. In particular, the notion of {{< knowl id="regular-value" text="regular value" >}} is expressed in terms of surjectivity of $dF_p$ along a {{< knowl id="fiber-of-a-map-preimage-fiber" text="fiber" >}}.

### Examples

1. **A map $\mathbb{R}^2\to\mathbb{R}^2$.** Let $F(x,y)=(x^2,y^2)$. Then in standard coordinates,
   \[
   dF_{(x,y)}(u,v) = (2x\,u,\;2y\,v).
   \]
   At $(1,1)$ the map has rank $2$, while at $(0,1)$ it has rank $1$, and at $(0,0)$ it has rank $0$.

2. **Projection is a submersion.** Let $\pi:\mathbb{R}^2\to\mathbb{R}$ be $\pi(x,y)=x$. Then
   \[
   d\pi_{(x,y)}(u,v)=u,
   \]
   which is surjective for every $(x,y)$. Thus $\pi$ is a {{< knowl id="smooth-submersion" text="smooth submersion" >}}, and its fibers are vertical lines.

3. **Inclusion is an immersion.** Let $i:S^1\hookrightarrow \mathbb{R}^2$ be the standard inclusion. For each $p\in S^1$, the map $di_p:T_pS^1\to T_p\mathbb{R}^2$ is injective, so $i$ is a {{< knowl id="smooth-immersion" text="smooth immersion" >}} (in fact a {{< knowl id="smooth-embedding" text="smooth embedding" >}}).
