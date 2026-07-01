+++
id = "algebra-modules/algebra-over-ring"
title = "Algebra over a commutative ring"
kind = "knowl"
summary = "A ring equipped with a compatible structure map from a commutative base ring."
aliases = ["algebra-over-ring", "Algebra over a commutative ring"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/algebra-over-ring.md"
+++

An **algebra over a commutative ring** is a [[algebra-rings/unital-ring|unital ring]] \(A\) together with a unital [[algebra-rings/ring-homomorphism|ring homomorphism]] \(\iota\colon R\to A\) from a [[algebra-rings/commutative-ring|commutative ring]] \(R\) such that \(\iota(R)\) lies in the center of \(A\) (equivalently, \(\iota(r)a=a\iota(r)\) for all \(r\in R\), \(a\in A\)).

Equivalently, \(A\) is an \(R\)-[[algebra-modules/module|module]] and the multiplication map \(A\times A\to A\) is \(R\)-bilinear, with \(1_R\) acting as \(1_A\). This framework unifies familiar constructions such as [[algebra-rings/polynomial-ring|polynomial rings]] and quotients.

**Examples:**
- The polynomial ring \(R[x]\) is an \(R\)-algebra via the inclusion \(R\hookrightarrow R[x]\).
- For an ideal \(I\subseteq R\), the [[algebra-rings/quotient-ring|quotient ring]] \(R/I\) is an \(R\)-algebra via the quotient map, where \(I\) is an [[algebra-rings/ideal|ideal]].
- The matrix ring \(M_n(R)\) is an \(R\)-algebra via scalar matrices \(r\mapsto rI_n\).
