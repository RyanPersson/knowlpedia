---
title: "Pullback of differential forms"
description: "Given a smooth map, pull back a k-form by applying the differential to each argument."
---

Let $F:M\to N$ be a {{< knowl id="smooth-map" text="smooth map" >}} between {{< knowl id="smooth-manifold" text="smooth manifolds" >}}.

A {{< knowl id="differential-k-form" text="differential $k$-form" >}} on $N$ assigns to each point $q\in N$ an alternating $k$-linear map on $T_qN$. The {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential" >}} $dF_p:T_pM\to T_{F(p)}N$ transports tangent vectors, and the pullback transports covariant objects in the opposite direction.

**Definition (pullback of a $k$-form).** If $\omega$ is a $k$-form on $N$, the **pullback** $F^*\omega$ is the $k$-form on $M$ defined by
\[
(F^*\omega)_p(v_1,\dots,v_k)
:=\omega_{F(p)}\bigl(dF_p(v_1),\dots,dF_p(v_k)\bigr),
\]
for $p\in M$ and $v_1,\dots,v_k\in T_pM$.

For $k=1$ this agrees with the {{< knowl id="pullback-of-covectors" text="pullback of covectors" >}}.

**Key properties.**
- **Functoriality:** for smooth maps $M\xrightarrow{F}N\xrightarrow{G}P$ one has $(G\circ F)^* = F^*\circ G^*$.
- **Compatibility with wedge:** for forms $\alpha,\beta$ on $N$,
  \[
  F^*(\alpha\wedge \beta)=F^*\alpha\wedge F^*\beta,
  \]
  using the {{< knowl id="wedge-product-of-differential-forms" text="wedge product" >}}.
- **Compatibility with exterior derivative:** for any form $\omega$ on $N$,
  \[
  F^*(d\omega)=d(F^*\omega),
  \]
  where $d$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}}.
  In particular, pullback preserves being {{< knowl id="closed-differential-form" text="closed" >}} and being {{< knowl id="exact-differential-form" text="exact" >}}, and therefore induces maps on {{< knowl id="de-rham-cohomology-group" text="de Rham cohomology" >}}.

If $F$ is a {{< knowl id="diffeomorphism" text="diffeomorphism" >}}, then $F^*$ is an isomorphism on forms with inverse $(F^{-1})^*$. If $i:Z\hookrightarrow N$ is a {{< knowl id="smooth-embedding" text="smooth embedding" >}}, then $i^*\omega$ is the restriction of $\omega$ to tangent vectors along $Z$.

### Examples

1. **Polar coordinates and the area form.** Let $\Phi:(0,\infty)\times (0,2\pi)\to \mathbb{R}^2\setminus\{0\}$ be $\Phi(r,\theta)=(r\cos\theta,r\sin\theta)$. For the standard $2$-form $dx\wedge dy$ on $\mathbb{R}^2$, one computes
   \[
   \Phi^*(dx\wedge dy)= r\,dr\wedge d\theta.
   \]
   This is the differential-form version of the Jacobian factor in change of variables.

2. **Pullback along an inclusion can kill high-degree forms.** Let $i:S^1\hookrightarrow\mathbb{R}^2$ be the inclusion. Since $S^1$ is $1$-dimensional, any $2$-form on $\mathbb{R}^2$ pulls back to $0$ on $S^1$. In particular,
   \[
   i^*(dx\wedge dy)=0.
   \]

3. **Projection from a product.** Let $\pi_1:M\times N\to M$ be the projection. For any $k$-form $\omega$ on $M$, the pullback $\pi_1^*\omega$ is the $k$-form on $M\times N$ that ignores tangent directions in the $N$-factor and evaluates $\omega$ on the $M$-components.
