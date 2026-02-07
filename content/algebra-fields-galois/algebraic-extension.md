---
title: "Algebraic extension"
description: "An extension E/F in which every element of E is algebraic over F."
---

A {{< knowl id="field-extension" text="field extension" >}} \(E/F\) is called an **algebraic extension** if every element \(\alpha\in E\) is an {{< knowl id="algebraic-element" text="algebraic element" >}} over \(F\); that is, for each \(\alpha\in E\) there exists a nonzero polynomial \(f(x)\in F[x]\) with \(f(\alpha)=0\).

Equivalently, \(E/F\) is algebraic iff for every \(\alpha\in E\), the simple subextension \(F(\alpha)/F\) (see {{< knowl id="simple-extension" text="simple extension" >}}) has finite {{< knowl id="degree-of-extension" text="degree" >}}. In particular, every finite extension \([E:F]<\infty\) is algebraic.

Algebraic extensions are the setting for splitting fields and Galois theory: for example, a {{< knowl id="galois-extension" text="Galois extension" >}} is an algebraic extension satisfying additional normality and separability conditions.

### Examples
1. \(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}\) is algebraic because \(\sqrt2\) and \(\sqrt3\) are algebraic over \(\mathbb{Q}\), and every element of \(\mathbb{Q}(\sqrt2,\sqrt3)\) is built from them using field operations.
2. The extension \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is algebraic (indeed finite), since \([\mathbb{F}_{p^n}:\mathbb{F}_p]=n\).
3. If \(\overline{\mathbb{Q}}\) denotes an {{< knowl id="algebraic-closure" text="algebraic closure" >}} of \(\mathbb{Q}\), then \(\overline{\mathbb{Q}}/\mathbb{Q}\) is algebraic by definition: its elements are precisely the complex numbers algebraic over \(\mathbb{Q}\).
