---
title: "Semisimple Lie algebra as a direct sum of simple ideals"
description: "A finite-dimensional semisimple Lie algebra splits uniquely as a direct sum of simple Lie algebras."
---

Let $\mathfrak g$ be a finite-dimensional Lie algebra over a field of characteristic $0$ (typically $\mathbb C$) and assume $\mathfrak g$ is {{< knowl id="semisimple-lie-algebra" text="semisimple" >}}. Then:

**Theorem (semisimple = direct sum of simple ideals).**  
There exist simple ideals $\mathfrak s_1,\dots,\mathfrak s_r\subseteq \mathfrak g$ (see {{< knowl id="simple-lie-algebra" text="simple Lie algebra" >}} and {{< knowl id="ideal-lie-algebra" text="ideal" >}}) such that
\[
\mathfrak g \;\cong\; \mathfrak s_1 \oplus \cdots \oplus \mathfrak s_r
\]
as Lie algebras (see {{< knowl id="direct-sum-of-lie-algebras" text="direct sum of Lie algebras" >}}). Moreover, each $\mathfrak s_i$ is an ideal in $\mathfrak g$, and the decomposition is unique up to permutation of the simple summands.

A standard structural proof uses the {{< knowl id="killing-form" text="Killing form" >}}: for semisimple $\mathfrak g$ the Killing form is nondegenerate (see {{< knowl id="killing-form-nondegenerate-iff-semisimple" text="nondegenerate iff semisimple" >}}), and minimal nonzero ideals turn out to be simple; orthogonal complements with respect to the Killing form provide complementary ideals, yielding an internal direct sum.

This theorem reduces many questions about semisimple Lie algebras to the simple case, which is exactly the setting of the {{< knowl id="classification-simple-lie-algebras" text="classification of simple Lie algebras" >}}.
