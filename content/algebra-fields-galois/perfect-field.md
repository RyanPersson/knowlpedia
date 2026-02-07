---
title: "Perfect field"
description: "A field for which every algebraic extension is separable."
---

Let \(F\) be a {{< knowl id="field" section="algebra-rings" text="field" >}}.

**Definition (perfect field).** The field \(F\) is *perfect* if every algebraic {{< knowl id="field-extension" text="field extension" >}} of \(F\) is a {{< knowl id="separable-extension" text="separable extension" >}}.

There are standard equivalent characterizations:
- \(F\) is perfect iff every {{< knowl id="algebraic-element" text="algebraic element" >}} over \(F\) is a {{< knowl id="separable-element" text="separable element" >}}.
- If \(\mathrm{char}(F)=0\), then \(F\) is perfect.
- If \(\mathrm{char}(F)=p>0\), then \(F\) is perfect iff the {{< knowl id="frobenius-endomorphism" text="Frobenius endomorphism" >}} \(\varphi:F\to F\), \(\varphi(a)=a^p\), is surjective (equivalently \(F=F^p\)).

Perfect fields are precisely the base fields over which “separable vs. algebraic” coincide: every algebraic extension automatically has no inseparable phenomena.

**Examples.**
1. \(\mathbb{Q}\), \(\mathbb{R}\), and \(\mathbb{C}\) are perfect because they have characteristic \(0\).
2. Every {{< knowl id="finite-field" text="finite field" >}} \(\mathbb{F}_{p^n}\) is perfect (in characteristic \(p\), Frobenius is automatically bijective on a finite set).
3. \(\mathbb{F}_p(t)\) is not perfect: Frobenius is not surjective since \(t\notin (\mathbb{F}_p(t))^p\). Equivalently, the extension \(\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)\) is {{< knowl id="inseparable-extension" text="inseparable" >}}.
