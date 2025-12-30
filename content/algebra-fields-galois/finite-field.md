---
title: "Finite field"
description: "A field with finitely many elements; every finite field has size p^n for a prime p."
---

**Definition.** A **finite field** is a field with finitely many elements. Every finite field has cardinality \(q=p^n\) for some prime \(p\) and integer \(n\ge 1\), and (up to isomorphism) there is exactly one field \(\mathbb{F}_{q}\) of each such size (see {{< knowl id="finite-field-existence-uniqueness" text="existence and uniqueness of finite fields" >}}).

The multiplicative group \(\mathbb{F}_q^\times\) is cyclic (see {{< knowl id="finite-field-multiplicative-group-cyclic" text="finite field multiplicative group is cyclic" >}}), and \(\mathrm{char}(\mathbb{F}_q)=p\) (see {{< knowl id="characteristic-zero-or-prime" section="algebra-rings" text="characteristic" >}}).

**See also.** {{< knowl id="frobenius-endomorphism" text="Frobenius endomorphism" >}}, {{< knowl id="finite-field-galois-cyclic" text="finite field extensions are Galois cyclic" >}}.

**Examples.**
1. \(\mathbb{F}_p \cong \mathbb{Z}/p\mathbb{Z}\) for a prime \(p\).
2. \(\mathbb{F}_4 \cong \mathbb{F}_2[x]/(x^2+x+1)\) since \(x^2+x+1\) is irreducible over \(\mathbb{F}_2\).
3. \(\mathbb{F}_{p^n}\) is the splitting field over \(\mathbb{F}_p\) of \(x^{p^n}-x\).
