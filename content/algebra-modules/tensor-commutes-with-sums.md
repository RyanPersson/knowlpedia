---
title: "Tensor commutes with direct limits and sums"
description: "Tensoring is a left adjoint, hence it preserves direct sums and filtered colimits."
---

**Tensor commutes with direct limits and sums**: Fix a right $R$-module $M$. Then the functor $M\otimes_R -$ preserves all small colimits of left $R$-modules; in particular, for any family $\{N_i\}_{i\in I}$ the canonical map
\[
M\otimes_R\Bigl(\bigoplus_{i\in I}N_i\Bigr)\longrightarrow \bigoplus_{i\in I}(M\otimes_R N_i)
\]
is an isomorphism, and for any directed system $\{N_i\}$ the canonical map $\varinjlim_i(M\otimes_R N_i)\to M\otimes_R(\varinjlim_i N_i)$ is an isomorphism.

Formally this follows from the {{< knowl id="tensor-hom-adjunction" text="Tensor–Hom adjunction" >}} (tensoring is a left adjoint), and the direct-sum case recovers {{< knowl id="tensor-preserves-direct-sums" text="tensor product preserves direct sums" >}} for {{< knowl id="direct-sum-modules" text="direct sums" >}}.
