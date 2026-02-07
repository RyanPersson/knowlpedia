---
title: "Character of a Tensor Product"
description: "For complex representations, the character of a tensor product is the pointwise product of characters."
---

Let \(G\) be a finite group and let \(V,W\) be finite-dimensional complex {{< knowl id="group-representation" text="representations" >}} with actions \(\rho_V,\rho_W\). Their {{< knowl id="tensor-product" section="algebra-modules" text="tensor product" >}} \(V\otimes W\) is a representation via
\[
\rho_{V\otimes W}(g) \;=\; \rho_V(g)\otimes \rho_W(g).
\]
The {{< knowl id="character" text="character" >}} is \(\chi_V(g)=\mathrm{tr}(\rho_V(g))\).

## Proposition
For all \(g\in G\),
\[
\chi_{V\otimes W}(g) \;=\; \chi_V(g)\,\chi_W(g).
\]
Equivalently, \(\chi_{V\otimes W} = \chi_V\cdot \chi_W\) as functions \(G\to \mathbb{C}\).

This follows from the linear algebra identity
\[
\mathrm{tr}(A\otimes B) = \mathrm{tr}(A)\,\mathrm{tr}(B),
\]
using the {{< knowl id="trace" section="linear-algebra" text="trace" >}}.

## Examples

### Example 1: Cyclic group \(C_n\)
For \(G=C_n=\langle g\rangle\), 1D characters satisfy multiplication under tensor product.
Let \(V_a,V_b\) be 1D reps with \(g\mapsto \zeta^a\) and \(g\mapsto \zeta^b\) where \(\zeta=e^{2\pi i/n}\). Then
\[
\chi_{V_a\otimes V_b}(g^m)=\chi_{V_a}(g^m)\chi_{V_b}(g^m)=\zeta^{am}\zeta^{bm}=\zeta^{(a+b)m},
\]
so \(V_a\otimes V_b \cong V_{a+b}\).

### Example 2: \(S_3\): tensoring by the sign representation
Let \(\varepsilon\) be the 1D sign representation of \(S_3\), and let \(\sigma\) be the 2D standard irreducible. On the three conjugacy classes \((e),(\text{transposition}),(\text{3-cycle})\),
\[
\chi_\varepsilon=(1,-1,1),\qquad \chi_\sigma=(2,0,-1).
\]
Then
\[
\chi_{\sigma\otimes \varepsilon}=\chi_\sigma\chi_\varepsilon=(2,0,-1)=\chi_\sigma,
\]
so \(\sigma\otimes \varepsilon \cong \sigma\).

### Example 3: \(S_3\): \(\sigma\otimes\sigma\)
Using \(\chi_{\sigma\otimes\sigma}=\chi_\sigma^2\) pointwise gives
\[
\chi_{\sigma\otimes\sigma}=(2,0,-1)^2=(4,0,1).
\]
Decomposing into irreducibles using the known irreducible characters \(\mathbf{1}=(1,1,1)\), \(\varepsilon=(1,-1,1)\), \(\sigma=(2,0,-1)\), we check:
\[
(4,0,1) = (1,1,1) + (1,-1,1) + (2,0,-1),
\]
so
\[
\sigma\otimes\sigma \cong \mathbf{1}\;\oplus\;\varepsilon\;\oplus\;\sigma.
\]
