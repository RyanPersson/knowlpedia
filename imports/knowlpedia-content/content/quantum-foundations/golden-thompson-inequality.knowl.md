+++
id = "quantum-foundations/golden-thompson-inequality"
title = "Golden-Thompson inequality"
kind = "knowl"
summary = "Trace inequality bounding Tr exp(A+B) by Tr(exp(A)exp(B)) for Hermitian matrices."
aliases = ["golden-thompson-inequality", "Golden-Thompson inequality"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/golden-thompson-inequality.md"
+++

Let \(A\) and \(B\) be Hermitian (self-adjoint) matrices (equivalently, finite-dimensional self-adjoint operators; see [[quantum-foundations/self-adjoint-operator-observable|self-adjoint-operator-observable]]). The **Golden-Thompson inequality** states that
\[
\operatorname{Tr}\!\big(e^{A+B}\big)\ \le\ \operatorname{Tr}\!\big(e^{A}e^{B}\big),
\]
where \(e^{X}\) denotes the matrix exponential and \(\operatorname{Tr}\) is the trace (see [[quantum-foundations/trace-operator|trace-operator]]).

Using cyclicity of the trace, the right-hand side can also be written as
\[
\operatorname{Tr}\!\big(e^{A}e^{B}\big)=\operatorname{Tr}\!\big(e^{A/2}e^{B}e^{A/2}\big).
\]

### Equality condition
If \(A\) and \(B\) commute (so they are simultaneously diagonalizable), then
\[
e^{A+B}=e^Ae^B
\]
and equality holds. In general, noncommutativity forces \(\operatorname{Tr}(e^{A+B})\) to be no larger than \(\operatorname{Tr}(e^{A}e^{B})\).

### Uses and context
Golden-Thompson is a foundational trace inequality in matrix analysis and quantum theory. It is often used to control partition functions in quantum statistical mechanics and appears in proofs of entropy and monotonicity statements involving [[quantum-foundations/quantum-relative-entropy|quantum-relative-entropy]].
