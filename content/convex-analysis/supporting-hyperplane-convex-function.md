---
title: "Supporting hyperplane of a convex function"
description: "An affine function whose graph supports the epigraph of a convex function."
---

A **supporting hyperplane of a convex function** $f$ at a point $x\in\operatorname{dom} f$ (see {{< knowl id="domain-and-epigraph-proper-function" text="domain" >}}) is an affine function
$$
\ell(y)=f(x)+\langle g,\,y-x\rangle
$$

such that $\ell(y)\le f(y)$ for all $y\in\mathbb{R}^n$.

Equivalently, the graph $\{(y,t): t=\ell(y)\}$ is a {{< knowl id="hyperplane" text="hyperplane" >}} in $\mathbb{R}^{n+1}$ that supports the {{< knowl id="domain-and-epigraph-proper-function" text="epigraph" >}} of $f$ (a {{< knowl id="convex-set" text="convex set" >}} when $f$ is convex). Such supporting hyperplanes are in one-to-one correspondence with {{< knowl id="subgradient" text="subgradients" >}}: $g$ supports $f$ at $x$ exactly when $g\in\partial f(x)$ (see {{< knowl id="subdifferential" text="subdifferential" >}}).

**Examples:**
- For $f(x)=x^2$ on $\mathbb{R}$ and any $x_0$, the tangent line $\ell(x)=x_0^2+2x_0(x-x_0)$ is a supporting hyperplane at $x_0$.
- For $f(x)=|x|$ on $\mathbb{R}$ at $x=0$, every line $\ell(x)=gx$ with $g\in[-1,1]$ is a supporting hyperplane.
