+++
id = "measure-theory/sigma-algebra"
title = "Sigma-algebra"
kind = "knowl"
summary = "A collection of subsets closed under complements and countable unions."
aliases = ["sigma-algebra"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/sigma-algebra.md"
+++

A **sigma-algebra** on a set $X$ is a nonempty collection $\Sigma \subseteq \mathcal P(X)$ such that if $A\in\Sigma$ then $X\setminus A\in\Sigma$, and whenever $(A_n)_{n\ge 1}$ is a sequence in $\Sigma$, the union $\bigcup_{n=1}^\infty A_n$ lies in $\Sigma$.

Equivalently, $\Sigma$ contains $X$ and is closed under complements and countable [[shared-foundations/union|unions]]; it then automatically contains the [[shared-foundations/empty-set|empty set]] and is closed under countable [[shared-foundations/intersection|intersections]]. Sigma-algebras define [[measure-theory/measurable-space|measurable spaces]] and are the domains of [[measure-theory/measure|measures]].

**Examples:**
- For any $X$, the [[shared-foundations/power-set|power set]] $\mathcal P(X)$ is a sigma-algebra.
- On $\mathbb R$ with its usual topology, the [[measure-theory/borel-sigma-algebra|Borel sigma-algebra]] is a sigma-algebra.
- The “trivial” sigma-algebra $\{\varnothing, X\}$ is a sigma-algebra on any set $X$.
