+++
id = "convex-analysis/subdifferential"
title = "Subdifferential"
kind = "knowl"
summary = "The set of all subgradients of a convex function at a point, defined by global supporting inequalities."
aliases = ["subdifferential"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/subdifferential.md"
+++

A **subdifferential** of a [[convex-analysis/convex-function-via-epigraph|convex function]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ at a point $x$ in its [[convex-analysis/domain-and-epigraph-proper-function|effective domain]] is the set
$$
\partial f(x)
\;=\;
\bigl\{g\in\mathbb{R}^n:\ f(z)\ge f(x)+\langle g,\,z-x\rangle \text{ for all } z\in\mathbb{R}^n\bigr\}.
$$

Any $g\in\partial f(x)$ is called a [[convex-analysis/subgradient|subgradient]] of $f$ at $x$.

Geometrically, $g\in\partial f(x)$ encodes a [[convex-analysis/supporting-hyperplane-convex-function|supporting hyperplane]] to the epigraph of $f$ at $(x,f(x))$, with normal determined by $g$ (compare [[convex-analysis/hyperplane|hyperplane]]). If $f$ is differentiable at $x$ (in the sense of the [[real-analysis/derivative|derivative]] / [[real-analysis/differentiable-map|differentiable map]]), then $\partial f(x)=\{\nabla f(x)\}$.

**Examples:**
- For $f(x)=|x|$ on $\mathbb{R}$, one has $\partial f(0)=[-1,1]$ and $\partial f(x)=\{\mathrm{sign}(x)\}$ for $x\ne 0$.
- If $f=\delta_C$ is the indicator of a closed convex set $C$, then $\partial f(x)$ consists of outward normal vectors to $C$ at $x$ (and is empty if $x\notin C$).
