---
title: "Pure gauge connection on a trivial bundle"
description: "A flat connection obtained from the zero connection by a global gauge transformation."
---

Let $P=M\times G\to M$ be a trivial principal bundle, where $G$ is a Lie group with Lie algebra $\mathfrak g$.

## Definition (pure gauge potential)
Given a smooth map $g:M\to G$ (a gauge transformation), define a $\mathfrak g$-valued 1-form on $M$ by
\[
A := g^{-1}dg \in \Omega^1(M;\mathfrak g),
\]
the pullback of the left Maurer–Cartan form along $g$.

This $A$ is called a **pure gauge** potential because it is exactly the gauge transform of the {{< knowl id="flat-connection-a0-on-a-trivial-bundle" text="flat connection" >}} with $A=0$.

## Flatness
Viewed as the local gauge potential of a {{< knowl id="principal-connection" text="principal connection" >}} on $M\times G$, the curvature is
\[
F = dA + \tfrac12[A\wedge A],
\]
and one has $F=0$ for $A=g^{-1}dg$ by the Maurer–Cartan identity. Hence pure gauge connections are flat.

In particular, their holonomy is trivial up to the natural basepoint identifications (they are globally gauge-equivalent to the product connection).

## Examples
1. **Abelian case.**  
   For $G=U(1)$, write $g=e^{if}$ for a smooth real-valued function $f$ (locally or globally when possible). Then $A$ is (up to the conventional factor of $i$) the 1-form $df$, and the curvature vanishes because $d(df)=0$.

2. **Matrix groups.**  
   For $G=\mathrm{GL}(n,\mathbb R)$ and a smooth map $g:M\to \mathrm{GL}(n,\mathbb R)$, the potential is the matrix-valued 1-form $A=g^{-1}dg$, flat by the same identity.

3. **Local normal form of flat connections.**  
   On a contractible open set $U\subset M$, any flat connection can be written (after choosing a trivialization) as $A=g^{-1}dg$ for some smooth $g:U\to G$.
