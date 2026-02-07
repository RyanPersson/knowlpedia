---
title: "Images and preimages of subspaces under linear maps"
description: "Linear maps send subspaces to subspaces and pull back subspaces to subspaces"
---

**Proposition.**
Let $T:X\to Y$ be a linear operator between vector spaces.

1. If $M\subset X$ is a {{< knowl id="linear-subspace" text="linear subspace" >}}, then $T(M)\subset Y$ is a linear subspace.
2. If $N\subset Y$ is a linear subspace, then the preimage
   $$
   T^{-1}(N):=\{x\in X\mid T(x)\in N\}
   $$

   is a linear subspace of $X$.

In particular, $\ker T$ and $\operatorname{im}T$ from {{< knowl id="image-and-kernel-linear-isomorphism" text="image/kernel" >}} are subspaces.

**Proof sketch.** For (1), use $T(m_1+m_2)=T(m_1)+T(m_2)$ and $T(\lambda m)=\lambda T(m)$ and closure of $M$. For (2), if $x_1,x_2\in T^{-1}(N)$ then $T(x_1+x_2)\in N$ by closure of $N$; similarly for scalars.
