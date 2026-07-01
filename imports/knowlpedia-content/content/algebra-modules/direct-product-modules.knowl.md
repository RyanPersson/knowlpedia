+++
id = "algebra-modules/direct-product-modules"
title = "Direct product of modules"
kind = "knowl"
summary = "The product of modules: all tuples with coordinatewise operations."
aliases = ["direct-product-modules", "Direct product of modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/direct-product-modules.md"
+++

Given a family of $R$-[[algebra-modules/module|modules]] $(M_i)_{i\in I}$, their **direct product** is
\[
\prod_{i\in I} M_i=\{(m_i)_{i\in I}: m_i\in M_i\},
\]
with coordinatewise addition and scalar multiplication. As a set it is the [[shared-foundations/cartesian-product|Cartesian product]], and it satisfies the categorical product universal property: giving a homomorphism $X\to \prod_i M_i$ is equivalent to giving compatible homomorphisms $X\to M_i$ for all $i$.

For infinite $I$, the product is strictly larger than the [[algebra-modules/direct-sum-modules|direct sum]] because it allows infinitely many nonzero coordinates.

**Examples:**
- $\prod_{n\ge 1}\mathbb Z$ is the set of all integer sequences (no finiteness restriction).
- For modules $M,N$, the product $M\times N$ is the usual binary product with projections.
- (Edge case) If each $M_i=0$, then the product is $0$ even if $I$ is infinite.
