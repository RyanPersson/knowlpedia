+++
id = "measure-theory/measurable-set"
title = "Measurable set"
kind = "knowl"
summary = "A subset that belongs to the sigma-algebra of a measurable space."
aliases = ["measurable-set", "Measurable set"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/measurable-set.md"
+++

A **measurable set** in a measurable space $(X,\Sigma)$ is a subset $A\subseteq X$ with $A\in\Sigma$.

Measurable sets are precisely the subsets to which a [[measure-theory/measure|measure]] assigns a value, and they determine [[measure-theory/measurable-function|measurable functions]] via preimages. The [[measure-theory/indicator-function|indicator function]] of a measurable set is a basic example of a measurable function.

**Examples:**
- In $(\mathbb R,\mathcal B(\mathbb R))$ with the [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]], every open [[real-analysis/interval|interval]] such as $(a,b)$ is measurable.
- If $A$ is measurable in $(X,\Sigma)$, then its [[shared-foundations/complement|complement]] $X\setminus A$ is also measurable.
- If $(A_n)_{n\ge 1}$ are measurable, then the countable [[shared-foundations/union|union]] $\bigcup_{n=1}^\infty A_n$ is measurable.
