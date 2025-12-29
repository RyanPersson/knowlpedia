---
title: "Equicontinuity"
description: "A family of functions is equicontinuous if a single δ(ε) works uniformly over the family."
---

Let $(X,d_X)$ and $(Y,d_Y)$ be {{< knowl id="metric-space" text="metric spaces" >}}, and let $\mathcal{F}$ be a family of functions $f:X\to Y$. The family $\mathcal{F}$ is **equicontinuous at a point** $x_0\in X$ if
$$\forall \varepsilon>0,\ \exists \delta>0\ \text{such that}\ \forall f\in\mathcal{F},\ \forall x\in X,\ \bigl(d_X(x,x_0)<\delta \Rightarrow d_Y(f(x),f(x_0))<\varepsilon\bigr).$$
It is **equicontinuous on $X$** if it is equicontinuous at every $x_0\in X$.

Equicontinuity is a {{< knowl id="compact-set" text="compactness" >}}-type condition for families of functions. Together with pointwise boundedness it leads to the Arzelà–Ascoli theorem ({{< knowl id="subsequence" text="subsequence" >}} compactness in $C(K)$ when $K$ is compact). Compare with {{< knowl id="uniform-continuity" text="uniform continuity" >}} for a single function.

**Examples:**
- If every $f\in\mathcal{F}$ is Lipschitz with a common constant $L$, then $\mathcal{F}$ is equicontinuous (take $\delta=\varepsilon/L$).
- The family $\{f_n(x)=x^n\}_{n\in\mathbb{N}}$ on $[0,1]$ is not equicontinuous at $x_0=1$.
- The family $\{f_n(x)=\sin(nx)\}_{n\in\mathbb{N}}$ is not equicontinuous on $\mathbb{R}$.
