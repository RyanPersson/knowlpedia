---
title: "Primitive root of unity"
description: "An element ζ with ζ^n = 1 whose multiplicative order is exactly n."
---

Let \(F\) be a {{< knowl id="field" section="algebra-rings" text="field" >}} and let \(\overline{F}\) be an {{< knowl id="algebraic-closure" text="algebraic closure" >}}. An element \(\zeta\in\overline{F}\) is an **\(n\)-th root of unity** if \(\zeta^n=1\). It is a **primitive \(n\)-th root of unity** if its multiplicative order is exactly \(n\), i.e.
\[
\zeta^n=1 \quad\text{and}\quad \zeta^d\ne 1 \text{ for every proper divisor } d\mid n.
\]
Equivalently, \(\zeta\) is primitive of order \(n\) if and only if it is a root of the {{< knowl id="cyclotomic-polynomial" text="cyclotomic polynomial" >}} \(\Phi_n(x)\).

When \(\mathrm{char}(F)\nmid n\), the polynomial \(x^n-1\) has distinct roots in \(\overline{F}\) (a separability phenomenon; compare {{< knowl id="separable-distinct-roots" text="distinct-root criterion" >}}), and the \(n\)-th roots of unity form a cyclic subgroup of \(\overline{F}^\times\). Adjoining a primitive \(n\)-th root produces the {{< knowl id="cyclotomic-extension" text="cyclotomic extension" >}} \(F(\zeta)/F\).

### Examples
1. **Complex numbers.** In \(\mathbb{C}\), \(\zeta_n=e^{2\pi i/n}\) is a primitive \(n\)-th root of unity, and all primitive \(n\)-th roots are \(\zeta_n^k\) with \(\gcd(k,n)=1\).

2. **Small orders.** Primitive 3rd roots of unity are the two nontrivial roots of \(x^2+x+1\), namely \(e^{2\pi i/3}\) and \(e^{4\pi i/3}\). Primitive 4th roots of unity are \(\pm i\).

3. **Finite fields.** If \(F=\mathbb{F}_q\) is a {{< knowl id="finite-field" text="finite field" >}}, then \(F^\times\) is cyclic of order \(q-1\) (see {{< knowl id="finite-field-multiplicative-group-cyclic" text="cyclic multiplicative group" >}}). Hence \(F\) contains a primitive \(n\)-th root of unity exactly when \(n\mid(q-1)\).
