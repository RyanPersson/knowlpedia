---
title: "Algebra homomorphism"
description: "A ring homomorphism that respects the chosen base-ring action."
---

An **algebra homomorphism** between \(R\)-algebras \(A\) and \(B\) (with structure maps \(\iota_A\colon R\to A\), \(\iota_B\colon R\to B\)) is a {{< knowl id="ring-homomorphism" section="algebra-rings" text="ring homomorphism" >}} \(\varphi\colon A\to B\) such that \(\varphi\circ \iota_A=\iota_B\). Equivalently, \(\varphi\) is a unital ring homomorphism that is \(R\)-linear as a {{< knowl id="module-homomorphism" text="module homomorphism" >}} with respect to the induced \(R\)-module structures coming from the {{< knowl id="algebra-over-ring" text="algebra structure" >}}

Algebra homomorphisms are the morphisms in the category of \(R\)-algebras; they preserve both multiplication and the base-ring scalars.

**Examples:**
- For any \(R\)-algebra \(A\) and \(a\in A\), evaluation \(R[x]\to A\), \(p(x)\mapsto p(a)\), is an \(R\)-algebra homomorphism from the {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial ring" >}}.
- If \(J\triangleleft A\) is an ideal stable under the \(R\)-algebra structure, then the quotient map \(A\to A/J\) is an \(R\)-algebra homomorphism.
