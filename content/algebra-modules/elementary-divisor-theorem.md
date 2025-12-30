---
title: "Elementary divisor theorem"
description: "Over a PID, a finitely generated module decomposes into primary cyclic summands."
---

**Elementary divisor theorem**: Let \(R\) be a {{< knowl id="pid" text="PID" >}} and let \(M\) be a finitely generated \(R\)-module. Then there exist \(r\ge 0\) and a finite multiset of prime powers \(\{p_i^{e_i}\}\subset R\) such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_i R/(p_i^{e_i}),
\]
where each \(p_i\) is a prime element of \(R\). The multiset of prime power factors is unique up to associates and reordering.

This is equivalent to the invariant factor decomposition in the {{< knowl id="structure-theorem-pid" text="structure theorem over a PID" >}} by factoring each invariant factor \(d_j\) into prime powers and regrouping into primary components. For \(R=\mathbb Z\), it recovers the primary decomposition in the {{< knowl id="classification-fg-abelian-groups" text="classification of finitely generated abelian groups" >}}

**Proof sketch** *(optional)*: Start from the invariant factor decomposition and use unique factorization in a PID to write each \(d_j\) as a product of prime powers. Show that \(R/(ab)\cong R/(a)\oplus R/(b)\) when \((a,b)=1\), then iterate and regroup by primes.
