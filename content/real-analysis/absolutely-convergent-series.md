---
title: "Absolutely convergent series"
description: "A series that converges after taking absolute values term-by-term."
---

An **absolutely convergent series** is a series $\sum_{n=1}^\infty a_n$ such that the series of absolute values $\sum_{n=1}^\infty |a_n|$ is a {{< knowl id="convergent-series" text="convergent series" >}}.

Absolute convergence is stronger than ordinary convergence: see {{< knowl id="absolute-convergence-implies-convergence" text="absolute convergence implies convergence" >}}. It also ensures stability under {{< knowl id="rearrangement-of-series" text="rearrangements" >}}, formalized by {{< knowl id="rearrangement-theorem-absolute" text="the rearrangement theorem for absolutely convergent series" >}}.

**Examples:**
- $\sum_{n=1}^\infty \frac{1}{n^2}$ is absolutely convergent.
- $\sum_{n=1}^\infty \frac{(-1)^n}{n^2}$ is absolutely convergent, since $\sum_{n=1}^\infty \left|\frac{(-1)^n}{n^2}\right|=\sum_{n=1}^\infty \frac{1}{n^2}$ converges.
