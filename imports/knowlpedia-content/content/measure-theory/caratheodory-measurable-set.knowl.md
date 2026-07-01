+++
id = "measure-theory/caratheodory-measurable-set"
title = "Carathéodory measurable set"
kind = "knowl"
summary = "A set that satisfies Carathéodory’s splitting condition for an outer measure."
aliases = ["caratheodory-measurable-set", "Carathéodory measurable set"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/caratheodory-measurable-set.md"
+++

A **Carathéodory measurable set** (with respect to an outer measure $\mu^*$ on $X$) is a subset $E\subseteq X$ such that for every subset $S\subseteq X$,
\[
\mu^*(S)=\mu^*(S\cap E)+\mu^*(S\setminus E).
\]

This condition says $E$ “splits” every set $S$ without loss of outer measure, using [[shared-foundations/intersection|intersection]] and [[shared-foundations/set-difference|set difference]]. In the [[measure-theory/caratheodory-construction|Carathéodory construction]], the collection of Carathéodory measurable sets forms a [[measure-theory/sigma-algebra|sigma-algebra]], and restricting $\mu^*$ to it gives a [[measure-theory/measure|measure]].

**Examples:**
- If $\mu^*$ is induced from a measure $\mu$ on a sigma-algebra $\Sigma$ (via the usual infimum over measurable supersets), then every $A\in\Sigma$ is Carathéodory measurable.
- For Lebesgue outer measure on $\mathbb R$, every [[measure-theory/borel-sigma-algebra|Borel set]] is Carathéodory measurable (and in fact many more sets are as well).
