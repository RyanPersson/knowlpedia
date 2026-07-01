+++
id = "convex-analysis/subgradient"
title = "Subgradient"
kind = "knowl"
summary = "A vector that defines an affine global lower bound to a convex function at a point."
aliases = ["subgradient"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/subgradient.md"
+++

A **subgradient** of a [[convex-analysis/convex-function-via-epigraph|convex function]] $f$ at a point $x\in\operatorname{dom} f$ (see [[convex-analysis/domain-and-epigraph-proper-function|domain]]) is a vector $g\in\mathbb{R}^n$ such that
$$
f(y)\ge f(x)+\langle g,\,y-x\rangle \quad \text{for all } y\in\mathbb{R}^n.
$$

Subgradients generalize derivatives: when $f$ is differentiable at $x$ (see [[real-analysis/derivative|derivative]]), the unique subgradient is $\nabla f(x)$. The set of all subgradients at $x$ is the [[convex-analysis/subdifferential|subdifferential]] $\partial f(x)$, and each subgradient induces a [[convex-analysis/supporting-hyperplane-convex-function|supporting hyperplane]] to the epigraph of $f$.

**Examples:**
- For $f(x)=|x|$ on $\mathbb{R}$, $\partial f(0)=[-1,1]$, so any $g\in[-1,1]$ is a subgradient at $0$.
- For $f(x)=\max\{x,0\}$ on $\mathbb{R}$, $\partial f(0)=[0,1]$, while $\partial f(x)=\{1\}$ for $x>0$ and $\partial f(x)=\{0\}$ for $x<0$.
