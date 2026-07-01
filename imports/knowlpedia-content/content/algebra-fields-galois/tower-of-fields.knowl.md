+++
id = "algebra-fields-galois/tower-of-fields"
title = "Tower of fields"
kind = "knowl"
summary = "A chain of field extensions F ⊆ K ⊆ E, used to analyze E/F in stages."
aliases = ["tower-of-fields", "Tower of fields"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/tower-of-fields.md"
+++

A **tower of fields** (or **tower of extensions**) is a chain of inclusions of fields
\[
F \subseteq K \subseteq E.
\]
Equivalently, it is a [[algebra-fields-galois/field-extension|field extension]] \(E/F\) together with an [[algebra-fields-galois/intermediate-field|intermediate field]] \(K\) between them. One often abbreviates this situation by writing \(E/K/F\).

If the degrees are finite, towers are governed by the [[algebra-fields-galois/tower-law|tower law]]:
\[
[E:F]=[E:K]\,[K:F].
\]
This allows one to compute or bound \([E:F]\) by passing through simpler intermediate steps.

### Examples
1. \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2)\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\) is a tower obtained by adjoining \(\sqrt2\) first, then \(\sqrt3\).
2. If \(m\mid n\), then \(\mathbb{F}_p\subseteq \mathbb{F}_{p^m}\subseteq \mathbb{F}_{p^n}\) is a tower of [[algebra-fields-galois/finite-field|finite fields]].
3. With \(t\) an indeterminate, \(\mathbb{Q}\subseteq \mathbb{Q}(t^2)\subseteq \mathbb{Q}(t)\) is a tower in which the top extension is [[algebra-fields-galois/transcendental-extension|transcendental]], but \(\mathbb{Q}(t)/\mathbb{Q}(t^2)\) has finite [[algebra-fields-galois/degree-of-extension|degree]] \(2\).
