+++
id = "algebra-fields-galois/separability-towers"
title = "Separability in towers"
kind = "knowl"
summary = "Separability is stable under passing up and down a tower of fields."
aliases = ["separability-towers", "Separability in towers"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/separability-towers.md"
+++

Consider a [[algebra-fields-galois/tower-of-fields|tower of fields]] \(K\subseteq E\subseteq L\) with \(L/K\) algebraic. Separability behaves transitively:

**Theorem (tower property for separability).**
1. If \(L/K\) is a [[algebra-fields-galois/separable-extension|separable extension]], then both \(E/K\) and \(L/E\) are separable.
2. If \(E/K\) and \(L/E\) are separable, then \(L/K\) is separable.

Equivalently at the element level: if \(\alpha\in L\) is [[algebra-fields-galois/separable-element|separable over \(K\)]], then it is separable over \(E\); conversely, if every element of \(E\) is separable over \(K\) and every element of \(L\) is separable over \(E\), then every element of \(L\) is separable over \(K\).

This interacts cleanly with degree computations via the [[algebra-fields-galois/tower-law|tower law]] when the extensions are finite.

### Examples

1. **Quadratic towers over \(\mathbb{Q}\).**
   \(\mathbb{Q}\subseteq \mathbb{Q}(\sqrt2)\subseteq \mathbb{Q}(\sqrt2,\sqrt3)\) is a finite tower in characteristic \(0\), hence both steps and the composite are separable.

2. **Purely inseparable tower in characteristic \(p\).**
   Let \(K=\mathbb{F}_p(t)\), \(E=K(t^{1/p})\), \(L=K(t^{1/p^2})\). Then \(E/K\) and \(L/E\) are [[algebra-fields-galois/inseparable-extension|inseparable]], and therefore \(L/K\) is inseparable as well.

3. **Mixed situation.**
   If \(K\) is [[algebra-fields-galois/perfect-field|perfect]] (e.g. \(K=\mathbb{F}_p\) or \(K=\mathbb{Q}\)), then any finite \(E/K\) is separable (see [[algebra-fields-galois/finite-extension-perfect-separable|perfect implies separable]]); hence in a finite tower \(K\subseteq E\subseteq L\), separability of \(L/K\) is equivalent to separability of \(L/E\).
