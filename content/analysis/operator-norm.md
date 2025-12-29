---
title: "Operator norm"
description: "The norm of a linear map defined as the maximal expansion of unit vectors."
---

Let $(V,\|\cdot\|_V)$ and $(W,\|\cdot\|_W)$ be normed vector spaces over $\mathbb{F}$, and let $T:V\to W$ be linear. The **operator norm** (or **induced norm**) of $T$ is
$$
\|T\| := \sup\{\|T x\|_W : x\in V,\ \|x\|_V=1\}.
$$
Equivalently,
$$
\|T\| = \sup_{x\ne 0}\frac{\|Tx\|_W}{\|x\|_V}.
$$

The operator norm measures the largest factor by which $T$ can stretch vectors. It is fundamental in analysis because boundedness/continuity of linear maps between normed spaces is equivalently expressed by finiteness of $\|T\|$.

**Examples:**
- If $T:\mathbb{R}\to\mathbb{R}$ is $T(x)=ax$, then $\|T\|=|a|$ (with the usual absolute value norm).
- If $T:\mathbb{R}^k\to\mathbb{R}^k$ is the identity map, then $\|T\|=1$.
- If $T:\mathbb{R}^2\to\mathbb{R}^2$ is rotation by angle $\theta$, then $\|T\|=1$ (it preserves Euclidean length).
