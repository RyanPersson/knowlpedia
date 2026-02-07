---
title: "Finite field"
description: "A field with finitely many elements; necessarily of size p^n and unique up to isomorphism for each p^n."
---

A **finite field** is a {{< knowl id="field" section="algebra-rings" text="field" >}} \(F\) with finite cardinality \(|F|<\infty\). Its {{< knowl id="characteristic" section="algebra-rings" text="characteristic" >}} is a prime \(p\), so \(F\) contains a copy of \(\mathbb{F}_p\), and \(F\) is a finite-dimensional {{< knowl id="field-extension" text="field extension" >}} of \(\mathbb{F}_p\). Consequently \(|F|=p^n\) where \(n=[F:\mathbb{F}_p]\) (see {{< knowl id="degree-of-extension" text="degree of an extension" >}}).

A fundamental classification statement is: for every prime power \(q=p^n\) there exists a finite field of order \(q\), and it is unique up to (noncanonical) isomorphism (see {{< knowl id="finite-field-existence-uniqueness" text="existence and uniqueness of finite fields" >}}). Moreover, the multiplicative group \(F^\times\) is cyclic (see {{< knowl id="finite-field-multiplicative-group-cyclic" text="finite-field multiplicative groups are cyclic" >}}), and the {{< knowl id="frobenius-endomorphism" text="Frobenius" >}} controls the Galois theory of \(F/\mathbb{F}_p\) (see {{< knowl id="finite-field-galois-group-cyclic" text="finite-field Galois groups are cyclic" >}}).

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
