---
title: "Tangent space at a point"
description: "The vector space of tangent vectors to a smooth manifold at a given point."
---

Let \(M\) be a {{< knowl id="smooth-manifold" text="smooth manifold" >}} and let \(p\in M\).

## Definition (Derivations)
The **tangent space** \(T_pM\) is the real vector space of all derivations at \(p\), i.e. all \(\mathbb{R}\)-linear maps
\[
v: C^\infty(M)\to \mathbb{R}
\]
such that \(v(fg)=f(p)\,v(g)+g(p)\,v(f)\) for all \(f,g\in C^\infty(M)\) (the Leibniz rule).

Elements \(v\in T_pM\) are called **tangent vectors at \(p\)**.

## Coordinate description
If \((U,\varphi)\) is a {{< knowl id="smooth-chart-coordinate-chart" text="smooth chart" >}} with \(p\in U\) and \(\varphi=(x^1,\dots,x^n)\), then there are canonical basis derivations \(\left.\frac{\partial}{\partial x^i}\right|_p\in T_pM\) defined by
\[
\left.\frac{\partial}{\partial x^i}\right|_p (f)
= \frac{\partial (f\circ \varphi^{-1})}{\partial x^i}\bigl(\varphi(p)\bigr).
\]
Every \(v\in T_pM\) is uniquely expressible as \(v=\sum_{i=1}^n v^i \left.\frac{\partial}{\partial x^i}\right|_p\), so a chart identifies \(T_pM\) (non-canonically) with \(\mathbb{R}^n\).

## Functoriality (pushforward)
Given a {{< knowl id="smooth-map" text="smooth map" >}} \(f:M\to N\) between smooth manifolds, there is an induced linear map on tangent spaces
\[
d f_p : T_pM \to T_{f(p)}N,
\]
called the {{< knowl id="differential-pushforward-of-a-smooth-map" text="differential (pushforward)" >}} of \(f\) at \(p\). As \(p\) varies, these tangent spaces assemble into the {{< knowl id="tangent-bundle" text="tangent bundle" >}}.

## Examples
1. **Euclidean space.** For \(M=\mathbb{R}^n\) and any \(p\in \mathbb{R}^n\), there is a canonical identification \(T_p\mathbb{R}^n\cong \mathbb{R}^n\), with basis \(\left.\frac{\partial}{\partial x^1}\right|_p,\dots,\left.\frac{\partial}{\partial x^n}\right|_p\) in the standard coordinates.

2. **The sphere as a constraint.** For \(S^2=\{x\in \mathbb{R}^3:\|x\|=1\}\) and \(p\in S^2\), the tangent space is
   \[
   T_pS^2=\{v\in \mathbb{R}^3 : v\cdot p = 0\},
   \]
   i.e. the plane through the origin orthogonal to \(p\).

3. **Lie groups.** For a {{< knowl id="lie-group" text="Lie group" >}} \(G\) with identity element \(e\), the tangent space \(T_eG\) is the underlying vector space of the {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra" section="lie-groups">}} of \(G\).
