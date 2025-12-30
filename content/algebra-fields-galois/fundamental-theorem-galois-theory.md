---
title: "Fundamental Theorem of Galois Theory"
description: "Intermediate fields correspond to subgroups of the Galois group."
---

**Theorem (FTGT).**  
Let \(L/K\) be a finite {{</* knowl id="galois-extension" text="Galois extension" */>}} with {{</* knowl id="galois-group" text="Galois group" */>}} \(G=\mathrm{Gal}(L/K)\). There is an inclusion-reversing bijection
\[
\{\text{intermediate fields }K\subseteq E\subseteq L\}
\longleftrightarrow
\{\text{subgroups }H\le G\},
\]
given by
\[
E \mapsto \mathrm{Gal}(L/E), \qquad H \mapsto L^H := \{x\in L : \sigma(x)=x\ \forall\sigma\in H\},
\]
the {{</* knowl id="fixed-field" text="fixed field" */>}} of \(H\).

It satisfies:
- \([L:E]=|\,\mathrm{Gal}(L/E)\,|\) and \([E:K]=[G:\mathrm{Gal}(L/E)]\) (compare {{</* knowl id="galois-degree-equals-group-order" text="degree = group order" */>}}).
- \(E/K\) is Galois iff \(\mathrm{Gal}(L/E)\trianglelefteq G\), and then \(\mathrm{Gal}(E/K)\cong G/\mathrm{Gal}(L/E)\).

**Examples.**
1. \(L=\mathbb{Q}(\sqrt2)\), \(G\cong C_2\): subgroups are \(\{1\}\) and \(G\), corresponding to fields \(L\) and \(\mathbb{Q}\).
2. \(L=\mathbb{F}_{p^n}\) over \(K=\mathbb{F}_p\): \(G\) is cyclic of order \(n\) (see {{</* knowl id="finite-field-galois-group-cyclic" text="finite-field Galois groups" */>}}); subgroups correspond to subfields \(\mathbb{F}_{p^d}\) with \(d\mid n\).
3. For the splitting field of \(x^3-2\) over \(\mathbb{Q}\), \(G\cong S_3\); intermediate fields correspond to subgroups of \(S_3\).

**Related.** {{</* knowl id="galois-correspondence" text="Galois correspondence (core bijection)" */>}}, {{</* knowl id="artins-theorem-fixed-fields" text="Artin's theorem on fixed fields" */>}}.
