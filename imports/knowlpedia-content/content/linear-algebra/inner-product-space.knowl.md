+++
id = "linear-algebra/inner-product-space"
title = "Inner product space"
kind = "knowl"
summary = "A vector space equipped with an inner product."
aliases = ["inner-product-space", "Inner product space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/inner-product-space.md"
+++

An **inner product space** is a [[linear-algebra/vector-space|vector space]] $V$ over $\mathbb{R}$ or $\mathbb{C}$ together with a specified [[linear-algebra/inner-product|inner product]] $\langle\cdot,\cdot\rangle$ on $V$.

Every inner product space is automatically a [[linear-algebra/normed-vector-space|normed vector space]] via $\|v\|=\sqrt{\langle v,v\rangle}$, and many constructions in linear algebra are organized by [[linear-algebra/orthogonality|orthogonality]]. A complete inner product space is a [[linear-algebra/hilbert-space|Hilbert space]].

**Examples:**
- $\mathbb{R}^n$ with the standard dot product is an inner product space.
- $\mathbb{C}^n$ with the standard Hermitian product is an inner product space.
- The space of polynomials on $[0,1]$ with $\langle p,q\rangle=\int_0^1 p(t)q(t)\,dt$ is an inner product space.
