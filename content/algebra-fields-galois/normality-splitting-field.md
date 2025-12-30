---
title: "Normal Extensions via Splitting Fields"
description: "A finite extension is normal iff it is the splitting field of some polynomials over the base."
---

**Theorem.**  
Let \(L/K\) be a finite extension. The following are equivalent:

1. \(L/K\) is a {{</* knowl id="normal-extension" text="normal extension" */>}}.
2. \(L\) is the {{</* knowl id="splitting-field" text="splitting field" */>}} over \(K\) of a set of polynomials in \(K[x]\) (equivalently, of one polynomial).
3. Every \(K\)-embedding \(L \hookrightarrow \overline{K}\) into an algebraic closure has image equal to \(L\).

Combined with separability, this characterizes Galois extensions (see {{</* knowl id="separable-normal-galois" text="separable + normal ⇔ Galois" */>}}).

**Examples.**
1. \(\mathbb{Q}(\sqrt2)/\mathbb{Q}\) is normal: it is the splitting field of \(x^2-2\).
2. \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is **not** normal: \(x^3-2\) does not split over \(\mathbb{Q}(\sqrt[3]{2})\).
3. \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is normal: it is the splitting field of \(x^{p^n}-x\) over \(\mathbb{F}_p\).

**Related.** {{</* knowl id="splitting-field-existence-uniqueness" text="splitting fields exist and are unique" */>}}.
