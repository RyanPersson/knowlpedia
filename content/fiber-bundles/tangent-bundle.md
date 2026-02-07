---
title: "Tangent bundle"
description: "The smooth vector bundle whose fiber at p is the tangent space T_pM."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} of dimension \(n\).

The **tangent bundle** of \(M\) is the set
\[
TM = \bigsqcup_{p\in M} T_pM,
\]
the disjoint union of all {{< knowl id="tangent-space-at-a-point" text="tangent spaces" >}} of \(M\), equipped with the projection map
\[
\pi: TM \to M,\qquad \pi(v)=p \ \text{for } v\in T_pM.
\]

There is a canonical smooth manifold structure on \(TM\) characterized as follows: for any {{< knowl id="smooth-chart-coordinate-chart" text="chart" >}} \((U,\varphi)\) on \(M\) with \(\varphi:U\to \mathbb{R}^n\), the induced map
\[
\pi^{-1}(U) \longrightarrow \varphi(U)\times \mathbb{R}^n
\]
sending a tangent vector \(v\in T_pM\) to \((\varphi(p), (v^1,\dots,v^n))\) in the coordinate basis \(\left.\frac{\partial}{\partial x^i}\right|_p\) is a diffeomorphism onto an open subset of \(\mathbb{R}^{2n}\). These charts are compatible across a {{< knowl id="smooth-atlas" text="smooth atlas" >}} and make \(\pi:TM\to M\) into a smooth map.

With this structure, \(TM\) is a rank-\(n\) vector bundle over \(M\): each fiber \(\pi^{-1}(p)=T_pM\) is a vector space, and the local identifications above give smooth local trivializations.

## Sections and vector fields
A smooth section of \(\pi:TM\to M\) is the same thing as a {{< knowl id="vector-field" text="vector field" >}} on \(M\): it assigns to each \(p\in M\) a tangent vector \(X(p)\in T_pM\) smoothly in \(p\).

## Functoriality
Any {{< knowl id="smooth-map" text="smooth map" >}} \(f:M\to N\) induces a map on tangent bundles
\[
df:TM\to TN
\]
defined fiberwise by the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} \(d f_p:T_pM\to T_{f(p)}N\). This “bundle map” covers \(f\) in the sense that \(\pi_N\circ df = f\circ \pi_M\).

## Examples
1. **Euclidean space is trivial.** For \(M=\mathbb{R}^n\), the tangent bundle is canonically diffeomorphic to a product:
   \[
   T\mathbb{R}^n \cong \mathbb{R}^n \times \mathbb{R}^n,
   \]
   with \(\pi(x,v)=x\).

2. **The circle is also trivial.** The tangent bundle of \(S^1\) is trivial:
   \[
   TS^1 \cong S^1\times \mathbb{R}.
   \]
   Concretely, the unit tangent vector field \(X(\cos t,\sin t)=(-\sin t,\cos t)\) provides a global framing.

3. **Products.** For smooth manifolds \(M\) and \(N\), there is a canonical identification
   \[
   T(M\times N) \cong TM \times TN
   \]
   compatible with the projections to \(M\times N\). Under this identification, a tangent vector at \((p,q)\) is a pair \((v,w)\) with \(v\in T_pM\) and \(w\in T_qN\).

(For comparison, the dual bundle of \(TM\) is the {{< knowl id="cotangent-bundle" text="cotangent bundle" >}}.)
