---
title: "Tower of fields"
description: "A chain of field extensions F ⊆ K ⊆ E, used to analyze E/F in stages."
---

A **tower of fields** (or **tower of extensions**) is a chain of inclusions of fields
\[
F \subseteq K \subseteq E.
\]
Equivalently, it is a {{< knowl id="field-extension" text="field extension" >}} \(E/F\) together with an {{< knowl id="intermediate-field" text="intermediate field" >}} \(K\) between them. One often abbreviates this situation by writing \(E/K/F\).

If the degrees are finite, towers are governed by the {{< knowl id="tower-law" text="tower law" >}}:
\[
[E:F]=[E:K]\,[K:F].
\]
This allows one to compute or bound \([E:F]\) by passing through simpler intermediate steps.

### Examples
1. \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2)\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\) is a tower obtained by adjoining \(\sqrt2\) first, then \(\sqrt3\).
2. If \(m\mid n\), then \(\mathbb{F}_p\subseteq \mathbb{F}_{p^m}\subseteq \mathbb{F}_{p^n}\) is a tower of {{< knowl id="finite-field" text="finite fields" >}}.
3. With \(t\) an indeterminate, \(\mathbb{Q}\subseteq \mathbb{Q}(t^2)\subseteq \mathbb{Q}(t)\) is a tower in which the top extension is {{< knowl id="transcendental-extension" text="transcendental" >}}, but \(\mathbb{Q}(t)/\mathbb{Q}(t^2)\) has finite {{< knowl id="degree-of-extension" text="degree" >}} \(2\).
