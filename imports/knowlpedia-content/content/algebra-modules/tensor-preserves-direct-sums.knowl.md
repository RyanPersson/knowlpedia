+++
id = "algebra-modules/tensor-preserves-direct-sums"
title = "Tensor product preserves direct sums"
kind = "knowl"
summary = "Tensoring with a fixed module distributes over arbitrary direct sums."
aliases = ["tensor-preserves-direct-sums", "Tensor product preserves direct sums"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-preserves-direct-sums.md"
+++

**Tensor product preserves direct sums**: Let $M$ be a right $R$-module and $\{N_i\}_{i\in I}$ a family of left $R$-modules. The canonical map
\[
M\otimes_R\Bigl(\bigoplus_{i\in I}N_i\Bigr)\longrightarrow \bigoplus_{i\in I}(M\otimes_R N_i)
\]
induced by the inclusions $N_i\to\bigoplus_{i\in I}N_i$ is an isomorphism. Likewise, for a family of right $R$-modules $\{M_i\}_{i\in I}$ and a left $R$-module $N$ there is a canonical isomorphism
\[
\Bigl(\bigoplus_{i\in I} M_i\Bigr)\otimes_R N \cong \bigoplus_{i\in I}(M_i\otimes_R N).
\]

This is a basic compatibility of the [[algebra-modules/tensor-product|tensor product]] with the [[algebra-modules/direct-sum-modules|direct sum]], and can be viewed as a special case of the [[algebra-modules/tensor-hom-adjunction|Tensor–Hom adjunction]].
