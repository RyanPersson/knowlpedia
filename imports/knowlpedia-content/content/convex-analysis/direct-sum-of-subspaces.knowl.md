+++
id = "convex-analysis/direct-sum-of-subspaces"
title = "Direct sum of subspaces"
kind = "knowl"
summary = "A sum of subspaces with trivial intersection"
aliases = ["direct-sum-of-subspaces", "Direct sum of subspaces"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/direct-sum-of-subspaces.md"
+++

Let $X$ be a vector space and let $M,N$ be [[convex-analysis/linear-subspace|linear subspaces]].

Let $Y:=M+N$ be their (set) sum. We say that $Y$ is the **direct sum** of $M$ and $N$ if
$$
M\cap N=\{0\}.
$$
In this case we write
$$
Y=M\oplus N.
$$

Direct sums formalize "adding independent directions": if $M\cap N=\{0\}$, then no nonzero vector lies in both subspaces. The key structural property is uniqueness of decomposition, captured in [[convex-analysis/characterization-of-direct-sums|the direct sum characterization]].

**Examples:**
- In $\mathbb{R}^2$, let $M=\operatorname{span}\{(1,0)\}$ and $N=\operatorname{span}\{(0,1)\}$. Then $\mathbb{R}^2=M\oplus N$.
- In $\mathbb{R}^3$, the $xy$-plane and the $z$-axis form a direct sum: $\mathbb{R}^3=\mathbb{R}^2\times\{0\}\ \oplus\ \operatorname{span}\{(0,0,1)\}$.
- If $M=N\neq\{0\}$, then $M+N=M$ but $M\cap N=M\neq\{0\}$, so this is not a direct sum.
