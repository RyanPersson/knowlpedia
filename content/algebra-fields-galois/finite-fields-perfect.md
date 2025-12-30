---
title: "Finite Fields are Perfect"
description: "Every finite field is perfect; equivalently, Frobenius is an automorphism."
---

**Theorem.**  
Every {{< knowl id="finite-field" text="finite field" >}} \( \mathbb{F}_q \) is {{< knowl id="perfect-field" text="perfect" >}}. In characteristic \(p\), this is equivalent to the {{< knowl id="frobenius-endomorphism" text="Frobenius map" >}} \(x\mapsto x^p\) being an automorphism (i.e., bijective). Consequently, every algebraic extension of a finite field is {{< knowl id="separable-extension" text="separable" >}}.

**Examples.**
1. In \(\mathbb{F}_{p^n}\), the map \(x\mapsto x^p\) is injective because the field has no zero divisors, hence bijective because the set is finite.
2. The polynomial \(x^{p^n}-x\) has derivative \(-1\), so its roots in \(\mathbb{F}_{p^n}\) are all distinct (see {{< knowl id="separable-distinct-roots" text="distinct roots criterion" >}}).
3. Any finite extension \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is separable (an instance of {{< knowl id="finite-extension-perfect-separable" text="perfect base ⇒ separable" >}}).

**Related.** {{< knowl id="finite-field-galois-group-cyclic" text="Galois groups of finite fields" >}}.
