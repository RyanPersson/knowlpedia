---
title: "Normal extension"
description: "An algebraic extension in which irreducible polynomials with one root split completely."
---

**Definition.** Let \(L/K\) be an {{< knowl id="algebraic-extension" text="algebraic extension" >}}. The extension \(L/K\) is **normal** if every {{< knowl id="irreducible-polynomial" section="algebra-rings" text="irreducible" >}} polynomial \(f(x)\in K[x]\) that has at least one root in \(L\) actually **splits completely** into linear factors over \(L\).

Equivalently, \(L\) is a {{< knowl id="splitting-field" text="splitting field" >}} of some family of polynomials in \(K[x]\). (In many common situations, \(L\) is the splitting field of a single polynomial.)

**See also.** {{< knowl id="separable-extension" text="separable extension" >}}, {{< knowl id="galois-extension" text="Galois extension" >}}, {{< knowl id="normality-splitting-field" text="normality and splitting fields" >}}.

**Examples.**
1. \(\mathbb{Q}(\sqrt2)/\mathbb{Q}\) is normal: it is the splitting field of \(x^2-2\).
2. \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is **not** normal: \(x^3-2\) has a root \(\sqrt[3]{2}\) in the field, but does not split there.
3. \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is normal: it is the splitting field of \(x^{p^n}-x\) over \(\mathbb{F}_p\).
