+++
id = "real-analysis/limit-point-accumulation-point-cluster-point"
title = "Limit point (accumulation point, cluster point)"
kind = "knowl"
summary = "A point x such that every neighborhood of x contains a point of the set different from x."
aliases = ["limit-point-accumulation-point-cluster-point", "Limit point (accumulation point, cluster point)"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/limit-point-accumulation-point-cluster-point.md"
+++

Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $A\subseteq X$. A point $x\in X$ is a **limit point** (also called an **accumulation point** or **cluster point**) of $A$ if
$$\forall r>0,\ \bigl(B(x,r)\setminus\{x\}\bigr)\cap A \neq \varnothing$$
(see [[topology/open-ball|open ball]]).

Limit points are the points that can be approached by elements of $A$ distinct from the point itself. They determine closedness (a set is [[topology/closed-set|closed]] iff it contains all its limit points) and appear throughout analysis. Compare with [[real-analysis/isolated-point|isolated points]].

**Examples:**
- In $\mathbb{R}$, every point of $[0,1]$ is a limit point of $(0,1)$; in particular, $0$ and $1$ are limit points of $(0,1)$.
- In $\mathbb{R}$, $0$ is a limit point of $\{1/n:n\in\mathbb{N}\}$.
- In $\mathbb{R}$, the set $\mathbb{Z}$ has no finite limit points (each integer is isolated).
