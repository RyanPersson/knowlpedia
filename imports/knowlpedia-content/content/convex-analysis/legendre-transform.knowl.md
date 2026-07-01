+++
id = "convex-analysis/legendre-transform"
title = "Legendre transform"
kind = "knowl"
summary = "A smooth, strict-convex special case of convex conjugation defined via the gradient map."
aliases = ["legendre-transform", "Legendre transform"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/legendre-transform.md"
+++

A **Legendre transform** of a differentiable [[convex-analysis/strictly-convex-function|strictly convex function]] $f:U\to\mathbb{R}$ on an open convex set $U\subseteq\mathbb{R}^n$ is the function $f^{\mathcal L}$ defined on the set $\nabla f(U)\subseteq\mathbb{R}^n$ by
$$
f^{\mathcal L}(p) \;=\; \langle p,x\rangle - f(x)
\quad\text{where } p=\nabla f(x).
$$

Strict convexity ensures that for each $p\in\nabla f(U)$ there is a unique $x\in U$ with $p=\nabla f(x)$, so the value is well-defined.

The Legendre transform is the “attained” version of the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]] when $f$ is smooth enough that the supremum defining $f^*$ is achieved at the unique point with $p=\nabla f(x)$. It connects convex analysis with the [[real-analysis/derivative|derivative]] and [[real-analysis/differentiable-map|differentiable map]] through the gradient map $x\mapsto\nabla f(x)$.

**Examples:**
- If $f(x)=\tfrac12\|x\|_2^2$ on $\mathbb{R}^n$, then $\nabla f(x)=x$ and $f^{\mathcal L}(p)=\tfrac12\|p\|_2^2$.
- If $f(x)=e^x$ on $\mathbb{R}$, then $\nabla f(x)=e^x$ so $p>0$ and $f^{\mathcal L}(p)=p\log p - p$ on $(0,\infty)$.
