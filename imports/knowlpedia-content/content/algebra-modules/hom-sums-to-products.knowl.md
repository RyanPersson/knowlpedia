+++
id = "algebra-modules/hom-sums-to-products"
title = "Hom turns sums into products"
kind = "knowl"
summary = "Hom out of a direct sum canonically identifies with the product of Homs."
aliases = ["hom-sums-to-products", "Hom turns sums into products"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/hom-sums-to-products.md"
+++

**Hom turns sums into products**: Let $\{M_i\}_{i\in I}$ be a family of $R$-modules and let $N$ be an $R$-module. Restriction along the canonical maps $\iota_i:M_i\to \bigoplus_{i\in I}M_i$ induces a natural isomorphism
\[
\operatorname{Hom}_R\Bigl(\bigoplus_{i\in I} M_i,\,N\Bigr)\;\cong\;\prod_{i\in I}\operatorname{Hom}_R(M_i,N).
\]

This expresses the [[algebra-modules/hom-module|Hom functor]] as converting a [[algebra-modules/direct-sum-modules|direct sum]] in the source into a [[algebra-modules/direct-product-modules|direct product]] of hom-sets, complementing how [[algebra-modules/tensor-product|tensor product]] behaves with sums.
