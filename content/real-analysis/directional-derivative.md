---
title: "Directional derivative"
description: "Rate of change of a function in a specified direction"
---

A **directional derivative** of a function $f:U\to \mathbb{R}$ (with $U\subseteq \mathbb{R}^n$) at a point $a\in U$ in the direction $v\in \mathbb{R}^n$ is the one-sided limit
$$
D_v f(a)=\lim_{t\to 0^+}\frac{f(a+tv)-f(a)}{t},
$$

when it exists (the limit uses a {{< knowl id="one-sided-limit" text="one-sided limit" >}} along the line through $a$ in direction $v$).

If $f$ is {{< knowl id="differentiable-map" text="differentiable" >}} at $a$ (as a map into $\mathbb{R}$), then $D_v f(a)$ exists for every $v$ and equals $Df(a)v$, where $Df(a)$ is the {{< knowl id="frechet-derivative" text="Fréchet derivative" >}}. For scalar functions, directional derivatives are encoded by the {{< knowl id="gradient" text="gradient" >}}.

**Examples:**
- If $f(x,y)=x^2+y^2$, then at $a=(1,0)$ and $v=(1,1)$,
  $$
  D_v f(a)=\lim_{t\to 0^+}\frac{(1+t)^2+t^2-1}{t}=2.
  $$

- For $f(x,y)=|x|$, one has $D_{(0,1)}f(0,0)=0$, while $D_{(1,0)}f(0,0)=1$ (one-sided).
