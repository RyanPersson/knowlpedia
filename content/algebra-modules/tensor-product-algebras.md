---
title: "Tensor product of algebras"
description: "The tensor product A⊗_R B equipped with the induced algebra structure."
---

The **tensor product of algebras** \(A\otimes_R B\) of two \(R\)-algebras \(A,B\) over a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} \(R\) is the {{< knowl id="tensor-product" text="tensor product" >}} of the underlying \(R\)-modules, equipped with the unique \(R\)-algebra structure for which
\[
(a\otimes b)\cdot (a'\otimes b') = (aa')\otimes (bb')
\]
and whose structure map \(R\to A\otimes_R B\) is \(r\mapsto (r\cdot 1_A)\otimes 1_B = 1_A\otimes (r\cdot 1_B)\). The multiplication is induced from the bilinear multiplication maps in \(A\) and \(B\) via the universal property of \(\otimes_R\).

This construction is the algebraic version of “base change” and interacts well with presentations, quotients, and localization in commutative algebra.

**Examples:**
- Over a field \(k\), one has \(k[x]\otimes_k k[y]\cong k[x,y]\) as \(k\)-algebras, where \(k[x]\) is a {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}}.
- If \(S\) is an \(R\)-algebra and \(I\subseteq R\) is an {{< knowl id="ideal" section="algebra-rings" text="ideal" >}}, then \(S\otimes_R (R/I)\cong S/IS\) as \(R\)-algebras.
