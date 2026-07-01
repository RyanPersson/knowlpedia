+++
id = "algebra-rings/content-formula"
title = "Content formula"
kind = "knowl"
summary = "Over a UFD, content(fg) is associate to content(f)content(g) for polynomials."
aliases = ["content-formula", "Content formula"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/content-formula.md"
+++

**Content formula**: Let $R$ be a UFD and let $f,g\in R[x]$. Then the content satisfies
\[
\operatorname{cont}(fg)\sim \operatorname{cont}(f)\operatorname{cont}(g),
\]
i.e., $\operatorname{cont}(fg)$ is associate to $\operatorname{cont}(f)\operatorname{cont}(g)$. In particular, the product of primitive polynomials is primitive.

Here [[algebra-rings/content-polynomial|content]] is computed in the [[algebra-rings/polynomial-ring|polynomial ring]] over a [[algebra-rings/ufd|UFD]]. The formula implies that the product of two [[algebra-rings/primitive-polynomial|primitive polynomials]] is primitive and is a standard ingredient in [[algebra-rings/gauss-content-lemma|Gauss's content lemma]].
