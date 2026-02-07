---
title: "Contraction principle"
description: "How a large deviation principle transfers through a continuous mapping."
---

**Contraction principle:** Let $(\mu_n)$ be {{< knowl id="probability-measure" section="probability" text="probability measures" >}} on a space $X$ that satisfy a {{< knowl id="large-deviation-principle" text="large deviation principle" >}} with speed $a_n\to\infty$ and {{< knowl id="rate-function" text="rate function" >}} $I\colon X\to[0,\infty]$. Let $f\colon X\to Y$ be continuous, and let $\nu_n=\mu_n\circ f^{-1}$ be the pushforward measures on $Y$. Then $(\nu_n)$ satisfies an LDP on $Y$ with the same speed $a_n$ and rate function
\[
J(y)=\inf\bigl\{ I(x)\,:\, x\in X,\ f(x)=y\bigr\},
\]
with the convention $\inf\varnothing=+\infty$.

In terms of {{< knowl id="random-variable" section="probability" text="random variables" >}}, if $Z_n$ satisfies an LDP on $X$ and $Y_n=f(Z_n)$ with $f$ continuous, then $(Y_n)$ satisfies an LDP with rate obtained by minimizing $I$ over the fiber $\{x:f(x)=y\}$. This principle is routinely combined with {{< knowl id="sanovs-theorem" text="Sanov's theorem" >}} and {{< knowl id="cramers-theorem" text="Cramér's theorem" >}} to derive LDPs for many statistics.
