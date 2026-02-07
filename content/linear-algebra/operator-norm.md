---
title: "Operator norm"
description: "Norm of a linear map defined by its maximal expansion of unit vectors."
---

An **operator norm** of a {{< knowl id="linear-map" text="linear map" >}} $T:V\to W$ between {{< knowl id="normed-vector-space" text="normed vector spaces" >}} $(V,\|\cdot\|_V)$ and $(W,\|\cdot\|_W)$ is the quantity
\[
\|T\|=\sup_{v\ne 0}\frac{\|T(v)\|_W}{\|v\|_V}=\sup_{\|v\|_V=1}\|T(v)\|_W,
\]
with the understanding that the supremum may be $+\infty$ in general. When $\|T\|<\infty$, one says $T$ is bounded.

For linear maps between normed spaces, finiteness of the operator norm is equivalent to being {{< knowl id="continuous-map" section="topology" text="continuous" >}}. The operator norm makes the collection of bounded linear maps into a normed vector space and specializes to a norm on {{< knowl id="linear-operator" text="linear operators" >}} when $V=W$.

**Examples:**
- If $T(v)=c\,v$ on a normed space, then $\|T\|=|c|$.
- For the projection $P(x,y)=(x,0)$ on $\mathbb{R}^2$ with the Euclidean norm, $\|P\|=1$.
- For a diagonal matrix $A=\operatorname{diag}(d_1,\dots,d_n)$ acting on $\mathbb{R}^n$ with the max norm, the induced operator norm is $\|A\|=\max_i |d_i|$.
