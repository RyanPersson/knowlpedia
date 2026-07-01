+++
id = "algebra-fields-galois/field-automorphism"
title = "Field automorphism"
kind = "knowl"
summary = "A bijective field homomorphism; automorphisms fixing a base field form the Galois group."
aliases = ["field-automorphism", "Field automorphism"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/field-automorphism.md"
+++

Let \(L\) be a [[algebra-rings/field|field]]. A **field automorphism** of \(L\) is a bijective field homomorphism \(\sigma:L\to L\). The set \(\mathrm{Aut}(L)\) of all field automorphisms is a group under composition (an instance of [[algebra-groups/automorphism-group|automorphism group]]).

If \(L/K\) is a [[algebra-fields-galois/field-extension|field extension]], a **\(K\)-automorphism** of \(L\) is a field automorphism \(\sigma\in\mathrm{Aut}(L)\) such that \(\sigma|_K=\mathrm{id}_K\). The group of all \(K\)-automorphisms is denoted \(\mathrm{Aut}_K(L)\), and when \(L/K\) is [[algebra-fields-galois/galois-extension|Galois]] it is the [[algebra-fields-galois/galois-group|Galois group]] \(\mathrm{Gal}(L/K)\).

Automorphisms are the “symmetries” that permute conjugates, and they control invariants such as [[algebra-fields-galois/fixed-field|fixed fields]], [[algebra-fields-galois/trace-field|trace]], and [[algebra-fields-galois/norm-field|norm]].

### Examples
1. **Complex conjugation.** The map \(\sigma:\mathbb{C}\to\mathbb{C}\), \(\sigma(a+bi)=a-bi\), is a field automorphism. It is a \(\mathbb{R}\)-automorphism of \(\mathbb{C}/\mathbb{R}\).

2. **Quadratic extension.** For \(L=\mathbb{Q}(\sqrt{d})\), the map \(\sigma(a+b\sqrt{d})=a-b\sqrt{d}\) is a nontrivial \(\mathbb{Q}\)-automorphism. Thus \(\mathrm{Aut}_\mathbb{Q}(L)\cong C_2\).

3. **Finite fields and Frobenius.** If \(L=\mathbb{F}_{p^n}\) is a [[algebra-fields-galois/finite-field|finite field]], then the [[algebra-fields-galois/frobenius-endomorphism|Frobenius map]] \(x\mapsto x^p\) is an automorphism of \(L\), and its powers generate \(\mathrm{Gal}(L/\mathbb{F}_p)\) (see [[algebra-fields-galois/finite-field-galois-group-cyclic|finite-field Galois groups are cyclic]]).
