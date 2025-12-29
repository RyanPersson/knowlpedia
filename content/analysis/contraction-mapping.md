---
title: "Contraction mapping"
description: "A self-map that strictly shrinks distances by a uniform factor <1"
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $T:X\to X$.

The map $T$ is a **contraction mapping** (or **contraction**) if there exists a constant $c\in[0,1)$ such that for all $x,y\in X$,
$
d\bigl(T(x),T(y)\bigr)\le c\,d(x,y).
$
The constant $c$ is called a **contraction constant**.

A contraction is a special case of a {{< knowl id="lipschitz-function" text="Lipschitz" >}} map: $T$ is Lipschitz with constant $L$ if $d(Tx,Ty)\le L d(x,y)$ for all $x,y$. Contractions are exactly Lipschitz maps with $L<1$.

Contractions are important because on {{< knowl id="complete-metric-space" text="complete metric spaces" >}} they have unique {{< knowl id="fixed-point" text="fixed points" >}} and the fixed point can be found by iteration ({{< knowl id="banach-fixed-point-theorem" text="Banach fixed point theorem" >}}).

**Examples:**
- On $\mathbb{R}$ with $d(x,y)=|x-y|$, the affine map $T(x)=ax+b$ is a contraction iff $|a|<1$, with contraction constant $c=|a|$.
- On $\mathbb{R}^k$, $T(x)=\tfrac12 x$ is a contraction with $c=\tfrac12$.
- The map $T(x)=x+1$ is Lipschitz with constant $1$ but is not a contraction (and it has no fixed point).
