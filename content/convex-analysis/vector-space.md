---
title: "Vector space"
description: "A set with addition and scalar multiplication satisfying the vector space axioms"
---

Let $X$ be a nonempty set and let $K$ be a field (in these notes, $K=\mathbb{R}$ or $K=\mathbb{C}$). Suppose we are given:

- an **addition** map $+:X\times X\to X$, $(x,y)\mapsto x+y$;
- a **scalar multiplication** map $\cdot:K\times X\to X$, $(\lambda,x)\mapsto \lambda x$.

Then $(X,+,\cdot)$ is a **vector space over $K$** if for all $x,y,z\in X$ and all $\alpha,\beta\in K$:

1. (Commutativity) $x+y=y+x$.
2. (Associativity) $(x+y)+z=x+(y+z)$.
3. (Zero) there exists $0\in X$ such that $x+0=x$.
4. (Additive inverses) for each $x\in X$ there exists $-x\in X$ such that $x+(-x)=0$.
5. (Distributivity over vectors) $\alpha(x+y)=\alpha x+\alpha y$.
6. (Distributivity over scalars) $(\alpha+\beta)x=\alpha x+\beta x$.
7. (Compatibility) $\alpha(\beta x)=(\alpha\beta)x$.
8. (Unit) $1x=x$.

Elements of $X$ are called **vectors**, and elements of $K$ are called **scalars**.

Vector spaces are the ambient setting for {{< knowl id="linear-combination" text="linear combinations" >}}, {{< knowl id="linear-subspace" text="linear subspaces" >}}, and {{< knowl id="linear-operator-linear-transformation" text="linear operators" >}}; adding a {{< knowl id="norm-normed-vector-space" text="norm" >}} yields a normed space.

**Examples:**
- $K^n$ with componentwise addition and scalar multiplication.
- The set of real polynomials on $\mathbb{R}$ with the usual operations.
- The set $F(\Omega)$ of all $K$-valued functions on a nonempty set $\Omega$, with $(f+g)(x)=f(x)+g(x)$ and $(\lambda f)(x)=\lambda f(x)$.
