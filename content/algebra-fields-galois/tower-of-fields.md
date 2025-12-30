---
title: "Tower of fields"
description: "A chain of field extensions K ⊆ F ⊆ L, used to compare degrees and structure."
---

**Definition.** A **tower of fields** is a chain of inclusions
\[
K \subseteq F \subseteq L
\]
where each inclusion is a {{< knowl id="field-extension" text="field extension" >}}. The middle field \(F\) is an {{< knowl id="intermediate-field" text="intermediate field" >}} of \(L/K\).

If the degrees are finite, the {{< knowl id="tower-law" text="tower law" >}} gives
\[
[L:K]=[L:F]\,[F:K].
\]

**See also.** {{< knowl id="degree-of-extension" text="degree of an extension" >}}, {{< knowl id="separability-towers" text="separability in towers" >}}.

**Examples.**
1. \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2)\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\) is a tower with \([\,\mathbb{Q}(\sqrt2):\mathbb{Q}\,]=2\).
2. \(\mathbb{F}_p \subseteq \mathbb{F}_{p^2} \subseteq \mathbb{F}_{p^6}\) is a tower of finite fields with degrees \(2\) and \(3\).
3. \(\mathbb{Q}\subseteq \mathbb{Q}(t)\subseteq \mathbb{Q}(t,\sqrt{t})\) is a tower where the bottom extension is transcendental and the top over the middle is algebraic of degree \(2\).
