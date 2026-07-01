+++
id = "shale-paper/fredholm-determinant-trace-log"
title = "Determinant on I + Trace-Class"
kind = "knowl"
summary = "Extension of det via det(I+A)=exp(tr log(I+A)) for trace-class A"
aliases = ["fredholm-determinant-trace-log", "Determinant on I + Trace-Class"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/fredholm-determinant-trace-log.md"
+++

For trace-class \(A\), one defines a determinant-like map \(\Delta(I+A)\) ("Fredholm determinant")
extending [[linear-algebra/determinant|determinant]] from finite rank.

**Key properties (paper use):**
- Near \(I\): \(\Delta(T)=\exp(\mathrm{tr}(\log T))\) (Lemma 2.1(a)).
- \(\Delta\) is continuous on \(GL(H)_1=I+\)trace-class.
- No continuous extension exists on \(GL(H)_2=I+\)Hilbert–Schmidt (Lemma 2.1(b)).

**Example:** If \(A\) is finite rank, \(\Delta(I+A)\) matches the usual finite-dimensional determinant.
