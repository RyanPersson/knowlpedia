+++
id = "algebra-rings/ring-monomorphism"
title = "Ring monomorphism"
kind = "knowl"
summary = "An injective ring homomorphism."
aliases = ["ring-monomorphism", "Ring monomorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring-monomorphism.md"
+++

A **ring monomorphism** is a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi:R\to S$ that is [[shared-foundations/injective-function|injective]] as a function.

Monomorphisms identify $R$ with a subring of $S$ up to isomorphism; equivalently, they are the homomorphisms with trivial [[algebra-rings/kernel-ring|kernel]]. In many contexts, one suppresses $\varphi$ and views $R$ as sitting inside $S$.

**Examples:**
- The inclusion $\mathbb Z\hookrightarrow \mathbb Q$ is a ring monomorphism.
- The map $k[x]\hookrightarrow k[x,y]$ sending $f(x)\mapsto f(x)$ is a ring monomorphism.
- The reduction map $\mathbb Z\to \mathbb Z/n\mathbb Z$ is not a monomorphism for $n\ge 2$.
