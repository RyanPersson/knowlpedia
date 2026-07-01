+++
id = "algebra-modules/tensor-product"
title = "Tensor product of modules"
kind = "knowl"
summary = "The universal recipient of balanced bilinear maps from a pair of modules."
aliases = ["tensor-product", "Tensor product of modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-product.md"
+++

The **tensor product of modules** of a right \(R\)-module \(M\) and a left \(R\)-module \(N\) (for a [[algebra-rings/ring|ring]] \(R\)) is an abelian group \(M\otimes_R N\) equipped with a canonical [[algebra-modules/bilinear-map|balanced bilinear map]] \(M\times N\to M\otimes_R N\), \((m,n)\mapsto m\otimes n\), satisfying the [[algebra-modules/tensor-product-universal-property|universal property]]: every balanced bilinear map out of \(M\times N\) factors uniquely through a homomorphism out of \(M\otimes_R N\).

This construction is functorial in both variables and is central for “extension of scalars” and for measuring non-exactness via derived functors. Over commutative rings it specializes to the tensor product of left [[algebra-modules/module|modules]].

**Examples:**
- For abelian groups (i.e. \(\mathbb Z\)-modules), \(\mathbb Z/n\mathbb Z\otimes_{\mathbb Z}\mathbb Z/m\mathbb Z \cong \mathbb Z/\gcd(n,m)\mathbb Z\).
- For a [[algebra-rings/field|field]] \(k\) and finite-dimensional [[linear-algebra/vector-space|vector spaces]] \(V,W\), one has \(\dim_k(V\otimes_k W)=\dim_k(V)\dim_k(W)\).
- If \(R\) is commutative, \(I\) is an [[algebra-rings/ideal|ideal]] of \(R\), and \(M\) is an \(R\)-module, then \((R/I)\otimes_R M \cong M/IM\) as a [[algebra-modules/quotient-module|quotient module]].
