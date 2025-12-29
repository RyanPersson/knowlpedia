---
title: "Limit of a function at infinity"
description: "The value L that f(x) approaches as x→∞, defined by an ε–M condition."
---

Let $f:E\to\mathbb{R}$ (or $\mathbb{C}$) where $E\subseteq\mathbb{R}$ is unbounded above. We say
$$\lim_{x\to\infty} f(x)=L$$
if
$$\forall \varepsilon>0,\ \exists M\in\mathbb{R}\ \text{such that}\ \forall x\in E,\ \bigl(x>M \Rightarrow |f(x)-L|<\varepsilon\bigr).$$

Limits at infinity formalize the long-range behavior of functions and are used in asymptotics, improper integrals, and series tests.

**Examples:**
- $\lim_{x\to\infty} \frac{1}{x}=0$.
- $\lim_{x\to\infty} \frac{x}{x+1}=1$.
- $\lim_{x\to\infty} \sin x$ does not exist (oscillation).
