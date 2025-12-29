---
title: "Limit point (accumulation point, cluster point)"
description: "A point x such that every neighborhood of x contains a point of the set different from x."
---

Let $(X,d)$ be a {{< knowl id="metric-space" text="metric space" >}} and let $A\subseteq X$. A point $x\in X$ is a **limit point** (also called an **accumulation point** or **cluster point**) of $A$ if
$$\forall r>0,\ \bigl(B(x,r)\setminus\{x\}\bigr)\cap A \neq \varnothing$$
(see {{< knowl id="open-ball" text="open ball" >}}).

Limit points are the points that can be approached by elements of $A$ distinct from the point itself. They determine closedness (a set is {{< knowl id="closed-set" text="closed" >}} iff it contains all its limit points) and appear throughout analysis. Compare with {{< knowl id="isolated-point" text="isolated points" >}}.

**Examples:**
- In $\mathbb{R}$, every point of $[0,1]$ is a limit point of $(0,1)$; in particular, $0$ and $1$ are limit points of $(0,1)$.
- In $\mathbb{R}$, $0$ is a limit point of $\{1/n:n\in\mathbb{N}\}$.
- In $\mathbb{R}$, the set $\mathbb{Z}$ has no finite limit points (each integer is isolated).
