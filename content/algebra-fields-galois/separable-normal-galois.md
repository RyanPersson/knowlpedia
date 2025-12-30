---
title: "Separable + Normal ⇔ Galois (Finite Case)"
description: "A finite extension is Galois exactly when it is separable and normal."
---

**Theorem.**  
Let \(L/K\) be a finite extension. Then \(L/K\) is a {{</* knowl id="galois-extension" text="Galois extension" */>}} if and only if it is both:

- {{</* knowl id="separable-extension" text="separable" */>}}, and
- {{</* knowl id="normal-extension" text="normal" */>}}.

When these conditions hold, the {{</* knowl id="galois-group" text="Galois group" */>}} has order \(|\mathrm{Gal}(L/K)|=[L:K]\) (see {{</* knowl id="galois-degree-equals-group-order" text="degree equals group order" */>}}).

**Examples.**
1. \(\mathbb{Q}(\sqrt2)/\mathbb{Q}\) is separable (char \(0\)) and normal (splitting field of \(x^2-2\)), hence Galois.
2. \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is separable but not normal, hence not Galois.
3. \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is separable and normal (splitting field of \(x^{p^n}-x\)), hence Galois.

**Related.** {{</* knowl id="normality-splitting-field" text="normality via splitting fields" */>}}, {{</* knowl id="separable-distinct-roots" text="separability via distinct roots" */>}}.
