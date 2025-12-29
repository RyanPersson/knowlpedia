---
title: "Diameter"
description: "The supremum of distances between pairs of points in a set."
---

Let $(X,d)$ be a metric space and let $A\subseteq X$. The **diameter** of $A$ is
$$\operatorname{diam}(A):=\sup\{d(x,y): x,y\in A\}\in[0,\infty].$$
(If the set of distances is unbounded, the supremum is $+\infty$.)

Diameter measures the "size" of a set in terms of its maximal pairwise separation. It is used in compactness and completeness arguments (e.g., nested closed sets with diameters $\to 0$).

**Examples:**
- In $\mathbb{R}$, $\operatorname{diam}([a,b])=b-a$.
- In $\mathbb{R}^2$, the diameter of the closed unit disk $\overline{B}(0,1)$ is $2$.
- In $\mathbb{R}$, $\operatorname{diam}(\mathbb{Z})=+\infty$.
