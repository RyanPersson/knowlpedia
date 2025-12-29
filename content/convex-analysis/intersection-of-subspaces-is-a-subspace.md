---
title: "Intersections of subspaces"
description: "The intersection of any family of linear subspaces is a linear subspace"
---

**Proposition.**
Let $X$ be a vector space, and let $\{Y_\alpha\}_{\alpha\in I}$ be a family of {{< knowl id="linear-subspace" text="linear subspaces" >}} of $X$. Then
$$
Y:=\bigcap_{\alpha\in I} Y_\alpha
$$
is also a linear subspace of $X$.

**Proof sketch.** Each $Y_\alpha$ contains $0$, so $0\in Y$. If $x,y\in Y$, then $x,y\in Y_\alpha$ for every $\alpha$, hence $x+y\in Y_\alpha$ for every $\alpha$, so $x+y\in Y$. Similarly, if $\lambda\in K$ and $x\in Y$, then $\lambda x\in Y_\alpha$ for all $\alpha$, so $\lambda x\in Y$.

This fact underlies the definition of the {{< knowl id="subspace-generated-by-a-set-span" text="span" >}} as an intersection of all subspaces containing a set.
