---
title: "Bilinear map"
description: "A map that is linear in each variable (and balanced over a ring when needed)."
---

A **bilinear map** between \(R\)-modules (for a {{< knowl id="commutative-ring" section="algebra-rings" text="commutative ring" >}} \(R\)) is a function \(\beta\colon M\times N\to P\) from a {{< knowl id="cartesian-product" section="analysis" text="cartesian product" >}} of \(R\)-modules such that, for each fixed argument, the resulting map is \(R\)-linear in the other:
\[
\beta(m+m',n)=\beta(m,n)+\beta(m',n),\quad \beta(m,n+n')=\beta(m,n)+\beta(m,n'),
\]
\[
\beta(rm,n)=r\,\beta(m,n),\quad \beta(m,rn)=r\,\beta(m,n).
\]
For a noncommutative ring \(R\), if \(M\) is a right \(R\)-module and \(N\) is a left \(R\)-module, one usually requires \(\beta\) to be **\(R\)-balanced**, meaning additionally \(\beta(mr,n)=\beta(m,rn)\).

Balanced bilinear maps are exactly the maps represented by the {{< knowl id="tensor-product-universal-property" text="universal property of the tensor product" >}}: they correspond uniquely to homomorphisms out of \(M\otimes_R N\) in the category of {{< knowl id="module" text="modules" >}}/abelian groups.

**Examples:**
- Multiplication \(\mu\colon R\times R\to R\) is bilinear for any {{< knowl id="ring" section="algebra-rings" text="ring" >}} \(R\).
- For a commutative ring \(R\) and an \(R\)-module \(M\), the evaluation pairing \(M^\vee\times M\to R\) is bilinear, where \(M^\vee\) is the {{< knowl id="dual-module" text="dual module" >}}.
