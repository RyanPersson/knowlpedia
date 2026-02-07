---
title: "Transition matrix of a local frame"
description: "The matrix-valued function describing how two local frames are related on an overlap."
---

Let $\pi:E\to M$ be a rank $r$ smooth vector bundle, and let $(e_1,\dots,e_r)$ and $(e'_1,\dots,e'_r)$ be two {{< knowl id="local-frame-of-a-vector-bundle" text="local frames" >}} of $E$ defined on open sets $U$ and $V$, respectively. On the overlap $U\cap V$, there is a unique map
\[
g:U\cap V\to \mathrm{GL}(r,\mathbb F)
\]
that is {{< knowl id="smooth-map" text="smooth" >}} and satisfies, for each $x\in U\cap V$ and each $j=1,\dots,r$,
\[
e'_j(x)=\sum_{i=1}^r e_i(x)\,g_{ij}(x).
\]
In matrix notation (with frames viewed as column vectors of sections), this reads
\[
e'(x)=e(x)\,g(x).
\]
The map $g$ is called the **transition matrix** from the frame $e$ to the frame $e'$ on $U\cap V$.

If three frames $e,e',e''$ are defined on mutually overlapping sets, their transition matrices satisfy the cocycle identity on triple overlaps:
\[
g_{e,e''}=g_{e,e'}\,g_{e',e''}.
\]

## Examples
1. **Trivial bundle.** For $E=M\times \mathbb F^r$, any two frames over $U$ differ by a smooth $g:U\to \mathrm{GL}(r,\mathbb F)$; the transition matrix is exactly that $g$.

2. **Möbius line bundle.** The Möbius real line bundle over $S^1$ can be described by two trivializations whose overlap transition function is the constant map $g(\theta)=-1\in \mathrm{GL}(1,\mathbb R)$. This single nontrivial transition function encodes the twist.

3. **Orientation check.** For a real bundle, on $U\cap V$ the sign of $\det g(x)$ detects whether the two frames determine the same {{< knowl id="orientation-of-a-real-vector-bundle" text="orientation" >}} (positive determinant) or the opposite one (negative determinant).
