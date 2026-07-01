+++
id = "shale-paper/jacobian-xT"
title = "Jacobian X(T) in Shale's Gaussian Setup"
kind = "knowl"
summary = "The Radon–Nikodym derivative of the transformed Gaussian measure n(T) with respect to n"
aliases = ["jacobian-xT", "Jacobian X(T) in Shale's Gaussian Setup"]
domains = ["shale-paper"]
legacy_source_path = "shale-paper/jacobian-xT.md"
+++

For \(T\in rGL(M)\), Shale defines a new measure \(n(T)\) via pullback on \(L_\infty\),
and sets
\[
X(T)=\frac{dn(T)}{dn},
\]
the [[shale-paper/radon-nikodym-derivative|Radon–Nikodym derivative]].

**Key properties (paper use):**
- \(X(T)^{1/2}\in L_2(M,n)\) and appears in the unitary implementer \(\mathfrak U(T)\).
- When \(|T|\in GL(M)_1\), \(X(T)\) has an explicit "Gaussian quadratic form" formula.

**Example:** In finite dimensions, \(X(T)\) reduces to \(|\det T|\) times an exponential factor.
