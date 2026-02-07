---
title: "Linear Closure"
description: "The algebraic analogue of closure for subsets of vector spaces"
---

Let $X$ be a real {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $\Omega\subset X$.

The **linear closure** of $\Omega$ is
$$
\operatorname{lin}(\Omega):=\Big\{x\in X\ \Big|\ \exists w\in\Omega \text{ with } [w,x)\subset \Omega\Big\},
$$

where $[w,x)$ denotes the half-open {{< knowl id="line-segments-in-a-vector-space" text="line segment" >}}
$$
[w,x):=\{\lambda w+(1-\lambda)x\mid \lambda\in(0,1]\}.
$$

Equivalently, $x\in\operatorname{lin}(\Omega)$ iff there exists a point $w\in\Omega$ such that the entire segment from $w$ to $x$ (excluding $x$) lies in $\Omega$.

When $X$ is a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and $\Omega$ is {{< knowl id="convex-set" text="convex" >}}, we have
$$
\Omega \subset \operatorname{lin}(\Omega)\subset \overline{\Omega},
$$

where $\overline{\Omega}$ is the usual {{< knowl id="closure-of-a-set" text="closure" >}}. See also {{< knowl id="algebraic-interior-core" text="algebraic interior (core)" >}} for the dual notion.

**Examples:**
- If $\Omega$ is a linear subspace $L$, then $\operatorname{lin}(L)=L$.
