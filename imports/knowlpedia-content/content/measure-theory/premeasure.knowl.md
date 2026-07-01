+++
id = "measure-theory/premeasure"
title = "Premeasure"
kind = "knowl"
summary = "A countably additive set function defined on a set algebra."
aliases = ["premeasure"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/premeasure.md"
+++

A **premeasure** on a set algebra $\mathcal A$ is a function $\mu_0:\mathcal A\to[0,\infty]$ with $\mu_0(\varnothing)=0$ such that whenever $(A_n)_{n\ge 1}$ is a pairwise disjoint sequence in $\mathcal A$ whose union $\bigcup_{n=1}^\infty A_n$ also lies in $\mathcal A$, one has
\[
\mu_0\!\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty \mu_0(A_n).
\]
Here $\varnothing$ is the [[shared-foundations/empty-set|empty set]].

Premeasures are typically defined on a [[measure-theory/set-algebra|set algebra]] that is simpler than a full sigma-algebra, and then extended to a [[measure-theory/measure|measure]] using the [[measure-theory/caratheodory-construction|Carathéodory construction]].

**Examples:**
- On the set algebra of finite unions of half-open [[real-analysis/interval|intervals]] $[a,b)\subseteq\mathbb R$, define $\mu_0([a,b))=b-a$ and extend additively across disjoint unions; this is a premeasure.
- On a set $X$, let $\mathcal A$ be the set algebra of finite subsets of $X$ and define $\mu_0(A)=|A|$ (cardinality) for $A\in\mathcal A$; this is a premeasure (the “counting premeasure” on finite sets).
