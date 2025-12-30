---
title: "Galois Correspondence"
description: "For a finite Galois extension, intermediate fields correspond to subgroups of the Galois group."
---

**Theorem (Correspondence).**  
Let \(L/K\) be a finite {{</* knowl id="galois-extension" text="Galois extension" */>}} and set \(G=\mathrm{Gal}(L/K)\). There is an inclusion-reversing bijection
\[
H \le G \quad \longleftrightarrow \quad K \subseteq E \subseteq L
\]
given by
\[
H \mapsto L^H \quad \text{and} \quad E \mapsto \mathrm{Gal}(L/E),
\]
where \(L^H\) is the {{</* knowl id="fixed-field" text="fixed field" */>}} of \(H\).

This is the core bijection inside the {{</* knowl id="fundamental-theorem-galois-theory" text="fundamental theorem of Galois theory" */>}}.

**Examples.**
1. If \(G\cong C_2\), then its only subgroups are \(\{1\}\) and \(G\), so there are no nontrivial intermediate fields.
2. For \(L=\mathbb{F}_{p^6}\) over \(K=\mathbb{F}_p\), subgroups of the cyclic group of order \(6\) correspond to subfields \(\mathbb{F}_{p^d}\) for \(d\mid 6\).
3. For \(G=S_3\), the subgroup lattice (order \(1,2,3,6\)) predicts the possible intermediate degrees in the splitting field of an irreducible cubic.

**Related.** {{</* knowl id="galois-group" text="Galois groups" */>}}, {{</* knowl id="galois-degree-equals-group-order" text="degree/order formula" */>}}.
