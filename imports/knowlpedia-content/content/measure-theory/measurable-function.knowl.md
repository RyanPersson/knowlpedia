+++
id = "measure-theory/measurable-function"
title = "Measurable function"
kind = "knowl"
summary = "A function whose preimages of measurable sets are measurable."
aliases = ["measurable-function", "Measurable function"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/measurable-function.md"
+++

A **measurable function** between measurable spaces $(X,\Sigma)$ and $(Y,\mathcal T)$ is a [[shared-foundations/function|function]] $f:X\to Y$ such that for every $B\in \mathcal T$, the [[shared-foundations/preimage|preimage]] $f^{-1}(B)$ lies in $\Sigma$.

Measurability depends on the choice of sigma-algebras on domain and codomain; in particular, using the [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]] connects measurability to topology. For example, a [[topology/continuous-map|continuous map]] between topological spaces is Borel measurable.

**Examples:**
- If $f:\mathbb R\to\mathbb R$ is continuous (in the usual topology), then $f$ is measurable as a map $(\mathbb R,\mathcal B(\mathbb R))\to(\mathbb R,\mathcal B(\mathbb R))$.
- If $A$ is a [[measure-theory/measurable-set|measurable set]] in $(X,\Sigma)$, then its [[measure-theory/indicator-function|indicator function]] $\mathbf 1_A:X\to\{0,1\}$ is measurable (with $\{0,1\}$ carrying its power-set sigma-algebra).
- Every [[measure-theory/simple-function|simple function]] is measurable by definition.
