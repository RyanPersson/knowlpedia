+++
id = "measure-theory/outer-measure"
title = "Outer measure"
kind = "knowl"
summary = "A monotone, countably subadditive set function defined on all subsets."
aliases = ["outer-measure", "Outer measure"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/outer-measure.md"
+++

An **outer measure** on a set $X$ is a function $\mu^*:\mathcal P(X)\to[0,\infty]$ such that $\mu^*(\varnothing)=0$, $\mu^*(A)\le \mu^*(B)$ whenever $A\subseteq B$, and for every sequence $(A_n)_{n\ge 1}$,
\[
\mu^*\!\left(\bigcup_{n=1}^\infty A_n\right)\le \sum_{n=1}^\infty \mu^*(A_n).
\]

Outer measures live on the full [[shared-foundations/power-set|power set]] and are used to define [[measure-theory/caratheodory-measurable-set|Carathéodory measurable sets]]. The [[measure-theory/caratheodory-construction|Carathéodory construction]] turns an outer measure into a genuine [[measure-theory/measure|measure]] on a sigma-algebra.

**Examples:**
- If $(X,\Sigma,\mu)$ is a [[measure-theory/measure-space|measure space]], then $\mu^*(A)=\inf\{\mu(B): B\in\Sigma,\ A\subseteq B\}$ defines an outer measure on $X$.
- Lebesgue outer measure on $\mathbb R^n$ is an outer measure built from coverings by rectangles and is the starting point for [[measure-theory/lebesgue-measure|Lebesgue measure]].
