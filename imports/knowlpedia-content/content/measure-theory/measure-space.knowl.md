+++
id = "measure-theory/measure-space"
title = "Measure space"
kind = "knowl"
summary = "A measurable space equipped with a measure."
aliases = ["measure-space", "Measure space"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/measure-space.md"
+++

A **measure space** is a triple $(X,\Sigma,\mu)$ where $(X,\Sigma)$ is a [[measure-theory/measurable-space|measurable space]] and $\mu$ is a [[measure-theory/measure|measure]] on $\Sigma$.

Measure spaces provide the basic setting for integration, convergence theorems, and statements that hold [[measure-theory/almost-everywhere|almost everywhere]] rather than pointwise.

**Examples:**
- For any set $X$, $(X,\mathcal P(X),\mu)$ with $\mu$ the counting measure is a measure space.
- On the unit [[real-analysis/interval|interval]] $[0,1]$, the triple $([0,1],\mathcal B([0,1]),\lambda)$ (Borel sets with a Lebesgue-type length measure $\lambda$) is a standard measure space used in probability and analysis.
