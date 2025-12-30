---
title: "Tower Law (Degree Multiplicativity)"
description: "In a finite tower of field extensions, degrees multiply."
---

**Theorem (Tower Law).**  
Let \(K \subseteq L \subseteq M\) be a tower of fields. If \( [L:K] \) and \( [M:L] \) are finite, then \( [M:K] \) is finite and
\[
[M:K] = [M:L]\,[L:K].
\]
Equivalently, the {{</* knowl id="degree-of-extension" text="degree of an extension" */>}} is multiplicative in a {{</* knowl id="tower-of-fields" text="tower of fields" */>}}.

**Examples.**
1. \( \mathbb{Q} \subset \mathbb{Q}(\sqrt2) \subset \mathbb{Q}(\sqrt2,\sqrt3)\):  
   \([\,\mathbb{Q}(\sqrt2):\mathbb{Q}\,]=2\), \([\,\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}(\sqrt2)\,]=2\), so \([\,\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}\,]=4\).
2. Finite fields: \( \mathbb{F}_p \subset \mathbb{F}_{p^2} \subset \mathbb{F}_{p^6}\):  
   \([\,\mathbb{F}_{p^2}:\mathbb{F}_p\,]=2\), \([\,\mathbb{F}_{p^6}:\mathbb{F}_{p^2}\,]=3\), hence \([\,\mathbb{F}_{p^6}:\mathbb{F}_p\,]=6\).
3. If \(K \subseteq L\) and \(M=L\), then \([M:K]=[L:K]\cdot 1\).

**Related.** {{</* knowl id="field-extension" text="field extension" */>}}, {{</* knowl id="tower-law" text="tower law" */>}}.
