---
title: "Algebraic Interior (Core) and Linear Closure"
description: "Algebraic analogues of interior and closure for subsets of vector spaces"
---

Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$.

The **algebraic interior** (or **core**) of $\Omega$ is
$$
\operatorname{core}(\Omega):=\Big\{x\in\Omega \ \Big|\ \forall v\in X,\ \exists \delta>0\ \text{s.t.}\ x+tv\in\Omega\ \text{for all }|t|<\delta\Big\}.
$$

The **linear closure** of $\Omega$ is
$$
\operatorname{lin}(\Omega):=\Big\{x\in X\ \Big|\ \exists w\in\Omega \text{ with } [w,x)\subset \Omega\Big\},
$$
where $[w,x)$ denotes the half-open {{< knowl id="line-segments-in-a-vector-space" text="line segment" >}}
$$
[w,x):=\{\lambda w+(1-\lambda)x\mid \lambda\in(0,1]\}.
$$

When $X$ is a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and $\Omega$ is {{< knowl id="convex-set" text="convex" >}}, these sets satisfy the inclusions
$$
\operatorname{int}(\Omega)\subset \operatorname{core}(\Omega)\subset \Omega \subset \operatorname{lin}(\Omega)\subset \overline{\Omega},
$$
where $\operatorname{int}(\Omega)$ and $\overline{\Omega}$ are the usual {{< knowl id="interior-of-a-set" text="interior" >}} and {{< knowl id="closure-of-a-set" text="closure" >}}, respectively.

**Examples:**
- If $\Omega$ is an open ball in a normed space, then $\operatorname{core}(\Omega)=\Omega$.
- If $\Omega$ is a linear subspace $L$, then $\operatorname{core}(L)=L$ and $\operatorname{lin}(L)=L$.
