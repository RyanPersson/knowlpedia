---
title: "Pushforward measure"
description: "The measure obtained by transporting a measure through a measurable map."
---

A **pushforward measure** transports a measure along a {{< knowl id="function" section="shared-foundations" text="function" >}}. Let $(X,\mathcal{A},\mu)$ be a {{< knowl id="measure-space" text="measure space" >}}, let $(Y,\mathcal{B})$ be a {{< knowl id="measurable-space" text="measurable space" >}}, and let $T:X\to Y$ be a {{< knowl id="measurable-function" text="measurable function" >}}. The **pushforward** of $\mu$ by $T$, denoted $T_\#\mu$ (also written $T_*\mu$), is the {{< knowl id="measure" text="measure" >}} on $(Y,\mathcal{B})$ defined by
$$
(T_\#\mu)(B)=\mu(T^{-1}(B)) \qquad \text{for all } B\in\mathcal{B}.
$$

Pushforward measures encode how $\mu$ “looks” after applying $T$ and are the natural language for the {{< knowl id="change-of-variables-pushforward" text="change-of-variables formula via pushforward" >}}. The definition measures subsets of $Y$ by pulling them back to $X$ and then measuring in $X$.

**Examples:**
- Let $\lambda$ be Lebesgue measure on $[0,1]$ and let $T(x)=x^2$. Then $\nu=T_\#\lambda$ satisfies $\nu([0,t])=\lambda([0,\sqrt{t}])=\sqrt{t}$ for $0\le t\le 1$, so $\nu$ has density $\frac{1}{2\sqrt{y}}$ with respect to Lebesgue measure on $(0,1]$.
- If $\pi_X:X\times Y\to X$ is the projection map and $\mu\otimes\nu$ is a {{< knowl id="product-measure" text="product measure" >}}, then for $A\in\mathcal{A}$ one has
  $$
  (\pi_X)_\#(\mu\otimes\nu)(A)=(\mu\otimes\nu)(A\times Y)=\mu(A)\nu(Y)
  $$

  whenever $\nu(Y)<\infty$; in particular, if $\nu$ is a probability measure then $(\pi_X)_\#(\mu\otimes\nu)=\mu$.
