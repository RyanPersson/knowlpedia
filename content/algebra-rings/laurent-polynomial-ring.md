---
title: "Laurent polynomial ring"
description: "The ring of finite sums of a_i x^i allowing negative exponents."
---

Let $R$ be a commutative ring with $1$. The **Laurent polynomial ring** $R[x,x^{-1}]$ consists of all finite sums
\[
\sum_{i=m}^n a_i x^i \quad (a_i\in R,\; m\le n,\; m\in\mathbb{Z}),
\]
with the obvious addition and multiplication extending those of {{< knowl id="polynomial-ring" text="polynomial rings" >}}.

This is the result of adjoining an inverse to the indeterminate: $x$ becomes a {{< knowl id="unit" text="unit" >}} in $R[x,x^{-1}]$. Laurent polynomial rings are basic examples of localizations and appear naturally in algebraic geometry and representation theory.

**Examples:**
- Over a field $k$, $k[t,t^{-1}]$ is the coordinate ring of the multiplicative group $k^\times$.
- $\mathbb{Z}[q,q^{-1}]$ is the ring of Laurent polynomials in $q$ with integer coefficients.
- The series $\sum_{n\ge 0} x^{-n}$ is not a Laurent polynomial (it has infinitely many negative-degree terms).