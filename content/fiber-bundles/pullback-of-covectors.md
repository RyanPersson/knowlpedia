---
title: "Pullback of covectors"
description: "The contravariant map on cotangent spaces induced by a smooth map, defined by precomposing with the differential."
---

Let $F:M\to N$ be a {{< knowl id="smooth-map" text="smooth map" >}} between {{< knowl id="smooth-manifold" text="smooth manifolds" >}}. For each $p\in M$, the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential" >}} gives a linear map
\[
dF_p:T_pM\to T_{F(p)}N
\]
between {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}}.

**Definition (pullback on a single fiber).** The **pullback of covectors** at $p$ is the linear map
\[
F_p^*:T_{F(p)}^*N \to T_p^*M
\]
defined by
\[
(F_p^*\alpha)(v):=\alpha\bigl(dF_p(v)\bigr)
\quad\text{for }\alpha\in T_{F(p)}^*N,\; v\in T_pM.
\]
Thus $F_p^*$ is the dual map of $dF_p$ (it is contravariant: it goes in the opposite direction).

This construction is fiberwise for the {{< knowl id="cotangent-bundle" text="cotangent bundle" >}}: a covector at $F(p)$ pulls back to a covector at $p$.

**Functoriality.** If $G:N\to P$ is another smooth map, then for each $p\in M$,
\[
(G\circ F)_p^* = F_p^*\circ G_{F(p)}^*.
\]
If $F$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}, then $dF_p$ is an isomorphism and $F_p^*$ is an isomorphism with inverse given by the corresponding pullback along $F^{-1}$.

Pullback of covectors is the $k=1$ case of the {{< knowl id="pullback-of-differential-forms" text="pullback of differential forms" >}}.

### Examples

1. **Pulling back the standard covectors on $\mathbb{R}^2$.** Let $F:\mathbb{R}^2\to\mathbb{R}^2$ be given by $F(u,v)=(u^2,uv)$, and let $(x,y)$ be coordinates on the target. Then, viewing $dx$ and $dy$ as smooth covector fields,
   \[
   F^*(dx)=d(u^2)=2u\,du,\qquad F^*(dy)=d(uv)=v\,du+u\,dv.
   \]
   At a specific point $(u,v)$, this matches the fiberwise definition $\alpha\mapsto \alpha\circ dF_{(u,v)}$.

2. **Inclusion of the circle.** Let $i:S^1\hookrightarrow\mathbb{R}^2$ be the inclusion and parametrize $S^1$ by $\gamma(\theta)=(\cos\theta,\sin\theta)$. Then
   \[
   i^*(dx) = -\sin\theta\,d\theta,\qquad i^*(dy)=\cos\theta\,d\theta,
   \]
   since $x\circ\gamma=\cos\theta$ and $y\circ\gamma=\sin\theta$.

3. **Constant map.** If $c:M\to N$ is constant with value $q\in N$, then $dc_p=0$ for every $p$, hence $c_p^*(\alpha)=0$ for every $\alpha\in T_q^*N$.
