---
title: "Fixed field"
description: "For a group G of automorphisms of L, the subfield L^G fixed pointwise by every element of G."
---

**Definition.** Let \(L\) be a field and let \(G\le \mathrm{Aut}(L)\) be a subgroup of its {{</* knowl id="field-automorphism" text="field automorphism group" */>}}. The **fixed field** of \(G\) is
\[
L^G \;=\; \{\,x\in L : \sigma(x)=x \text{ for all } \sigma\in G\,\}.
\]
It is a subfield of \(L\). In {{</* knowl id="galois-extension" text="Galois" */>}} settings, fixed fields of subgroups are exactly the {{</* knowl id="intermediate-field" text="intermediate fields" */>}} (see {{</* knowl id="galois-correspondence" text="Galois correspondence" */>}} and {{</* knowl id="artins-theorem-fixed-fields" text="Artin's theorem on fixed fields" */>}}).

**See also.** {{</* knowl id="group-action" text="group action" */>}} (automorphisms act on field elements).

**Examples.**
1. If \(G=\langle\text{conjugation}\rangle\le \mathrm{Aut}(\mathbb{C})\), then \(\mathbb{C}^G=\mathbb{R}\).
2. For \(L=\mathbb{F}_{p^n}\) and \(G=\mathrm{Gal}(L/\mathbb{F}_p)\), one has \(L^G=\mathbb{F}_p\).
3. In \(L=\mathbb{Q}(\sqrt2)\), the full Galois group \(G\cong C_2\) fixes exactly \(\mathbb{Q}\): \(L^G=\mathbb{Q}\).
