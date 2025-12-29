---
title: "Class C^k map (ℝ^k→ℝ^m)"
description: "A map whose partial derivatives up to order k exist and are continuous."
---

Let $U\subseteq\mathbb{R}^k$ be open and let $f:U\to\mathbb{R}^m$ with components $f=(f_1,\dots,f_m)$. For an integer $r\ge 0$, write $\partial^\alpha$ for partial derivatives corresponding to a multi-index $\alpha=(\alpha_1,\dots,\alpha_k)\in\mathbb{N}^k$ with order $|\alpha|=\alpha_1+\cdots+\alpha_k$.

The map $f$ is of **class $C^r$** on $U$ if for every component $f_i$ and every multi-index $\alpha$ with $|\alpha|\le r$, the partial derivative $\partial^\alpha f_i$ exists on $U$ and is continuous on $U$.

Class $C^r$ regularity is the standard smoothness hypothesis in the inverse and implicit function theorems, Taylor's theorem in several variables, and the change-of-variables formula.

**Examples:**
- Any polynomial map is $C^r$ for every $r$.
- The map $f(x)=\|x\|_2$ on $\mathbb{R}^k$ is $C^1$ on $\mathbb{R}^k\setminus\{0\}$ but not differentiable at $0$.
- If all first partial derivatives of $f$ exist and are continuous on $U$, then $f$ is $C^1$ on $U$ and hence differentiable on $U$.
