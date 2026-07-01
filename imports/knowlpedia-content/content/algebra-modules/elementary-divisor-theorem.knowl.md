+++
id = "algebra-modules/elementary-divisor-theorem"
title = "Elementary divisor theorem"
kind = "knowl"
summary = "Over a PID, a finitely generated module decomposes into primary cyclic summands."
aliases = ["elementary-divisor-theorem", "Elementary divisor theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/elementary-divisor-theorem.md"
+++

**Elementary divisor theorem**: Let \(R\) be a [[algebra-rings/pid|PID]] and let \(M\) be a finitely generated \(R\)-module. Then there exist \(r\ge 0\) and a finite multiset of prime powers \(\{p_i^{e_i}\}\subset R\) such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_i R/(p_i^{e_i}),
\]
where each \(p_i\) is a prime element of \(R\). The multiset of prime power factors is unique up to associates and reordering.

This is equivalent to the invariant factor decomposition in the [[algebra-modules/structure-theorem-pid|structure theorem over a PID]] by factoring each invariant factor \(d_j\) into prime powers and regrouping into primary components. For \(R=\mathbb Z\), it recovers the primary decomposition in the [[algebra-modules/classification-fg-abelian-groups|classification of finitely generated abelian groups]]
