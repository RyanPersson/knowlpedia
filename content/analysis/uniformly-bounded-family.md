---
title: "Uniformly bounded family"
description: "A family of functions bounded by a single constant on the whole domain"
---

Let $X$ be a set and let $\mathcal{F}\subseteq \mathbb{R}^X$ be a family of real-valued functions.

The family $\mathcal{F}$ is **uniformly bounded** if there exists $M<\infty$ such that
$
\forall f\in\mathcal{F}\ \forall x\in X:\ |f(x)|\le M.
$

Equivalently, writing the {{< knowl id="sup-norm" text="sup norm" >}} $\|f\|_\infty=\sup_{x\in X}|f(x)|$ (possibly $+\infty$), uniform boundedness is:
$
\sup_{f\in\mathcal{F}} \|f\|_\infty <\infty.
$

Uniform boundedness is stronger than {{< knowl id="pointwise-bounded-family" text="pointwise boundedness" >}}; the distinction is central in compactness criteria such as {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli" >}}.

**Examples:**
- On $X=[0,1]$, the family $\{f_n(x)=x^n\}$ is uniformly bounded by $1$.
- On $X=\mathbb{R}$, the family $\{f_n(x)=x/n\}$ is not uniformly bounded (the supremum over $x$ is infinite for each fixed $n$), even though it is pointwise bounded.
