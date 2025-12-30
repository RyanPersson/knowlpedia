---
title: "Flat module"
description: "A module whose tensor product functor preserves exactness."
---

A **flat module** is a left \(R\)-module \(M\) over a ring \(R\) such that tensoring with \(M\) preserves exactness: for every {{< knowl id="short-exact-sequence" text="short exact sequence" >}} of right \(R\)-modules
\[
0\to A\to B\to C\to 0,
\]
the sequence
\[
0\to A\otimes_R M\to B\otimes_R M\to C\otimes_R M\to 0
\]
is exact, where \(\otimes_R\) is the {{< knowl id="tensor-product" text="tensor product" >}}. Equivalently, the functor \(-\otimes_R M\) is exact (it is always right-exact, so flatness is precisely left-exactness).

Flatness is weaker than projectivity: every {{< knowl id="projective-module" text="projective module" >}} is flat (see {{< knowl id="projective-implies-flat" text="projective implies flat" >}}), and every {{< knowl id="free-module" text="free module" >}} is flat. Over a {{< knowl id="commutative-ring" text="commutative ring" >}}, flatness controls base change and localization.

**Examples:**
- Any free \(R\)-module is flat.
- If \(R\) is commutative and \(S\subseteq R\) is multiplicative, then the localization \(S^{-1}R\) is flat as an \(R\)-module.
- Over a {{< knowl id="pid" text="PID" >}}, every {{< knowl id="torsion-free-module" text="torsion-free module" >}} is flat.
