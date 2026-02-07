---
title: "Determinant on I + Trace-Class"
description: "Extension of det via det(I+A)=exp(tr log(I+A)) for trace-class A"
---

For trace-class \(A\), one defines a determinant-like map \(\Delta(I+A)\) ("Fredholm determinant")
extending {{< knowl id="determinant" section="linear-algebra" text="determinant" >}} from finite rank.

**Key properties (paper use):**
- Near \(I\): \(\Delta(T)=\exp(\mathrm{tr}(\log T))\) (Lemma 2.1(a)).
- \(\Delta\) is continuous on \(GL(H)_1=I+\)trace-class.
- No continuous extension exists on \(GL(H)_2=I+\)Hilbert–Schmidt (Lemma 2.1(b)).

**Example:** If \(A\) is finite rank, \(\Delta(I+A)\) matches the usual finite-dimensional determinant.
