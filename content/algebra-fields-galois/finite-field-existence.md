---
title: "Existence of Finite Fields"
description: "For every prime power q = p^n, there exists a field with q elements."
---

**Theorem (Existence).**  
Let \(q=p^n\) be a prime power. There exists a {{< knowl id="finite-field" text="finite field" >}} with \(q\) elements, denoted \(\mathbb{F}_q\).

One construction: choose an irreducible polynomial \(g(t)\in \mathbb{F}_p[t]\) of degree \(n\) and set
\[
\mathbb{F}_q \cong \mathbb{F}_p[t]/(g(t)).
\]
Uniqueness up to isomorphism is treated in {{< knowl id="finite-field-existence-uniqueness" text="existence and uniqueness" >}}.

**Examples.**
1. \(q=4\): take \(g(t)=t^2+t+1\in\mathbb{F}_2[t]\) (irreducible), so \(\mathbb{F}_4\cong \mathbb{F}_2[t]/(t^2+t+1)\).
2. \(q=9\): \(t^2+1\) is irreducible in \(\mathbb{F}_3[t]\), giving \(\mathbb{F}_9\cong \mathbb{F}_3[t]/(t^2+1)\).
3. \(q=p\): \(\mathbb{F}_p\cong \mathbb{Z}/p\mathbb{Z}\) is the {{< knowl id="prime-subfield" section="algebra-rings" text="prime field" >}} of characteristic \(p\).

**Related.** {{< knowl id="finite-field-galois-cyclic" text="finite-field extensions are cyclic Galois" >}}.
