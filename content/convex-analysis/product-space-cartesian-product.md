---
title: "Product space"
description: "A Cartesian product of vector spaces with componentwise operations"
---

Let $X_1,\dots,X_m$ be vector spaces over the same field $K$. Their **Cartesian product**
$$
X:=X_1\times\cdots\times X_m
$$

becomes a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} over $K$ by defining, for $x=(x_1,\dots,x_m)$ and $y=(y_1,\dots,y_m)$ in $X$ and $\alpha\in K$,
$$
x+y:=(x_1+y_1,\dots,x_m+y_m),\qquad \alpha x:=(\alpha x_1,\dots,\alpha x_m).
$$

This vector space is called the **product space** (or **direct product**) of $X_1,\dots,X_m$.

**Examples:**
- $\mathbb{R}^n$ is the product of $n$ copies of $\mathbb{R}$.
- If $X=Y\times Z$, then the subsets $Y\times\{0\}$ and $\{0\}\times Z$ are subspaces whose sum is all of $X$.
- For function spaces, $C[a,b]\times C[a,b]$ is a product space of pairs of continuous functions.
