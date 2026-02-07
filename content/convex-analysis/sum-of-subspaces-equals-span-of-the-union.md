---
title: "Sum of subspaces and span of the union"
description: "The sum of two subspaces is a subspace and equals the span of their union"
---

**Proposition.**
Let $M$ and $N$ be {{< knowl id="linear-subspace" text="linear subspaces" >}} of a vector space $X$. Define their sum using set addition:
$$
M+N:=\{m+n\mid m\in M,\ n\in N\}.
$$
Then:

1. $M+N$ is a linear subspace of $X$.
2. $M+N=\operatorname{span}(M\cup N)$.

**Proof sketch.** Closure of $M+N$ under addition and scalar multiplication follows from closure of $M$ and $N$ and the definitions of {{< knowl id="set-operations-sum-scalar-multiple-difference" text="set sum and scalar multiples" >}}. For (2), note that $M\cup N\subset M+N$ (since $0\in M$ and $0\in N$), so the span of $M\cup N$ is contained in $M+N$. Conversely, any subspace containing $M\cup N$ contains $M+N$, hence $M+N$ is contained in the span.
