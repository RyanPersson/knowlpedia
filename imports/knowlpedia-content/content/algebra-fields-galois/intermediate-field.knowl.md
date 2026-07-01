+++
id = "algebra-fields-galois/intermediate-field"
title = "Intermediate field"
kind = "knowl"
summary = "A subfield K with F ⊆ K ⊆ E inside a given field extension E/F."
aliases = ["intermediate-field", "Intermediate field"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/intermediate-field.md"
+++

Let \(E/F\) be a [[algebra-fields-galois/field-extension|field extension]]. An **intermediate field** (or **subextension**) of \(E/F\) is a field \(K\) such that
\[
F \subseteq K \subseteq E,
\]
where both inclusions are inclusions of fields. Equivalently, \(K\) is a subfield of \(E\) that contains \(F\).

Any intermediate field \(K\) determines a [[algebra-fields-galois/tower-of-fields|tower]]
\[
F \subseteq K \subseteq E.
\]
When the relevant degrees are finite, the [[algebra-fields-galois/tower-law|tower law]] relates \([E:F]\), \([E:K]\), and \([K:F]\). In the special case of a [[algebra-fields-galois/galois-extension|Galois extension]], intermediate fields are organized by the [[algebra-fields-galois/galois-correspondence|Galois correspondence]].

### Examples
1. In \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\), the fields
   \(\mathbb{Q}(\sqrt2)\), \(\mathbb{Q}(\sqrt3)\), and \(\mathbb{Q}(\sqrt6)\)
   are intermediate fields between \(\mathbb{Q}\) and \(\mathbb{Q}(\sqrt2,\sqrt3)\).
2. If \(m\mid n\), then \(\mathbb{F}_{p^m}\) is an intermediate field of \(\mathbb{F}_{p^n}/\mathbb{F}_p\); concretely,
   \[
   \mathbb{F}_p \subseteq \mathbb{F}_{p^m} \subseteq \mathbb{F}_{p^n}.
   \]
3. In \(\mathbb{Q}\subseteq \mathbb{Q}(t)\) (the rational function field in one indeterminate), the subfield \(\mathbb{Q}(t^2)\) is intermediate:
   \[
   \mathbb{Q} \subseteq \mathbb{Q}(t^2) \subseteq \mathbb{Q}(t).
   \]
