---
title: "Separability in towers"
description: "Separability is stable under passing up and down a tower of fields."
---

Consider a {{< knowl id="tower-of-fields" text="tower of fields" >}} \(K\subseteq E\subseteq L\) with \(L/K\) algebraic. Separability behaves transitively:

**Theorem (tower property for separability).**
1. If \(L/K\) is a {{< knowl id="separable-extension" text="separable extension" >}}, then both \(E/K\) and \(L/E\) are separable.
2. If \(E/K\) and \(L/E\) are separable, then \(L/K\) is separable.

Equivalently at the element level: if \(\alpha\in L\) is {{< knowl id="separable-element" text="separable over \(K\)" >}}, then it is separable over \(E\); conversely, if every element of \(E\) is separable over \(K\) and every element of \(L\) is separable over \(E\), then every element of \(L\) is separable over \(K\).

This interacts cleanly with degree computations via the {{< knowl id="tower-law" text="tower law" >}} when the extensions are finite.

### Examples

1. **Quadratic towers over \(\mathbb{Q}\).**  
   \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2)\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\) is a finite tower in characteristic \(0\), hence both steps and the composite are separable.

2. **Purely inseparable tower in characteristic \(p\).**  
   Let \(K=\mathbb{F}_p(t)\), \(E=K(t^{1/p})\), \(L=K(t^{1/p^2})\). Then \(E/K\) and \(L/E\) are {{< knowl id="inseparable-extension" text="inseparable" >}}, and therefore \(L/K\) is inseparable as well.

3. **Mixed situation.**  
   If \(K\) is {{< knowl id="perfect-field" text="perfect" >}} (e.g. \(K=\mathbb{F}_p\) or \(K=\mathbb{Q}\)), then any finite \(E/K\) is separable (see {{< knowl id="finite-extension-perfect-separable" text="perfect implies separable" >}}); hence in a finite tower \(K\subseteq E\subseteq L\), separability of \(L/K\) is equivalent to separability of \(L/E\).
