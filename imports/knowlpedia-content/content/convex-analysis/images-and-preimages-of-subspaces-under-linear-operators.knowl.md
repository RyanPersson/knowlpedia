+++
id = "convex-analysis/images-and-preimages-of-subspaces-under-linear-operators"
title = "Images and preimages of subspaces under linear maps"
kind = "knowl"
summary = "Linear maps send subspaces to subspaces and pull back subspaces to subspaces"
aliases = ["images-and-preimages-of-subspaces-under-linear-operators", "Images and preimages of subspaces under linear maps"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/images-and-preimages-of-subspaces-under-linear-operators.md"
+++

**Proposition.**
Let $T:X\to Y$ be a linear operator between vector spaces.

1. If $M\subset X$ is a [[convex-analysis/linear-subspace|linear subspace]], then $T(M)\subset Y$ is a linear subspace.
2. If $N\subset Y$ is a linear subspace, then the preimage
   $$
   T^{-1}(N):=\{x\in X\mid T(x)\in N\}
   $$

   is a linear subspace of $X$.

In particular, $\ker T$ and $\operatorname{im}T$ from [[convex-analysis/image-and-kernel-linear-isomorphism|image/kernel]] are subspaces.

**Proof sketch.** For (1), use $T(m_1+m_2)=T(m_1)+T(m_2)$ and $T(\lambda m)=\lambda T(m)$ and closure of $M$. For (2), if $x_1,x_2\in T^{-1}(N)$ then $T(x_1+x_2)\in N$ by closure of $N$; similarly for scalars.
