+++
id = "measure-theory/continuity-from-above-measure"
title = "Continuity from above"
kind = "knowl"
summary = "For decreasing measurable sets, the measure of the intersection is the limit of the measures under a finiteness hypothesis."
aliases = ["continuity-from-above-measure", "Continuity from above"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/continuity-from-above-measure.md"
+++

**Continuity from above:** Let $(X,\Sigma,\mu)$ be a [[measure-theory/measure-space|measure space]] and let $E_1,E_2,\dots \in \Sigma$ satisfy
$$
E_1 \supseteq E_2 \supseteq E_3 \supseteq \cdots
\quad\text{and}\quad
\mu(E_1)<\infty.
$$
Then
$$
\mu\!\left(\bigcap_{n=1}^\infty E_n\right)=\lim_{n\to\infty}\mu(E_n).
$$

This complements [[measure-theory/continuity-from-below-measure|continuity from below]] and is a basic limiting property of a [[measure-theory/measure|measure]] that is used repeatedly in measure-theoretic arguments.
