---
title: "Gauss lemma (content multiplicativity)"
description: "In a UFD, the content of a product equals the product of contents up to associates."
---

**Gauss content lemma**: Let \(R\) be a {{< knowl id="ufd" text="UFD" >}}. For \(f,g\in R[x]\) in the {{< knowl id="polynomial-ring" text="polynomial ring" >}}, let \(\operatorname{cont}(f)\) denote the {{< knowl id="content-polynomial" text="content" >}} of \(f\) (a gcd of its coefficients, defined up to units). Then
\[
\operatorname{cont}(fg)\ \sim\ \operatorname{cont}(f)\operatorname{cont}(g),
\]
where \(\sim\) denotes equality up to {{< knowl id="associated-elements" text="associates" >}}. Equivalently, the product of two {{< knowl id="primitive-polynomial" text="primitive polynomials" >}} is primitive.

This lemma is the technical engine behind Gauss-type transfer results between \(R[x]\) and \(\mathrm{Frac}(R)[x]\).