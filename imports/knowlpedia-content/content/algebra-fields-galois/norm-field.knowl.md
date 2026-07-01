+++
id = "algebra-fields-galois/norm-field"
title = "Field norm"
kind = "knowl"
summary = "For a finite extension L/K, the norm N_{L/K}(α) is the determinant of multiplication-by-α as a K-linear map."
aliases = ["norm-field", "Field norm"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/norm-field.md"
+++

Let \(L/K\) be a finite [[algebra-fields-galois/field-extension|field extension]] of degree \(n=[L:K]\). For \(\alpha\in L\), consider the \(K\)-linear map \(m_\alpha:L\to L\), \(x\mapsto \alpha x\). The **(field) norm** of \(\alpha\) from \(L\) to \(K\) is
\[
\mathrm{N}_{L/K}(\alpha) := \det(m_\alpha)\in K.
\]

If \(L/K\) is separable (see [[algebra-fields-galois/separable-extension|separable extension]]) and \(\Omega\) contains \(L\), then
\[
\mathrm{N}_{L/K}(\alpha)=\prod_{\sigma} \sigma(\alpha),
\]
where the product runs over all \(K\)-[[algebra-fields-galois/field-embedding|embeddings]] \(\sigma:L\hookrightarrow \Omega\). The norm is multiplicative, \(\mathrm{N}_{L/K}(\alpha\beta)=\mathrm{N}_{L/K}(\alpha)\mathrm{N}_{L/K}(\beta)\), and satisfies the tower property in [[algebra-fields-galois/trace-norm-towers|trace/norm in towers]] for a [[algebra-fields-galois/tower-of-fields|tower of fields]] \(K\subseteq M\subseteq L\).

### Examples
1. **Quadratic extension.** Let \(L=K(\sqrt{d})\) with \(\mathrm{char}(K)\neq 2\). For \(\alpha=a+b\sqrt{d}\),
\[
\mathrm{N}_{L/K}(\alpha)=(a+b\sqrt{d})(a-b\sqrt{d})=a^2-b^2d.
\]

2. **Norm via minimal polynomial.** If \(L=K(\alpha)\) is a [[algebra-fields-galois/simple-extension|simple extension]] and the minimal polynomial of \(\alpha\) over \(K\) is \(m_\alpha(x)=x^n+c_{n-1}x^{n-1}+\cdots+c_0\), then
\[
\mathrm{N}_{L/K}(\alpha)=(-1)^n c_0.
\]
(Here \(c_0\) is the constant term.)

3. **Finite fields.** For \(L=\mathbb{F}_{q^n}\) over \(K=\mathbb{F}_q\),
\[
\mathrm{N}_{L/K}(\alpha)=\alpha\cdot \alpha^{q}\cdot \alpha^{q^2}\cdots \alpha^{q^{n-1}}=\alpha^{(q^n-1)/(q-1)}.
\]
This is compatible with the cyclic structure of the multiplicative group (see [[algebra-fields-galois/finite-field-multiplicative-group-cyclic|finite-field multiplicative group is cyclic]]).
