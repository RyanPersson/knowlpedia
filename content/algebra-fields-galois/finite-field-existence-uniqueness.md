---
title: "Finite Fields: Existence and Uniqueness"
description: "For each prime power q = p^n, there is a unique (up to isomorphism) field with q elements."
---

**Theorem.**  
Let \(q=p^n\) be a prime power. Then:

1. (**Existence**) There exists a {{</* knowl id="finite-field" text="finite field" */>}} \(\mathbb{F}_q\) with exactly \(q\) elements (see {{</* knowl id="finite-field-existence" text="existence" */>}}).
2. (**Uniqueness**) Any two fields with \(q\) elements are isomorphic.

Moreover, \(\mathbb{F}_q\) can be realized as \( \mathbb{F}_p[t]/(g(t))\) for an irreducible \(g\) of degree \(n\), and also as the splitting field over \(\mathbb{F}_p\) of \(x^{q}-x\).

**Examples.**
1. \(\mathbb{F}_4 \cong \mathbb{F}_2[t]/(t^2+t+1)\).
2. \(\mathbb{F}_9 \cong \mathbb{F}_3[t]/(t^2+1)\) since \(t^2+1\) is irreducible over \(\mathbb{F}_3\).
3. \(\mathbb{F}_{8} \cong \mathbb{F}_2[t]/(t^3+t+1)\) (any irreducible cubic over \(\mathbb{F}_2\) works).

**Related.** {{</* knowl id="finite-field-galois-group-cyclic" text="Galois group of finite fields" */>}}, {{</* knowl id="finite-field-multiplicative-group-cyclic" text="cyclic multiplicative group" */>}}.
