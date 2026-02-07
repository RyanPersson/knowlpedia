---
title: "Normal extension"
description: "An algebraic extension in which every irreducible polynomial having one root splits completely."
---

Let \(K/F\) be an algebraic {{< knowl id="field-extension" text="field extension" >}}.

**Definition (normal extension).** The extension \(K/F\) is *normal* if for every irreducible polynomial \(p(x)\in F[x]\), the condition “\(p\) has a root in \(K\)” implies “\(p\) splits into linear factors in \(K[x]\)”.

There are several standard equivalent characterizations (assuming \(K/F\) is algebraic):
- Fix an {{< knowl id="algebraic-closure" text="algebraic closure" >}} \(\overline F\) containing \(K\). Then \(K/F\) is normal iff every \(F\)-{{< knowl id="field-embedding" text="embedding" >}} \(\sigma:K\hookrightarrow \overline F\) satisfies \(\sigma(K)=K\).
- \(K/F\) is normal iff \(K\) is the {{< knowl id="splitting-field" text="splitting field" >}} over \(F\) of some family of polynomials in \(F[x]\). If \(K/F\) is finite, it suffices to take a single polynomial.

Splitting fields are normal (see {{< knowl id="normality-splitting-field" text="normality of splitting fields" >}}). A normal extension need not be {{< knowl id="separable-extension" text="separable" >}}; when it is both normal and separable, it is {{< knowl id="galois-extension" text="Galois" >}}.

**Examples.**
1. \(\mathbb{Q}(\sqrt2)/\mathbb{Q}\) is normal: it is the splitting field of \(x^2-2\).
2. \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is not normal: the irreducible polynomial \(x^3-2\) has one root \(\sqrt[3]{2}\) in \(\mathbb{Q}(\sqrt[3]{2})\), but its other roots \(\zeta_3\sqrt[3]{2}\) and \(\zeta_3^2\sqrt[3]{2}\) are not in that field.
3. For finite fields, \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is normal: it is the splitting field of \(x^{p^n}-x\) over \(\mathbb{F}_p\).
