+++
id = "algebra-fields-galois/separable-normal-galois"
title = "Finite Galois extensions are separable and normal"
kind = "knowl"
summary = "A finite extension is Galois iff it is both separable and normal."
aliases = ["separable-normal-galois", "Finite Galois extensions are separable and normal"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/separable-normal-galois.md"
+++

Let \(K\subseteq L\) be a finite [[algebra-fields-galois/field-extension|field extension]]. Then:

**Theorem.** The following are equivalent:
1. \(L/K\) is a [[algebra-fields-galois/galois-extension|Galois extension]].
2. \(L/K\) is both [[algebra-fields-galois/separable-extension|separable]] and [[algebra-fields-galois/normal-extension|normal]].

Under these conditions, the extension degree equals the order of the [[algebra-fields-galois/galois-group|Galois group]]:
\[
[L:K] = |\mathrm{Gal}(L/K)|
\]
(cf. [[algebra-fields-galois/galois-degree-equals-group-order|degree equals group order]]).

Over a [[algebra-fields-galois/perfect-field|perfect field]], separability is automatic for finite extensions (see [[algebra-fields-galois/finite-extension-perfect-separable|perfect implies separable]]), so “finite Galois” is equivalent to “finite normal.”

### Examples

1. **Quadratic extensions over \(\mathbb{Q}\).**
   \(L=\mathbb{Q}(\sqrt2)\) is the splitting field of \(x^2-2\), hence normal (see [[algebra-fields-galois/normality-splitting-field|normality via splitting fields]]); characteristic \(0\) gives separability. Thus \(L/\mathbb{Q}\) is Galois with \(|\mathrm{Gal}(L/\mathbb{Q})|=2\).

2. **A separable but non-normal extension.**
   \(L=\mathbb{Q}(\sqrt[3]{2})\) is separable (char \(0\)) but not normal, so it is not Galois. Its normal closure is the splitting field \(\mathbb{Q}(\sqrt[3]{2},\zeta_3)\).

3. **A normal but inseparable extension (characteristic \(p\)).**
   Let \(K=\mathbb{F}_p(t)\) and \(L=K(t^{1/p})\). Then \(L/K\) is inseparable (its defining polynomial has zero derivative), hence not Galois even though purely inseparable extensions satisfy a strong form of “no new embeddings.” This illustrates why the separability hypothesis is essential.
