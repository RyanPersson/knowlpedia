+++
id = "algebra-modules/tensor-product-algebras"
title = "Tensor product of algebras"
kind = "knowl"
summary = "The tensor product A⊗_R B equipped with the induced algebra structure."
aliases = ["tensor-product-algebras", "Tensor product of algebras"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-product-algebras.md"
+++

The **tensor product of algebras** \(A\otimes_R B\) of two \(R\)-algebras \(A,B\) over a [[algebra-rings/commutative-ring|commutative ring]] \(R\) is the [[algebra-modules/tensor-product|tensor product]] of the underlying \(R\)-modules, equipped with the unique \(R\)-algebra structure for which
\[
(a\otimes b)\cdot (a'\otimes b') = (aa')\otimes (bb')
\]
and whose structure map \(R\to A\otimes_R B\) is \(r\mapsto (r\cdot 1_A)\otimes 1_B = 1_A\otimes (r\cdot 1_B)\). The multiplication is induced from the bilinear multiplication maps in \(A\) and \(B\) via the universal property of \(\otimes_R\).

This construction is the algebraic version of “base change” and interacts well with presentations, quotients, and localization in commutative algebra.

**Examples:**
- Over a field \(k\), one has \(k[x]\otimes_k k[y]\cong k[x,y]\) as \(k\)-algebras, where \(k[x]\) is a [[algebra-rings/polynomial-ring|polynomial ring]].
- If \(S\) is an \(R\)-algebra and \(I\subseteq R\) is an [[algebra-rings/ideal|ideal]], then \(S\otimes_R (R/I)\cong S/IS\) as \(R\)-algebras.
