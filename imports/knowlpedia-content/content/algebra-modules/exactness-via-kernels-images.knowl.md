+++
id = "algebra-modules/exactness-via-kernels-images"
title = "Exactness via kernels and images"
kind = "knowl"
summary = "A sequence is exact at a term precisely when the incoming image equals the outgoing kernel."
aliases = ["exactness-via-kernels-images", "Exactness via kernels and images"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/exactness-via-kernels-images.md"
+++

**Exactness via kernels and images**: A sequence of $R$-modules and homomorphisms
\[
\cdots \longrightarrow M_{i-1}\xrightarrow{d_{i-1}} M_i \xrightarrow{d_i} M_{i+1}\longrightarrow \cdots
\]
is exact at $M_i$ if and only if $\operatorname{im}(d_{i-1})=\ker(d_i)$.

This rewrites [[algebra-modules/exact-sequence-modules|exactness]] purely in terms of [[algebra-modules/kernel-module|kernels]] and [[algebra-modules/image-module|images]], and is used constantly for [[algebra-modules/short-exact-sequence|short exact sequences]].
