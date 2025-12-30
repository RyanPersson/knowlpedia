---
title: "Algebra over a commutative ring"
description: "A ring equipped with a compatible structure map from a commutative base ring."
---

An **algebra over a commutative ring** is a {{< knowl id="unital-ring" section="algebra-rings" text="unital ring" >}} \(A\) together with a unital {{< knowl id="ring-homomorphism" section="algebra-rings" text="ring homomorphism" >}} \(\iota\colon R\to A\) from a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} \(R\) such that \(\iota(R)\) lies in the center of \(A\) (equivalently, \(\iota(r)a=a\iota(r)\) for all \(r\in R\), \(a\in A\)).

Equivalently, \(A\) is an \(R\)-{{< knowl id="module" text="module" >}} and the multiplication map \(A\times A\to A\) is \(R\)-bilinear, with \(1_R\) acting as \(1_A\). This framework unifies familiar constructions such as {{< knowl id="polynomial-ring" section="algebra-rings" text="polynomial rings" >}} and quotients.

**Examples:**
- The polynomial ring \(R[x]\) is an \(R\)-algebra via the inclusion \(R\hookrightarrow R[x]\).
- For an ideal \(I\subseteq R\), the {{< knowl id="quotient-ring" section="algebra-rings" text="quotient ring" >}} \(R/I\) is an \(R\)-algebra via the quotient map, where \(I\) is an {{< knowl id="ideal" section="algebra-rings" text="ideal" >}}.
- The matrix ring \(M_n(R)\) is an \(R\)-algebra via scalar matrices \(r\mapsto rI_n\).
