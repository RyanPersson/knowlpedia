+++
id = "algebra-modules/tensor-commutes-with-sums"
title = "Tensor commutes with direct limits and sums"
kind = "knowl"
summary = "Tensoring is a left adjoint, hence it preserves direct sums and filtered colimits."
aliases = ["tensor-commutes-with-sums", "Tensor commutes with direct limits and sums"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-commutes-with-sums.md"
+++

**Tensor commutes with direct limits and sums**: Fix a right $R$-module $M$. Then the functor $M\otimes_R -$ preserves all small colimits of left $R$-modules; in particular, for any family $\{N_i\}_{i\in I}$ the canonical map
\[
M\otimes_R\Bigl(\bigoplus_{i\in I}N_i\Bigr)\longrightarrow \bigoplus_{i\in I}(M\otimes_R N_i)
\]
is an isomorphism, and for any directed system $\{N_i\}$ the canonical map $\varinjlim_i(M\otimes_R N_i)\to M\otimes_R(\varinjlim_i N_i)$ is an isomorphism.

Formally this follows from the [[algebra-modules/tensor-hom-adjunction|Tensor–Hom adjunction]] (tensoring is a left adjoint), and the direct-sum case recovers [[algebra-modules/tensor-preserves-direct-sums|tensor product preserves direct sums]] for [[algebra-modules/direct-sum-modules|direct sums]].
