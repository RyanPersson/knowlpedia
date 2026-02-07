---
title: "Expectation of a function of a random variable"
description: "Compute the expectation of a transformed random variable using the distribution of the original."
---

**Law of the unconscious statistician:** Let $X:\Omega\to S$ be a {{< knowl id="random-variable" text="random variable" >}} with {{< knowl id="distribution-law" text="distribution (law)" >}} $\mu_X$ on $(S,\mathcal S)$. If $g:S\to\mathbb R$ is {{< knowl id="measurable-function" section="measure-theory" text="measurable" >}} and $g(X)$ is integrable, then
$$
\mathbb E[g(X)] = \int_\Omega g(X(\omega))\,d\mathbb P(\omega) = \int_S g(x)\,\mu_X(dx).
$$

This identity lets you compute expectations by integrating against the distribution of $X$ rather than over the original {{< knowl id="probability-space" text="probability space" >}}. When $\mu_X$ has a density with respect to {{< knowl id="lebesgue-measure" section="measure-theory" text="Lebesgue measure" >}} (via the {{< knowl id="radon-nikodym-theorem" text="Radon–Nikodym theorem" >}}), the right-hand side becomes an ordinary integral of $g(x)$ against that density.
