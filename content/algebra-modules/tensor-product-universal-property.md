---
title: "Universal property of the tensor product"
description: "Balanced bilinear maps out of M×N correspond to linear maps out of M⊗N."
---

The **universal property of the tensor product** says that for a right \(R\)-module \(M\) and a left \(R\)-module \(N\), a pair \((T,\tau)\) is a tensor product if \(\tau\colon M\times N\to T\) is a {{</* knowl id="bilinear-map" text="balanced bilinear map" */>}} and for every abelian group \(A\) and every balanced bilinear map \(f\colon M\times N\to A\), there exists a unique group homomorphism \(\overline f\colon T\to A\) such that \(\overline f\circ\tau=f\).

When such \((T,\tau)\) exists, it is unique up to unique isomorphism; one writes \(T=M\otimes_R N\) and \(\tau(m,n)=m\otimes n\), producing the {{</* knowl id="tensor-product" text="tensor product" */>}}. The universal property is the mechanism that turns bilinear constructions into linear ones (i.e. {{</* knowl id="module-homomorphism" text="module homomorphisms" */>}}, when the target has compatible structure).

**Examples:**
- The canonical pairing \(M\times R\to M\), \((m,r)\mapsto mr\), induces a natural isomorphism \(M\otimes_R R\cong M\).
- Any balanced bilinear pairing \(M\times N\to P\) factors uniquely as \(M\times N\to M\otimes_R N\to P\).
