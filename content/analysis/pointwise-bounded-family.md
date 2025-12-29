---
title: "Pointwise bounded family"
description: "A family of functions whose values are bounded at each fixed point of the domain"
---

Let $X$ be a set, let $(Y,d_Y)$ be a {{< knowl id="metric-space" text="metric space" >}}, and let $\mathcal{F}$ be a family of functions $f:X\to Y$.

The family $\mathcal{F}$ is **pointwise bounded** if for every $x\in X$ the set of values
$
\mathcal{F}(x)=\{f(x): f\in\mathcal{F}\}\subseteq Y
$
is {{< knowl id="bounded-set" text="bounded" >}} in $Y$, meaning there exist $y_x\in Y$ and $M_x<\infty$ such that
$
d_Y\bigl(f(x),y_x\bigr)\le M_x\quad\text{for all } f\in\mathcal{F}.
$

For real-valued families $\mathcal{F}\subseteq \mathbb{R}^X$, this reduces to:
$
\forall x\in X\ \exists M_x<\infty\ \forall f\in\mathcal{F}:\ |f(x)|\le M_x.
$

Pointwise boundedness is a natural "local boundedness" hypothesis; on {{< knowl id="compact-set" text="compact" >}} domains, combined with {{< knowl id="equicontinuous-family" text="equicontinuity" >}} it often upgrades to {{< knowl id="uniformly-bounded-family" text="uniform boundedness" >}}.

**Examples:**
- If $\mathcal{F}=\{f_n\}$ with $f_n(x)=x/n$ on $X=\mathbb{R}$, then $\mathcal{F}$ is pointwise bounded (at each fixed $x$, $|x/n|\le |x|$).
- The family $f_n(x)=n$ on any nonempty $X$ is not pointwise bounded.
