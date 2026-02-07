---
title: "Hilbert–Schmidt Operator"
description: "An operator with finite ℓ²-norm of matrix coefficients (Schatten class 2)"
---

A bounded operator \(X\) on a Hilbert space is **Hilbert–Schmidt** if
\(\|X\|_2^2=\sum_\alpha \|Xe_\alpha\|^2<\infty\) for some (hence any) orthonormal basis \(\{e_\alpha\}\).

**Key properties (paper use):**
- Hilbert–Schmidt operators are {{< knowl id="compact-operator" section="linear-algebra" text="compact" >}}.
- "Restricted" conditions are of the form \(|T|-I\in HS\) (membership in \(GL(H)_2\), \(rGL(H)\), \(rSp(K)\)).

**Example:** On \(\ell^2\), the diagonal operator \(\mathrm{diag}(a_n)\) is HS iff \(\sum_n |a_n|^2<\infty\).
