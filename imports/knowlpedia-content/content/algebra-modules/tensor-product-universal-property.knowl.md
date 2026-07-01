+++
id = "algebra-modules/tensor-product-universal-property"
title = "Universal property of the tensor product"
kind = "knowl"
summary = "Balanced bilinear maps out of M×N correspond to linear maps out of M⊗N."
aliases = ["tensor-product-universal-property", "Universal property of the tensor product"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/tensor-product-universal-property.md"
+++

The **universal property of the tensor product** says that for a right \(R\)-module \(M\) and a left \(R\)-module \(N\), a pair \((T,\tau)\) is a tensor product if \(\tau\colon M\times N\to T\) is a [[algebra-modules/bilinear-map|balanced bilinear map]] and for every abelian group \(A\) and every balanced bilinear map \(f\colon M\times N\to A\), there exists a unique group homomorphism \(\overline f\colon T\to A\) such that \(\overline f\circ\tau=f\).

When such \((T,\tau)\) exists, it is unique up to unique isomorphism; one writes \(T=M\otimes_R N\) and \(\tau(m,n)=m\otimes n\), producing the [[algebra-modules/tensor-product|tensor product]]. The universal property is the mechanism that turns bilinear constructions into linear ones (i.e. [[algebra-modules/module-homomorphism|module homomorphisms]], when the target has compatible structure).

**Examples:**
- The canonical pairing \(M\times R\to M\), \((m,r)\mapsto mr\), induces a natural isomorphism \(M\otimes_R R\cong M\).
- Any balanced bilinear pairing \(M\times N\to P\) factors uniquely as \(M\times N\to M\otimes_R N\to P\).
