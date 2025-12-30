---
title: "Separable element"
description: "An algebraic element whose minimal polynomial has no repeated roots."
---

**Definition.** Let \(L/K\) be a {{< knowl id="field-extension" text="field extension" >}} and let \(\alpha\in L\) be {{< knowl id="algebraic-element" text="algebraic over K" >}}. The element \(\alpha\) is **separable over \(K\)** if its {{< knowl id="minimal-polynomial-field" section="algebra-rings" text="minimal polynomial" >}} \(m_\alpha(x)\in K[x]\) has **distinct roots** in a splitting field (equivalently, \(m_\alpha\) has no repeated root).

A standard criterion is: \(\alpha\) is separable iff \(\gcd(m_\alpha, m_\alpha')=1\) in \(K[x]\), where \(m_\alpha'\) is the formal derivative.

**See also.** {{< knowl id="separable-extension" text="separable extension" >}}, {{< knowl id="inseparable-extension" text="inseparable extension" >}}, {{< knowl id="separable-distinct-roots" text="separable ⇔ distinct roots" >}}.

**Examples.**
1. Over any field of characteristic \(0\) (e.g. \(\mathbb{Q}\)), every algebraic element is separable; in particular \(\sqrt2\) is separable over \(\mathbb{Q}\).
2. In \(\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)\), the element \(t^{1/p}\) is algebraic but **not** separable: its minimal polynomial is \(x^p-t\), which has repeated roots in characteristic \(p\).
3. Every element of a finite field \(\mathbb{F}_{p^n}\) is separable over \(\mathbb{F}_p\).
