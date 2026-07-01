+++
id = "lie-groups/semisimple-direct-sum-simple"
title = "Semisimple Lie algebra as a direct sum of simple ideals"
kind = "knowl"
summary = "A finite-dimensional semisimple Lie algebra splits uniquely as a direct sum of simple Lie algebras."
aliases = ["semisimple-direct-sum-simple", "Semisimple Lie algebra as a direct sum of simple ideals"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/semisimple-direct-sum-simple.md"
+++

Let $\mathfrak g$ be a finite-dimensional Lie algebra over a field of characteristic $0$ (typically $\mathbb C$) and assume $\mathfrak g$ is [[lie-groups/semisimple-lie-algebra|semisimple]]. Then:

**Theorem (semisimple = direct sum of simple ideals).**
There exist simple ideals $\mathfrak s_1,\dots,\mathfrak s_r\subseteq \mathfrak g$ (see [[lie-groups/simple-lie-algebra|simple Lie algebra]] and [[lie-groups/ideal-lie-algebra|ideal]]) such that
\[
\mathfrak g \;\cong\; \mathfrak s_1 \oplus \cdots \oplus \mathfrak s_r
\]
as Lie algebras (see [[lie-groups/direct-sum-of-lie-algebras|direct sum of Lie algebras]]). Moreover, each $\mathfrak s_i$ is an ideal in $\mathfrak g$, and the decomposition is unique up to permutation of the simple summands.

A standard structural proof uses the [[lie-groups/killing-form|Killing form]]: for semisimple $\mathfrak g$ the Killing form is nondegenerate (see [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegenerate iff semisimple]]), and minimal nonzero ideals turn out to be simple; orthogonal complements with respect to the Killing form provide complementary ideals, yielding an internal direct sum.

This theorem reduces many questions about semisimple Lie algebras to the simple case, which is exactly the setting of the [[lie-groups/classification-simple-lie-algebras|classification of simple Lie algebras]].
