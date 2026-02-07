---
title: "Quotient vector space and codimension"
description: "A vector space of cosets modulo a subspace; its dimension defines codimension"
---

Let $X$ be a vector space over $K$, and let $Y\subset X$ be a {{< knowl id="linear-subspace" text="linear subspace" >}}.

Define a relation on $X$ by
$$
x\sim u \quad\Longleftrightarrow\quad x-u\in Y.
$$

This is an equivalence relation. The equivalence class of $x$ is denoted
$$
[x]=x+Y:=\{u\in X\mid u-x\in Y\}.
$$
The set of all equivalence classes is written
$$
X/Y:=\{x+Y\mid x\in X\}.
$$

Define operations on $X/Y$ by
$$
(x+Y)+(u+Y):=(x+u)+Y,\qquad \lambda(x+Y):=(\lambda x)+Y.
$$

These operations are well-defined (independent of representatives) and make $X/Y$ a vector space, called the **quotient vector space**.

The **codimension** of $Y$ in $X$ is defined by
$$
\operatorname{codim}(Y):=\dim(X/Y).
$$

**Examples:**
- If $Y=\{0\}$, then $X/Y\cong X$ via $x+\{0\}\mapsto x$.
- If $X=\mathbb{R}^2$ and $Y$ is the $x$-axis, then $X/Y$ is (linearly) isomorphic to $\mathbb{R}$.
- If $Y=X$, then $X/Y$ is the zero vector space.
