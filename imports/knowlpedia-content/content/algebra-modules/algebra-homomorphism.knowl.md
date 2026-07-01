+++
id = "algebra-modules/algebra-homomorphism"
title = "Algebra homomorphism"
kind = "knowl"
summary = "A ring homomorphism that respects the chosen base-ring action."
aliases = ["algebra-homomorphism", "Algebra homomorphism"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/algebra-homomorphism.md"
+++

An **algebra homomorphism** between \(R\)-algebras \(A\) and \(B\) (with structure maps \(\iota_A\colon R\to A\), \(\iota_B\colon R\to B\)) is a [[algebra-rings/ring-homomorphism|ring homomorphism]] \(\varphi\colon A\to B\) such that \(\varphi\circ \iota_A=\iota_B\). Equivalently, \(\varphi\) is a unital ring homomorphism that is \(R\)-linear as a [[algebra-modules/module-homomorphism|module homomorphism]] with respect to the induced \(R\)-module structures coming from the [[algebra-modules/algebra-over-ring|algebra structure]]

Algebra homomorphisms are the morphisms in the category of \(R\)-algebras; they preserve both multiplication and the base-ring scalars.

**Examples:**
- For any \(R\)-algebra \(A\) and \(a\in A\), evaluation \(R[x]\to A\), \(p(x)\mapsto p(a)\), is an \(R\)-algebra homomorphism from the [[algebra-rings/polynomial-ring|polynomial ring]].
- If \(J\triangleleft A\) is an ideal stable under the \(R\)-algebra structure, then the quotient map \(A\to A/J\) is an \(R\)-algebra homomorphism.
