---
title: "Frobenius endomorphism"
description: "In characteristic p>0, the map Fr(x)=x^p is a ring homomorphism; on finite fields it is an automorphism."
---

**Definition.** Let \(K\) be a field of characteristic \(p>0\). The **Frobenius endomorphism** is the map
\[
\mathrm{Fr}:K\to K,\qquad \mathrm{Fr}(x)=x^p.
\]
It is a ring homomorphism because \((x+y)^p=x^p+y^p\) in characteristic \(p\). For fields it is always injective; it is surjective exactly when \(K\) is {{</* knowl id="perfect-field" text="perfect" */>}}.

On a finite field \(\mathbb{F}_{p^n}\), Frobenius is an automorphism and generates the {{</* knowl id="galois-group" text="Galois group" */>}} of \(\mathbb{F}_{p^n}/\mathbb{F}_p\).

**See also.** {{</* knowl id="field-automorphism" text="field automorphism" */>}}, {{</* knowl id="finite-field" text="finite field" */>}}.

**Examples.**
1. On \(\mathbb{F}_p\), Frobenius is the identity map since \(x^p=x\) for all \(x\in\mathbb{F}_p\).
2. On \(\mathbb{F}_{p^n}\), the automorphisms fixing \(\mathbb{F}_p\) are \(\mathrm{Fr}^k:x\mapsto x^{p^k}\) for \(k=0,\dots,n-1\).
3. On \(K=\mathbb{F}_p(t)\), Frobenius is not surjective: there is no element \(u\in K\) with \(u^p=t\).
