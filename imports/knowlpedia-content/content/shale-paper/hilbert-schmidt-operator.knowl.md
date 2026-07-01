+++
id = "shale-paper/hilbert-schmidt-operator"
title = "Hilbert–Schmidt Operator"
kind = "knowl"
summary = "An operator with finite ℓ²-norm of matrix coefficients (Schatten class 2)"
aliases = ["hilbert-schmidt-operator", "Hilbert–Schmidt Operator"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/hilbert-schmidt-operator.md"
+++

A bounded operator \(X\) on a Hilbert space is **Hilbert–Schmidt** if
\(\|X\|_2^2=\sum_\alpha \|Xe_\alpha\|^2<\infty\) for some (hence any) orthonormal basis \(\{e_\alpha\}\).

**Key properties (paper use):**
- Hilbert–Schmidt operators are [[linear-algebra/compact-operator|compact]].
- "Restricted" conditions are of the form \(|T|-I\in HS\) (membership in \(GL(H)_2\), \(rGL(H)\), \(rSp(K)\)).

**Example:** On \(\ell^2\), the diagonal operator \(\mathrm{diag}(a_n)\) is HS iff \(\sum_n |a_n|^2<\infty\).
