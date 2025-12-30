---
title: "Primitive root of unity"
description: "A root of unity ζ with multiplicative order exactly n (i.e., ζ^n=1 but ζ^d≠1 for d<n)."
---

**Definition.** Let \(L\) be a field and let \(n\ge 1\). An element \(\zeta\in L^\times\) is an **n-th root of unity** if \(\zeta^n=1\). It is **primitive** if its multiplicative order is exactly \(n\), i.e.
\[
\zeta^n=1 \quad\text{and}\quad \zeta^d\neq 1 \text{ for every } 1\le d<n.
\]
Equivalently, \(\zeta\) generates the cyclic subgroup of all \(n\)-th roots of unity in \(L^\times\) (compare {{</* knowl id="cyclic-subgroup" text="cyclic subgroups" */>}} and {{</* knowl id="finite-field-multiplicative-group-cyclic" text="cyclicity of finite-field units" */>}}).

Primitive \(n\)-th roots are precisely the roots of the {{</* knowl id="cyclotomic-polynomial" text="cyclotomic polynomial" */>}} \(\Phi_n(x)\).

**See also.** {{</* knowl id="cyclotomic-extension" text="cyclotomic extension" */>}}, {{</* knowl id="order-divides-group-order" text="order divides group order" */>}}.

**Examples.**
1. In \(\mathbb{C}\), \(\zeta_n=e^{2\pi i/n}\) is a primitive \(n\)-th root of unity.
2. \(\zeta_3=\frac{-1+i\sqrt3}{2}\) is a primitive cube root of unity; it satisfies \(x^2+x+1=0\).
3. In a finite field \(\mathbb{F}_q\), an element of order \(n\) exists iff \(n\mid (q-1)\), since \(\mathbb{F}_q^\times\) is cyclic of order \(q-1\).
