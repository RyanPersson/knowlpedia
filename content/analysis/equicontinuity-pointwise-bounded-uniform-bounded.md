---
title: "Equicontinuity + pointwise boundedness implies uniform boundedness on compact sets"
description: "On a compact domain, equicontinuity upgrades pointwise bounds to a global bound"
---

Let $(K,d)$ be a {{< knowl id="compact-set" text="compact" >}} {{< knowl id="metric-space" text="metric space" >}} and let $\mathcal{F}\subseteq C(K,\mathbb{R})$ be a family of {{< knowl id="continuous-function" text="continuous functions" >}}. Assume:
- $\mathcal{F}$ is {{< knowl id="equicontinuous-family" text="equicontinuous" >}} on $K$, and
- $\mathcal{F}$ is {{< knowl id="pointwise-bounded-family" text="pointwise bounded" >}} on $K$ (for each $x\in K$, $\sup_{f\in\mathcal{F}}|f(x)|<\infty$).

**Lemma**: Then $\mathcal{F}$ is {{< knowl id="uniformly-bounded-family" text="uniformly bounded" >}} on $K$; i.e., there exists $M<\infty$ such that
$
|f(x)|\le M\quad \text{for all } f\in\mathcal{F},\ x\in K.
$

This lemma is a standard step in the proof of the {{< knowl id="arzela-ascoli-theorem" text="Arzelà–Ascoli theorem" >}}.

**Proof sketch**:
Apply equicontinuity with $\varepsilon=1$: for each $x\in K$ there exists $\delta_x>0$ such that
$
d(x,y)<\delta_x \implies |f(y)-f(x)|<1 \quad \text{for all } f\in\mathcal{F}.
$
By pointwise boundedness at $x$, choose $M_x$ with $|f(x)|\le M_x$ for all $f\in\mathcal{F}$. Then for all $y\in {{< knowl id="open-ball" text="$B$" >}}(x,\delta_x)$ and all $f\in\mathcal{F}$,
$
|f(y)|\le |f(y)-f(x)|+|f(x)|<1+M_x.
$
The balls $\{B(x,\delta_x)\}_{x\in K}$ form an {{< knowl id="open-cover" text="open cover" >}} of $K$. Compactness gives a finite subcover $B(x_i,\delta_{x_i})$ for $i=1,\dots,N$. Let
$
M=\max_{1\le i\le N} (1+M_{x_i}),
$
which is finite. Then $|f(y)|\le M$ for all $y\in K$ and all $f\in\mathcal{F}$.
