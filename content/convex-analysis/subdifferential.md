---
title: "Subdifferential"
description: "The set of all subgradients of a convex function at a point, defined by global supporting inequalities."
---

A **subdifferential** of a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} $f:\mathbb{R}^n\to(-\infty,+\infty]$ at a point $x$ in its {{< knowl id="domain-and-epigraph-proper-function" text="effective domain" >}} is the set
$$
\partial f(x)
\;=\;
\bigl\{g\in\mathbb{R}^n:\ f(z)\ge f(x)+\langle g,\,z-x\rangle \text{ for all } z\in\mathbb{R}^n\bigr\}.
$$

Any $g\in\partial f(x)$ is called a {{< knowl id="subgradient" text="subgradient" >}} of $f$ at $x$.

Geometrically, $g\in\partial f(x)$ encodes a {{< knowl id="supporting-hyperplane-convex-function" text="supporting hyperplane" >}} to the epigraph of $f$ at $(x,f(x))$, with normal determined by $g$ (compare {{< knowl id="hyperplane" text="hyperplane" >}}). If $f$ is differentiable at $x$ (in the sense of the {{< knowl id="derivative" section="real-analysis" text="derivative" >}} / {{< knowl id="differentiable-map" section="real-analysis" text="differentiable map" >}}), then $\partial f(x)=\{\nabla f(x)\}$.

**Examples:**
- For $f(x)=|x|$ on $\mathbb{R}$, one has $\partial f(0)=[-1,1]$ and $\partial f(x)=\{\mathrm{sign}(x)\}$ for $x\ne 0$.
- If $f=\delta_C$ is the indicator of a closed convex set $C$, then $\partial f(x)$ consists of outward normal vectors to $C$ at $x$ (and is empty if $x\notin C$).
