---
title: "Degree of a Finite Galois Extension Equals Group Order"
description: "For finite Galois L/K, the extension degree equals |Gal(L/K)|."
---

**Theorem.**  
If \(L/K\) is a finite {{</* knowl id="galois-extension" text="Galois extension" */>}}, then
\[
[L:K] = |\mathrm{Gal}(L/K)|.
\]
Equivalently, the {{</* knowl id="galois-group" text="Galois group" */>}} has size equal to the {{</* knowl id="degree-of-extension" text="degree" */>}}.

This is a key numerical input in the {{</* knowl id="fundamental-theorem-galois-theory" text="fundamental theorem of Galois theory" */>}}.

**Examples.**
1. \(\mathbb{Q}(\sqrt2)/\mathbb{Q}\) is Galois with group \(\{1,\sqrt2\mapsto-\sqrt2\}\), so \([L:K]=2=|G|\).
2. \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is Galois and \(|\mathrm{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p)|=n\) (see {{</* knowl id="finite-field-galois-group-cyclic" text="cyclicity of the finite-field Galois group" */>}}).
3. If \(L\) is the splitting field over \(\mathbb{Q}\) of an irreducible separable cubic with Galois group \(S_3\), then \([L:\mathbb{Q}]=6\).

**Related.** {{</* knowl id="separable-normal-galois" text="Galois ⇔ separable + normal" */>}}.
