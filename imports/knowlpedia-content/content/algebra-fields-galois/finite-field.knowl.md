+++
id = "algebra-fields-galois/finite-field"
title = "Finite field"
kind = "knowl"
summary = "A field with finitely many elements; necessarily of size p^n and unique up to isomorphism for each p^n."
aliases = ["finite-field", "Finite field"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/finite-field.md"
+++

A **finite field** is a [[algebra-rings/field|field]] \(F\) with finite cardinality \(|F|<\infty\). Its [[algebra-rings/characteristic|characteristic]] is a prime \(p\), so \(F\) contains a copy of \(\mathbb{F}_p\), and \(F\) is a finite-dimensional [[algebra-fields-galois/field-extension|field extension]] of \(\mathbb{F}_p\). Consequently \(|F|=p^n\) where \(n=[F:\mathbb{F}_p]\) (see [[algebra-fields-galois/degree-of-extension|degree of an extension]]).

A fundamental classification statement is: for every prime power \(q=p^n\) there exists a finite field of order \(q\), and it is unique up to (noncanonical) isomorphism (see [[algebra-fields-galois/finite-field-existence-uniqueness|existence and uniqueness of finite fields]]). Moreover, the multiplicative group \(F^\times\) is cyclic (see [[algebra-fields-galois/finite-field-multiplicative-group-cyclic|finite-field multiplicative groups are cyclic]]), and the [[algebra-fields-galois/frobenius-endomorphism|Frobenius]] controls the Galois theory of \(F/\mathbb{F}_p\) (see [[algebra-fields-galois/finite-field-galois-group-cyclic|finite-field Galois groups are cyclic]]).

### Examples
1. **Prime fields.** For a prime \(p\), the field \(\mathbb{F}_p=\mathbb{Z}/p\mathbb{Z}\) has \(p\) elements.

2. **A field of order \(4\).** Let
\[
\mathbb{F}_4 \cong \mathbb{F}_2[t]/(t^2+t+1),
\]
since \(t^2+t+1\) is irreducible over \(\mathbb{F}_2\). Writing \(\alpha=t\bmod(t^2+t+1)\), one has \(\alpha^2=\alpha+1\) and every element is \(0,1,\alpha,\alpha+1\).

3. **A field of order \(9\).** Similarly,
\[
\mathbb{F}_9 \cong \mathbb{F}_3[u]/(u^2+1),
\]
because \(u^2+1\) has no root in \(\mathbb{F}_3\). Then \(u^2=-1\) and \(\mathbb{F}_9^\times\) is cyclic of order \(8\).
