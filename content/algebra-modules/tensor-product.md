---
title: "Tensor product of modules"
description: "The universal recipient of balanced bilinear maps from a pair of modules."
---

The **tensor product of modules** of a right \(R\)-module \(M\) and a left \(R\)-module \(N\) (for a {{</* knowl id="ring" text="ring" */>}} \(R\)) is an abelian group \(M\otimes_R N\) equipped with a canonical {{</* knowl id="bilinear-map" text="balanced bilinear map" */>}} \(M\times N\to M\otimes_R N\), \((m,n)\mapsto m\otimes n\), satisfying the {{</* knowl id="tensor-product-universal-property" text="universal property" */>}}: every balanced bilinear map out of \(M\times N\) factors uniquely through a homomorphism out of \(M\otimes_R N\).

This construction is functorial in both variables and is central for “extension of scalars” and for measuring non-exactness via derived functors. Over commutative rings it specializes to the tensor product of left {{</* knowl id="module" text="modules" */>}}.

**Examples:**
- For abelian groups (i.e. \(\mathbb Z\)-modules), \(\mathbb Z/n\mathbb Z\otimes_{\mathbb Z}\mathbb Z/m\mathbb Z \cong \mathbb Z/\gcd(n,m)\mathbb Z\).
- For a {{</* knowl id="field" text="field" */>}} \(k\) and finite-dimensional {{</* knowl id="vector-space" text="vector spaces" */>}} \(V,W\), one has \(\dim_k(V\otimes_k W)=\dim_k(V)\dim_k(W)\).
- If \(R\) is commutative, \(I\) is an {{</* knowl id="ideal" text="ideal" */>}} of \(R\), and \(M\) is an \(R\)-module, then \((R/I)\otimes_R M \cong M/IM\) as a {{</* knowl id="quotient-module" text="quotient module" */>}}.
