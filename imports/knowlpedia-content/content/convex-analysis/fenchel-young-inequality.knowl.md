+++
id = "convex-analysis/fenchel-young-inequality"
title = "Fenchel-Young inequality"
kind = "knowl"
summary = "An inequality relating a function and its Fenchel conjugate via the dual pairing."
aliases = ["fenchel-young-inequality", "Fenchel-Young inequality"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/fenchel-young-inequality.md"
+++

**Fenchel-Young inequality:** Let $f:\mathbb{R}^n\to(-\infty,+\infty]$ be a proper [[shared-foundations/function|function]], and let $f^*$ be its [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]. Then for all $x\in\mathbb{R}^n$ and $y\in\mathbb{R}^n$,
$$
f(x)+f^*(y)\ge \langle x,\,y\rangle.
$$

If $f$ is convex, equality holds if and only if $y\in\partial f(x)$ (equivalently, $x\in\partial f^*(y)$), where $\partial f$ denotes the [[convex-analysis/subdifferential|subdifferential]].

This inequality is the basic mechanism behind weak duality in [[convex-analysis/convex-duality-primal-dual|convex primal-dual pairs]]: conjugate-based dual objectives arise by repeatedly applying Fenchel-Young.
