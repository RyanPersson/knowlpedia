---
title: "Algebraic Interior (Core)"
description: "The algebraic analogue of interior for subsets of vector spaces"
---

Let $X$ be a real {{< knowl id="vector-space" text="vector space" >}} and let $\Omega\subset X$.

The **algebraic interior** (or **core**) of $\Omega$ is
$$
\operatorname{core}(\Omega):=\Big\{x\in\Omega \ \Big|\ \forall v\in X,\ \exists \delta>0\ \text{s.t.}\ x+tv\in\Omega\ \text{for all }|t|<\delta\Big\}.
$$

Equivalently, $x\in\operatorname{core}(\Omega)$ iff for every direction $v\in X$, one can move a small amount from $x$ in the direction $v$ and remain in $\Omega$.

When $X$ is a {{< knowl id="norm-normed-vector-space" text="normed vector space" >}} and $\Omega$ is {{< knowl id="convex-set" text="convex" >}}, we have
$$
\operatorname{int}(\Omega)\subset \operatorname{core}(\Omega)\subset \Omega,
$$
where $\operatorname{int}(\Omega)$ is the usual {{< knowl id="interior-of-a-set" text="interior" >}}. See also {{< knowl id="linear-closure" text="linear closure" >}} for the dual notion.

**Examples:**
- If $\Omega$ is an open ball in a normed space, then $\operatorname{core}(\Omega)=\Omega$.
- If $\Omega$ is a linear subspace $L$, then $\operatorname{core}(L)=L$.
