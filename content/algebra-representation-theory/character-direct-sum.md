---
title: "Character of a Direct Sum"
description: "For complex representations, the character of a direct sum is the sum of the characters."
---

Let \(G\) be a finite group and let \(V\) be a finite-dimensional complex {{< knowl id="group-representation" text="representation" >}} with action \(\rho_V:G\to \mathrm{GL}(V)\). Its {{< knowl id="character" text="character" >}} is the class function
\[
\chi_V(g) \;=\; \mathrm{tr}(\rho_V(g)),
\]
using the {{< knowl id="trace" section="linear-algebra" text="trace" >}}.

If \(V\) and \(W\) are representations, their direct sum \(V\oplus W\) is a {{< knowl id="direct-sum-modules" section="algebra-modules" text="direct sum" >}} representation with
\[
\rho_{V\oplus W}(g) \;=\;
\begin{pmatrix}
\rho_V(g) & 0\\
0 & \rho_W(g)
\end{pmatrix}.
\]

## Proposition
For all \(g\in G\),
\[
\chi_{V\oplus W}(g) \;=\; \chi_V(g) + \chi_W(g).
\]
More generally, for a finite direct sum \(\bigoplus_{i=1}^m V_i\),
\[
\chi_{\oplus_i V_i} \;=\; \sum_{i=1}^m \chi_{V_i}.
\]

This identity is used constantly alongside {{< knowl id="character-orthogonality" text="character orthogonality" >}} to compute multiplicities of {{< knowl id="irreducible-representation" text="irreducible representations" >}} inside a given representation.

## Examples

### Example 1: \(S_3\) permutation representation on 3 letters
Let \(V=\mathbb{C}^3\) with \(S_3\) acting by permuting the standard basis. Its character counts fixed points:
- \(\chi_V(e)=3\),
- for a transposition, \(\chi_V(\text{transposition})=1\),
- for a 3-cycle, \(\chi_V(\text{3-cycle})=0\).

This representation decomposes as \(V \cong \mathbf{1} \oplus V_{\mathrm{std}}\), where \(\mathbf{1}\) is the trivial rep and \(V_{\mathrm{std}}\) is the 2D standard irreducible. The characters satisfy
\[
\chi_V = \chi_{\mathbf{1}} + \chi_{\mathrm{std}},
\]
with \(\chi_{\mathbf{1}}=(1,1,1)\) and \(\chi_{\mathrm{std}}=(2,0,-1)\) on the three conjugacy classes, giving \((3,1,0)\) as required.

### Example 2: Cyclic group \(C_n\)
Let \(G=C_n=\langle g\rangle\). Fix \(\zeta=e^{2\pi i/n}\). For integers \(a,b\), let \(V_a\) and \(V_b\) be 1D representations with \(g\) acting by \(\zeta^a\) and \(\zeta^b\). Then
\[
\chi_{V_a}(g^m)=\zeta^{am},\qquad \chi_{V_b}(g^m)=\zeta^{bm},
\]
and the direct sum satisfies
\[
\chi_{V_a\oplus V_b}(g^m)=\zeta^{am}+\zeta^{bm}.
\]

### Example 3: Adding a trivial summand
For any \(V\), the character of \(V\oplus \mathbf{1}\) is \(\chi_V + 1\), i.e. \(\chi_{V\oplus \mathbf{1}}(g)=\chi_V(g)+1\) for every \(g\in G\).
