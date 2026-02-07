---
title: "Field automorphism"
description: "A bijective field homomorphism; automorphisms fixing a base field form the Galois group."
---

Let \(L\) be a {{< knowl id="field" section="algebra-rings" text="field" >}}. A **field automorphism** of \(L\) is a bijective field homomorphism \(\sigma:L\to L\). The set \(\mathrm{Aut}(L)\) of all field automorphisms is a group under composition (an instance of {{< knowl id="automorphism-group" section="algebra-groups" text="automorphism group" >}}).

If \(L/K\) is a {{< knowl id="field-extension" text="field extension" >}}, a **\(K\)-automorphism** of \(L\) is a field automorphism \(\sigma\in\mathrm{Aut}(L)\) such that \(\sigma|_K=\mathrm{id}_K\). The group of all \(K\)-automorphisms is denoted \(\mathrm{Aut}_K(L)\), and when \(L/K\) is {{< knowl id="galois-extension" text="Galois" >}} it is the {{< knowl id="galois-group" text="Galois group" >}} \(\mathrm{Gal}(L/K)\).

Automorphisms are the “symmetries” that permute conjugates, and they control invariants such as {{< knowl id="fixed-field" text="fixed fields" >}}, {{< knowl id="trace-field" text="trace" >}}, and {{< knowl id="norm-field" text="norm" >}}.

### Examples
1. **Complex conjugation.** The map \(\sigma:\mathbb{C}\to\mathbb{C}\), \(\sigma(a+bi)=a-bi\), is a field automorphism. It is a \(\mathbb{R}\)-automorphism of \(\mathbb{C}/\mathbb{R}\).

2. **Quadratic extension.** For \(L=\mathbb{Q}(\sqrt{d})\), the map \(\sigma(a+b\sqrt{d})=a-b\sqrt{d}\) is a nontrivial \(\mathbb{Q}\)-automorphism. Thus \(\mathrm{Aut}_\mathbb{Q}(L)\cong C_2\).

3. **Finite fields and Frobenius.** If \(L=\mathbb{F}_{p^n}\) is a {{< knowl id="finite-field" text="finite field" >}}, then the {{< knowl id="frobenius-endomorphism" text="Frobenius map" >}} \(x\mapsto x^p\) is an automorphism of \(L\), and its powers generate \(\mathrm{Gal}(L/\mathbb{F}_p)\) (see {{< knowl id="finite-field-galois-group-cyclic" text="finite-field Galois groups are cyclic" >}}).
