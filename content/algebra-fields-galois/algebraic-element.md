---
title: "Algebraic element"
description: "An element α is algebraic over F if it satisfies a nonzero polynomial with coefficients in F."
---

Let \(E/F\) be a {{< knowl id="field-extension" text="field extension" >}} and let \(\alpha\in E\). The element \(\alpha\) is **algebraic over \(F\)** if there exists a nonzero polynomial \(f(x)\in F[x]\) such that
\[
f(\alpha)=0 \quad \text{in } E.
\]
If no such nonzero polynomial exists, then \(\alpha\) is {{< knowl id="transcendental-element" text="transcendental over F" >}}.

Equivalently, \(\alpha\) is algebraic over \(F\) iff the evaluation homomorphism
\[
\operatorname{ev}_\alpha: F[x]\to E,\quad f\mapsto f(\alpha),
\]
has nonzero kernel. When \(\alpha\) is algebraic, the simple extension \(F(\alpha)/F\) (see {{< knowl id="simple-extension" text="simple extension" >}}) is an {{< knowl id="algebraic-extension" text="algebraic extension" >}} and has finite {{< knowl id="degree-of-extension" text="degree" >}}.

### Examples
1. \(\sqrt2\in \mathbb{R}\) is algebraic over \(\mathbb{Q}\) because it satisfies \(x^2-2=0\).
2. \(i\in \mathbb{C}\) is algebraic over \(\mathbb{R}\) because it satisfies \(x^2+1=0\).
3. Every element of \(\mathbb{F}_{p^n}\) is algebraic over \(\mathbb{F}_p\): for any \(a\in\mathbb{F}_{p^n}\), one has \(a^{p^n}=a\), so \(a\) is a root of \(x^{p^n}-x\in\mathbb{F}_p[x]\).
