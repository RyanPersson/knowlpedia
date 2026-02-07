---
title: "Varadhan's lemma"
description: "Asymptotic evaluation of exponential integrals under a large deviation principle."
---

**Varadhan's lemma:** Let $X$ be a Polish space and let $(\mu_n)$ be {{< knowl id="probability-measure" section="probability" text="probability measures" >}} on $X$ that satisfy a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} with speed $a_n\to\infty$ and {{< knowl id="good-rate-function" text="good rate function" >}} $I\colon X\to[0,\infty]$. If $f\colon X\to\mathbb{R}$ is continuous and bounded above, then
\[
\lim_{n\to\infty}\frac{1}{a_n}\log \int_X \exp\bigl(a_n f(x)\bigr)\,\mu_n(dx)
= \sup_{x\in X}\bigl\{f(x)-I(x)\bigr\}.
\]

Taking $f=-\varphi$ yields the {{< knowl id="laplace-principle" text="Laplace principle" >}}. In many applications, the “goodness” of $I$ is obtained by combining an LDP with {{< knowl id="exponential-tightness" text="exponential tightness" >}}.
