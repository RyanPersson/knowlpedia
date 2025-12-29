---
title: "Direct sum of subspaces"
description: "A sum of subspaces with trivial intersection"
---

Let $X$ be a vector space and let $M,N$ be {{< knowl id="linear-subspace" text="linear subspaces" >}}.

Let $Y:=M+N$ be their (set) sum. We say that $Y$ is the **direct sum** of $M$ and $N$ if
$$
M\cap N=\{0\}.
$$
In this case we write
$$
Y=M\oplus N.
$$

Direct sums formalize "adding independent directions": if $M\cap N=\{0\}$, then no nonzero vector lies in both subspaces. The key structural property is uniqueness of decomposition, captured in {{< knowl id="characterization-of-direct-sums" text="the direct sum characterization" >}}.

**Examples:**
- In $\mathbb{R}^2$, let $M=\operatorname{span}\{(1,0)\}$ and $N=\operatorname{span}\{(0,1)\}$. Then $\mathbb{R}^2=M\oplus N$.
- In $\mathbb{R}^3$, the $xy$-plane and the $z$-axis form a direct sum: $\mathbb{R}^3=\mathbb{R}^2\times\{0\}\ \oplus\ \operatorname{span}\{(0,0,1)\}$.
- If $M=N\neq\{0\}$, then $M+N=M$ but $M\cap N=M\neq\{0\}$, so this is not a direct sum.
