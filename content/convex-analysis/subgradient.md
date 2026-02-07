---
title: "Subgradient"
description: "A vector that defines an affine global lower bound to a convex function at a point."
---

A **subgradient** of a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} $f$ at a point $x\in\operatorname{dom} f$ (see {{< knowl id="domain-and-epigraph-proper-function" text="domain" >}}) is a vector $g\in\mathbb{R}^n$ such that
$$
f(y)\ge f(x)+\langle g,\,y-x\rangle \quad \text{for all } y\in\mathbb{R}^n.
$$

Subgradients generalize derivatives: when $f$ is differentiable at $x$ (see {{< knowl id="derivative" section="real-analysis" text="derivative" >}}), the unique subgradient is $\nabla f(x)$. The set of all subgradients at $x$ is the {{< knowl id="subdifferential" text="subdifferential" >}} $\partial f(x)$, and each subgradient induces a {{< knowl id="supporting-hyperplane-convex-function" text="supporting hyperplane" >}} to the epigraph of $f$.

**Examples:**
- For $f(x)=|x|$ on $\mathbb{R}$, $\partial f(0)=[-1,1]$, so any $g\in[-1,1]$ is a subgradient at $0$.
- For $f(x)=\max\{x,0\}$ on $\mathbb{R}$, $\partial f(0)=[0,1]$, while $\partial f(x)=\{1\}$ for $x>0$ and $\partial f(x)=\{0\}$ for $x<0$.
