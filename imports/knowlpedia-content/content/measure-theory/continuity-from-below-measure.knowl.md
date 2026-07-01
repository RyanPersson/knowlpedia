+++
id = "measure-theory/continuity-from-below-measure"
title = "Continuity from below"
kind = "knowl"
summary = "For increasing measurable sets, the measure of the union is the limit of the measures."
aliases = ["continuity-from-below-measure", "Continuity from below"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/continuity-from-below-measure.md"
+++

**Continuity from below:** Let $(X,\Sigma,\mu)$ be a [[measure-theory/measure-space|measure space]] and let $E_1,E_2,\dots \in \Sigma$ satisfy
$$
E_1 \subseteq E_2 \subseteq E_3 \subseteq \cdots.
$$
Then
$$
\mu\!\left(\bigcup_{n=1}^\infty E_n\right)=\lim_{n\to\infty}\mu(E_n).
$$

Together with [[measure-theory/continuity-from-above-measure|continuity from above]], this expresses how [[measure-theory/measure|measures]] interact with countable unions and intersections of [[measure-theory/measurable-set|measurable sets]].
