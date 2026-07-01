+++
id = "measure-theory/pushforward-measure"
title = "Pushforward measure"
kind = "knowl"
summary = "The measure obtained by transporting a measure through a measurable map."
aliases = ["pushforward-measure", "Pushforward measure"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/pushforward-measure.md"
+++

A **pushforward measure** transports a measure along a [[shared-foundations/function|function]]. Let $(X,\mathcal{A},\mu)$ be a [[measure-theory/measure-space|measure space]], let $(Y,\mathcal{B})$ be a [[measure-theory/measurable-space|measurable space]], and let $T:X\to Y$ be a [[measure-theory/measurable-function|measurable function]]. The **pushforward** of $\mu$ by $T$, denoted $T_\#\mu$ (also written $T_*\mu$), is the [[measure-theory/measure|measure]] on $(Y,\mathcal{B})$ defined by
$$
(T_\#\mu)(B)=\mu(T^{-1}(B)) \qquad \text{for all } B\in\mathcal{B}.
$$

Pushforward measures encode how $\mu$ “looks” after applying $T$ and are the natural language for the [[measure-theory/change-of-variables-pushforward|change-of-variables formula via pushforward]]. The definition measures subsets of $Y$ by pulling them back to $X$ and then measuring in $X$.

**Examples:**
- Let $\lambda$ be Lebesgue measure on $[0,1]$ and let $T(x)=x^2$. Then $\nu=T_\#\lambda$ satisfies $\nu([0,t])=\lambda([0,\sqrt{t}])=\sqrt{t}$ for $0\le t\le 1$, so $\nu$ has density $\frac{1}{2\sqrt{y}}$ with respect to Lebesgue measure on $(0,1]$.
- If $\pi_X:X\times Y\to X$ is the projection map and $\mu\otimes\nu$ is a [[measure-theory/product-measure|product measure]], then for $A\in\mathcal{A}$ one has
  $$
  (\pi_X)_\#(\mu\otimes\nu)(A)=(\mu\otimes\nu)(A\times Y)=\mu(A)\nu(Y)
  $$

  whenever $\nu(Y)<\infty$; in particular, if $\nu$ is a probability measure then $(\pi_X)_\#(\mu\otimes\nu)=\mu$.
