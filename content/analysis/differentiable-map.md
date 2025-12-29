---
title: "Differentiable map (ℝ^k→ℝ^m)"
description: "A map f is differentiable if it has a Fréchet derivative at every point of its domain."
---

Let $U\subseteq\mathbb{R}^k$ be {{< knowl id="open-set" text="open" >}} and let $f:U\to\mathbb{R}^m$. The map $f$ is **differentiable on $U$** if it is differentiable at every point $a\in U$ in the {{< knowl id="total-derivative-frechet-derivative" text="Fréchet sense" >}}, i.e. if for each $a$ there exists a {{< knowl id="linear-map" text="linear map" >}} $Df(a):\mathbb{R}^k\to\mathbb{R}^m$ such that
$$
\lim_{h\to 0}\frac{\|f(a+h)-f(a)-Df(a)h\|_2}{\|h\|_2}=0.
$$

Differentiability in this sense is the correct multivariable analogue of {{< knowl id="differentiability-one-variable" text="one-variable differentiability" >}}. It implies {{< knowl id="continuity-at-a-point" text="continuity" >}} and yields the multivariable chain rule.

**Examples:**
- Any polynomial map $f:\mathbb{R}^k\to\mathbb{R}^m$ is differentiable on $\mathbb{R}^k$.
- If $f$ is $C^1$ on $U$ (continuous first partial derivatives), then $f$ is differentiable on $U$.
- The map $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=|x|$ is differentiable at points with $x\ne 0$, but not differentiable along the line $x=0$.
