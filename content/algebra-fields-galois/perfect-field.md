---
title: "Perfect field"
description: "A field K such that every algebraic extension of K is separable."
---

**Definition.** A field \(K\) is **perfect** if every {{< knowl id="algebraic-extension" text="algebraic extension" >}} \(L/K\) is {{< knowl id="separable-extension" text="separable" >}}.

Key characterizations:
- If \(\mathrm{char}(K)=0\), then \(K\) is perfect.
- If \(\mathrm{char}(K)=p>0\), then \(K\) is perfect iff the {{< knowl id="frobenius-endomorphism" text="Frobenius map" >}} \(x\mapsto x^p\) is surjective (equivalently, \(K^p=K\)).

**See also.** {{< knowl id="finite-fields-perfect" text="finite fields are perfect" >}}, {{< knowl id="inseparable-extension" text="inseparable extension" >}}.

**Examples.**
1. \(\mathbb{Q}\), \(\mathbb{R}\), and \(\mathbb{C}\) are perfect (characteristic \(0\)).
2. Every finite field \(\mathbb{F}_{p^n}\) is perfect.
3. \(\mathbb{F}_p(t)\) is **not** perfect: \(t\) is not a \(p\)-th power in \(\mathbb{F}_p(t)\), so Frobenius is not surjective.
