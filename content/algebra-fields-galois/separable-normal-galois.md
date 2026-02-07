---
title: "Finite Galois extensions are separable and normal"
description: "A finite extension is Galois iff it is both separable and normal."
---

Let \(K\subseteq L\) be a finite {{< knowl id="field-extension" text="field extension" >}}. Then:

**Theorem.** The following are equivalent:
1. \(L/K\) is a {{< knowl id="galois-extension" text="Galois extension" >}}.
2. \(L/K\) is both {{< knowl id="separable-extension" text="separable" >}} and {{< knowl id="normal-extension" text="normal" >}}.

Under these conditions, the extension degree equals the order of the {{< knowl id="galois-group" text="Galois group" >}}:
\[
[L:K] = |\mathrm{Gal}(L/K)|
\]
(cf. {{< knowl id="galois-degree-equals-group-order" text="degree equals group order" >}}).

Over a {{< knowl id="perfect-field" text="perfect field" >}}, separability is automatic for finite extensions (see {{< knowl id="finite-extension-perfect-separable" text="perfect implies separable" >}}), so “finite Galois” is equivalent to “finite normal.”

### Examples

1. **Quadratic extensions over \(\mathbb{Q}\).**  
   \(L=\mathbb{Q}(\sqrt2)\) is the splitting field of \(x^2-2\), hence normal (see {{< knowl id="normality-splitting-field" text="normality via splitting fields" >}}); characteristic \(0\) gives separability. Thus \(L/\mathbb{Q}\) is Galois with \(|\mathrm{Gal}(L/\mathbb{Q})|=2\).

2. **A separable but non-normal extension.**  
   \(L=\mathbb{Q}(\sqrt[3]{2})\) is separable (char \(0\)) but not normal, so it is not Galois. Its normal closure is the splitting field \(\mathbb{Q}(\sqrt[3]{2},\zeta_3)\).

3. **A normal but inseparable extension (characteristic \(p\)).**  
   Let \(K=\mathbb{F}_p(t)\) and \(L=K(t^{1/p})\). Then \(L/K\) is inseparable (its defining polynomial has zero derivative), hence not Galois even though purely inseparable extensions satisfy a strong form of “no new embeddings.” This illustrates why the separability hypothesis is essential.
