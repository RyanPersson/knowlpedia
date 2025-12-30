---
title: "Artin's Theorem on Fixed Fields"
description: "A finite group of automorphisms gives a Galois extension of degree equal to the group order."
---

**Theorem (Artin).**  
Let \(L\) be a field and \(G\) a finite subgroup of {{< knowl id="field-automorphism" text="field automorphisms" >}} of \(L\). Let
\[
K := L^G = \{x\in L : \sigma(x)=x\ \forall\sigma\in G\}
\]
be the {{< knowl id="fixed-field" text="fixed field" >}}. Then:
1. \(L/K\) is a finite {{< knowl id="galois-extension" text="Galois extension" >}},
2. \(\mathrm{Gal}(L/K)=G\), and
3. \([L:K]=|G|\) (compare {{< knowl id="galois-degree-equals-group-order" text="degree equals group order" >}}).

A standard tool in the proof is the {{< knowl id="dedekind-independence-lemma" text="Dedekind independence lemma" >}}.

**Examples.**
1. \(L=\mathbb{C}\), \(G=\{1,\text{complex conjugation}\}\). Then \(L^G=\mathbb{R}\) and \([\mathbb{C}:\mathbb{R}]=2=|G|\).
2. \(L=\mathbb{F}_{p^n}\), \(G=\langle x\mapsto x^p\rangle\) has order \(n\). Then \(L^G=\mathbb{F}_p\).
3. Cyclotomic example: \(L=\mathbb{Q}(\zeta_m)\) with automorphisms \(\zeta_m\mapsto \zeta_m^a\) (\((a,m)=1\)); fixed fields correspond to subgroups of \((\mathbb{Z}/m\mathbb{Z})^\times\) via {{< knowl id="fundamental-theorem-galois-theory" text="FTGT" >}}.

**Related.** {{< knowl id="galois-group" text="Galois groups" >}}, {{< knowl id="finite-field-galois-cyclic" text="finite-field Galois extensions" >}}.
