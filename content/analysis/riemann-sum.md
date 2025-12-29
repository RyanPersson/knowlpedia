---
title: "Riemann sum"
description: "A finite sum ∑ f(t_i)Δx_i associated to a tagged partition of [a,b]."
---

Let $f:[a,b]\to\mathbb{R}$ be bounded and let $(P,T)$ be a tagged partition with $P:a=x_0<\cdots<x_n=b$ and tags $t_i\in[x_{i-1},x_i]$. The **Riemann sum** of $f$ for $(P,T)$ is
$$
S(f;P,T) := \sum_{i=1}^n f(t_i)\,(x_i-x_{i-1}).
$$

Riemann sums approximate the integral by sampling $f$ at finitely many points and weighting by interval lengths. The Riemann integral (when it exists) is the common limit of these sums as the mesh tends to $0$.

**Examples:**
- For $f(x)=x$ on $[0,1]$, using the uniform partition $x_i=i/n$ and right-endpoint tags gives
  $S=\sum_{i=1}^n \frac{i}{n}\cdot\frac{1}{n}=\frac{1}{n^2}\cdot\frac{n(n+1)}{2}\to \frac12.$
- If $f$ is constant $c$, then $S(f;P,T)=c(b-a)$ for every tagged partition.
- For discontinuous $f$, Riemann sums may depend strongly on the tags unless $f$ is integrable.
