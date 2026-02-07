---
title: "Continuity from above"
description: "For decreasing measurable sets, the measure of the intersection is the limit of the measures under a finiteness hypothesis."
---

**Continuity from above:** Let $(X,\Sigma,\mu)$ be a {{< knowl id="measure-space" text="measure space" >}} and let $E_1,E_2,\dots \in \Sigma$ satisfy
$$
E_1 \supseteq E_2 \supseteq E_3 \supseteq \cdots
\quad\text{and}\quad
\mu(E_1)<\infty.
$$
Then
$$
\mu\!\left(\bigcap_{n=1}^\infty E_n\right)=\lim_{n\to\infty}\mu(E_n).
$$

This complements {{< knowl id="continuity-from-below-measure" text="continuity from below" >}} and is a basic limiting property of a {{< knowl id="measure" text="measure" >}} that is used repeatedly in measure-theoretic arguments.
