+++
id = "algebra-rings/gauss-content-lemma"
title = "Gauss lemma (content multiplicativity)"
kind = "knowl"
summary = "In a UFD, the content of a product equals the product of contents up to associates."
aliases = ["gauss-content-lemma", "Gauss lemma (content multiplicativity)"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/gauss-content-lemma.md"
+++

**Gauss content lemma**: Let \(R\) be a [[algebra-rings/ufd|UFD]]. For \(f,g\in R[x]\) in the [[algebra-rings/polynomial-ring|polynomial ring]], let \(\operatorname{cont}(f)\) denote the [[algebra-rings/content-polynomial|content]] of \(f\) (a gcd of its coefficients, defined up to units). Then
\[
\operatorname{cont}(fg)\ \sim\ \operatorname{cont}(f)\operatorname{cont}(g),
\]
where \(\sim\) denotes equality up to [[algebra-rings/associated-elements|associates]]. Equivalently, the product of two [[algebra-rings/primitive-polynomial|primitive polynomials]] is primitive.

This lemma is the technical engine behind Gauss-type transfer results between \(R[x]\) and \(\mathrm{Frac}(R)[x]\).
