---
title: "Fenchel-Young inequality"
description: "An inequality relating a function and its Fenchel conjugate via the dual pairing."
---

**Fenchel-Young inequality:** Let $f:\mathbb{R}^n\to(-\infty,+\infty]$ be a proper {{< knowl id="function" section="shared-foundations" text="function" >}}, and let $f^*$ be its {{< knowl id="convex-conjugate-fenchel" text="Fenchel conjugate" >}}. Then for all $x\in\mathbb{R}^n$ and $y\in\mathbb{R}^n$,
$$
f(x)+f^*(y)\ge \langle x,\,y\rangle.
$$

If $f$ is convex, equality holds if and only if $y\in\partial f(x)$ (equivalently, $x\in\partial f^*(y)$), where $\partial f$ denotes the {{< knowl id="subdifferential" text="subdifferential" >}}.

This inequality is the basic mechanism behind weak duality in {{< knowl id="convex-duality-primal-dual" text="convex primal-dual pairs" >}}: conjugate-based dual objectives arise by repeatedly applying Fenchel-Young.
