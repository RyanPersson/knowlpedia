---
title: "Laplace principle"
description: "A variational limit for exponential integrals that encodes large-deviation behavior."
---

A **Laplace principle** for a sequence of {{< knowl id="probability-measure" section="probability" text="probability measures" >}} $(\mu_n)$ on a space $X$, with speed $a_n\to\infty$ and {{< knowl id="rate-function" text="rate function" >}} $I\colon X\to[0,\infty]$, is the statement that for every bounded continuous function $\varphi\colon X\to\mathbb{R}$,
\[
\lim_{n\to\infty}\frac{1}{a_n}\log \int_X \exp\bigl(-a_n\varphi(x)\bigr)\,\mu_n(dx)
= -\inf_{x\in X}\bigl\{\varphi(x)+I(x)\bigr\}.
\]

This is the Laplace-transform formulation of the {{< knowl id="large-deviation-principle" text="large deviation principle" >}}. Under standard hypotheses (for example, $X$ Polish and $(\mu_n)$ {{< knowl id="exponential-tightness" text="exponentially tight" >}}), the Laplace principle with a {{< knowl id="good-rate-function" text="good rate function" >}} is equivalent to an LDP with the same rate function.

**Examples:**
- By {{< knowl id="cramers-theorem" text="Cramér's theorem" >}}, the empirical mean of an {{< knowl id="iid-sequence" section="probability" text="i.i.d. sequence" >}} of real-valued {{< knowl id="random-variable" section="probability" text="random variables" >}} satisfies the Laplace principle with speed $n$ and rate given by the {{< knowl id="cramer-transform" text="Cramér transform" >}}.
- By {{< knowl id="sanovs-theorem" text="Sanov's theorem" >}}, the empirical measure of an i.i.d. sample satisfies the Laplace principle with speed $n$ and rate given by {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} with respect to the common law.
