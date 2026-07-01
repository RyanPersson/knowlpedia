+++
id = "algebra-fields-galois/algebraic-element"
title = "Algebraic element"
kind = "knowl"
summary = "An element α is algebraic over F if it satisfies a nonzero polynomial with coefficients in F."
aliases = ["algebraic-element", "Algebraic element"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/algebraic-element.md"
+++

Let \(E/F\) be a [[algebra-fields-galois/field-extension|field extension]] and let \(\alpha\in E\). The element \(\alpha\) is **algebraic over \(F\)** if there exists a nonzero polynomial \(f(x)\in F[x]\) such that
\[
f(\alpha)=0 \quad \text{in } E.
\]
If no such nonzero polynomial exists, then \(\alpha\) is [[algebra-fields-galois/transcendental-element|transcendental over F]].

Equivalently, \(\alpha\) is algebraic over \(F\) iff the evaluation homomorphism
\[
\operatorname{ev}_\alpha: F[x]\to E,\quad f\mapsto f(\alpha),
\]
has nonzero kernel. When \(\alpha\) is algebraic, the simple extension \(F(\alpha)/F\) (see [[algebra-fields-galois/simple-extension|simple extension]]) is an [[algebra-fields-galois/algebraic-extension|algebraic extension]] and has finite [[algebra-fields-galois/degree-of-extension|degree]].

### Examples
1. \(\sqrt2\in \mathbb{R}\) is algebraic over \(\mathbb{Q}\) because it satisfies \(x^2-2=0\).
2. \(i\in \mathbb{C}\) is algebraic over \(\mathbb{R}\) because it satisfies \(x^2+1=0\).
3. Every element of \(\mathbb{F}_{p^n}\) is algebraic over \(\mathbb{F}_p\): for any \(a\in\mathbb{F}_{p^n}\), one has \(a^{p^n}=a\), so \(a\) is a root of \(x^{p^n}-x\in\mathbb{F}_p[x]\).
