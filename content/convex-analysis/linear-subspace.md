---
title: "Linear subspace"
description: "A subset closed under addition and scalar multiplication, forming a vector space in its own right"
---

Let $(X,+,\cdot)$ be a vector space over $K$, and let $Y\subset X$.

The set $Y$ is a **linear subspace** of $X$ if:

1. $0\in Y$,
2. $a+b\in Y$ for all $a,b\in Y$,
3. $\lambda a\in Y$ for all $\lambda\in K$ and $a\in Y$.

With the inherited operations, $Y$ is itself a {{< knowl id="vector-space" text="vector space" >}}, and many constructions in analysis arise as subspaces (kernels, images, function spaces, etc.). Subspaces are also the building blocks for {{< knowl id="quotient-vector-space-codimension" text="quotient spaces" >}} and {{< knowl id="direct-sum-of-subspaces" text="direct sums" >}}.

**Examples:**
- $\{0\}$ and $X$ are subspaces of $X$.
- In the space of all sequences $s$, the set $\ell^1=\{x=(x_n):\sum_{n=1}^\infty |x_n|<\infty\}$ is a subspace.
- In $F([a,b])$, the set $C[a,b]$ of continuous functions is a subspace.
