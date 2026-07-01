+++
id = "algebra-rings/ring-isomorphism"
title = "Ring isomorphism"
kind = "knowl"
summary = "A bijective ring homomorphism with a homomorphic inverse."
aliases = ["ring-isomorphism", "Ring isomorphism"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ring-isomorphism.md"
+++

A **ring isomorphism** is a [[algebra-rings/ring-homomorphism|ring homomorphism]] $\varphi:R\to S$ that is [[shared-foundations/bijective-function|bijective]] and whose inverse function $\varphi^{-1}:S\to R$ is also a ring homomorphism.

Equivalently, $\varphi$ is an isomorphism iff it is bijective and respects the ring operations; then $\varphi^{-1}$ exists as an [[shared-foundations/inverse-function|inverse function]] and automatically preserves operations. Isomorphic rings are “the same” for algebraic purposes: they have corresponding ideal lattices, unit groups, and invariants.

**Examples:**
- The map $R[x]/(x)\to R$ sending $f(x)+(x)\mapsto f(0)$ is a ring isomorphism.
- For a commutative ring $R$, $R\times R \cong R[t]/(t(t-1))$ (one concrete model of a product ring).
- The map $\mathbb Z\to \mathbb Z$, $n\mapsto 2n$, is a ring homomorphism but not an isomorphism (not surjective).
