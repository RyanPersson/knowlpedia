---
title: "Inner product space"
description: "A vector space equipped with an inner product."
---

An **inner product space** is a {{< knowl id="vector-space" text="vector space" >}} $V$ over $\mathbb{R}$ or $\mathbb{C}$ together with a specified {{< knowl id="inner-product" text="inner product" >}} $\langle\cdot,\cdot\rangle$ on $V$.

Every inner product space is automatically a {{< knowl id="normed-vector-space" text="normed vector space" >}} via $\|v\|=\sqrt{\langle v,v\rangle}$, and many constructions in linear algebra are organized by {{< knowl id="orthogonality" text="orthogonality" >}}. A complete inner product space is a {{< knowl id="hilbert-space" text="Hilbert space" >}}.

**Examples:**
- $\mathbb{R}^n$ with the standard dot product is an inner product space.
- $\mathbb{C}^n$ with the standard Hermitian product is an inner product space.
- The space of polynomials on $[0,1]$ with $\langle p,q\rangle=\int_0^1 p(t)q(t)\,dt$ is an inner product space.
