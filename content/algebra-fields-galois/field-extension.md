---
title: "Field extension"
description: "An inclusion of fields F ⊆ E (written E/F) and the basic language used to study it."
---

Let \(F\) and \(E\) be {{< knowl id="field" section="algebra-rings" text="fields" >}}. A **field extension** of \(F\) is a pair \((E,\iota)\) where \(\iota:F\hookrightarrow E\) is an injective field homomorphism. In practice one identifies \(F\) with its image \(\iota(F)\subseteq E\), writes simply \(F\subseteq E\), and denotes the extension by \(E/F\).

If \(E/F\) is a field extension, any subfield \(K\) with \(F\subseteq K\subseteq E\) is an {{< knowl id="intermediate-field" text="intermediate field" >}}. Such a \(K\) produces a {{< knowl id="tower-of-fields" text="tower of fields" >}} \(F\subseteq K\subseteq E\). When \(E\) is finite-dimensional as an \(F\)-vector space, the {{< knowl id="degree-of-extension" text="degree" >}} \([E:F]\) is defined.

A map of extensions is typically expressed via a {{< knowl id="field-embedding" text="field embedding" >}} \(E\hookrightarrow E'\) that restricts to the identity on \(F\); a bijective embedding \(E\to E\) fixing \(F\) is a {{< knowl id="field-automorphism" text="field automorphism" >}} over \(F\).

### Examples
1. \(\mathbb{R}\subseteq \mathbb{C}\) is a field extension, often written \(\mathbb{C}/\mathbb{R}\).
2. \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt{2})\) is a field extension obtained by adjoining \(\sqrt{2}\).
3. For a prime \(p\) and \(n\ge 1\), \(\mathbb{F}_p \subseteq \mathbb{F}_{p^n}\) is a finite field extension (where \(\mathbb{F}_{p^n}\) is a {{< knowl id="finite-field" text="finite field" >}} of size \(p^n\)).
