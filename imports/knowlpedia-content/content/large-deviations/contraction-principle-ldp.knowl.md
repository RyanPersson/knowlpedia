+++
id = "large-deviations/contraction-principle-ldp"
title = "Contraction principle"
kind = "knowl"
summary = "How a large deviation principle transfers through a continuous mapping."
aliases = ["contraction-principle-ldp", "Contraction principle"]
domains = ["large-deviations"]
legacy_source_path = "large-deviations/contraction-principle-ldp.md"
+++

**Contraction principle:** Let $(\mu_n)$ be [[probability/probability-measure|probability measures]] on a space $X$ that satisfy a [[large-deviations/large-deviation-principle|large deviation principle]] with speed $a_n\to\infty$ and [[large-deviations/rate-function|rate function]] $I\colon X\to[0,\infty]$. Let $f\colon X\to Y$ be continuous, and let $\nu_n=\mu_n\circ f^{-1}$ be the pushforward measures on $Y$. Then $(\nu_n)$ satisfies an LDP on $Y$ with the same speed $a_n$ and rate function
\[
J(y)=\inf\bigl\{ I(x)\,:\, x\in X,\ f(x)=y\bigr\},
\]
with the convention $\inf\varnothing=+\infty$.

In terms of [[probability/random-variable|random variables]], if $Z_n$ satisfies an LDP on $X$ and $Y_n=f(Z_n)$ with $f$ continuous, then $(Y_n)$ satisfies an LDP with rate obtained by minimizing $I$ over the fiber $\{x:f(x)=y\}$. This principle is routinely combined with [[large-deviations/sanovs-theorem|Sanov's theorem]] and [[large-deviations/cramers-theorem|Cramér's theorem]] to derive LDPs for many statistics.
