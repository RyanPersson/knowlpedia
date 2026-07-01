+++
id = "shale-paper/trace-class-operator"
title = "Trace-Class Operator"
kind = "knowl"
summary = "An operator with absolutely summable singular values (Schatten class 1)"
aliases = ["trace-class-operator", "Trace-Class Operator"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/trace-class-operator.md"
+++

A bounded operator \(X\) is **trace-class** if its trace norm \(\|X\|_1<\infty\)
(equivalently, the singular values are \(\ell^1\)).

**Key properties (paper use):**
- The trace \(\mathrm{tr}(X)\) is well-defined and basis-independent.
- The "determinant" \(\Delta(I+X)\) extends to \(I+\)trace-class ([[shale-paper/fredholm-determinant-trace-log|Fredholm determinant]]).

**Example:** On \(\ell^2\), \(\mathrm{diag}(a_n)\) is trace-class iff \(\sum_n |a_n|<\infty\).
