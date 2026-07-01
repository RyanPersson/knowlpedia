+++
id = "algebra-fields-galois/finite-extension-perfect-separable"
title = "Perfect fields and separability of finite extensions"
kind = "knowl"
summary = "Over a perfect field, every algebraic (hence every finite) extension is separable."
aliases = ["finite-extension-perfect-separable", "Perfect fields and separability of finite extensions"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/finite-extension-perfect-separable.md"
+++

A [[algebra-fields-galois/perfect-field|perfect field]] is a field \(K\) such that every algebraic extension of \(K\) is [[algebra-fields-galois/separable-extension|separable]]. The key consequence for field extensions is:

**Theorem.** If \(K\) is perfect and \(L/K\) is algebraic (in particular, if \(L/K\) is finite), then \(L/K\) is separable. Moreover, any algebraic extension \(L\) of a perfect field \(K\) is itself perfect.

This is especially useful combined with the [[algebra-fields-galois/separable-normal-galois|separable + normal = Galois]] criterion: over a perfect base field, to check that a finite extension is [[algebra-fields-galois/galois-extension|Galois]], it suffices to check [[algebra-fields-galois/normal-extension|normality]].

### Examples

1. **Characteristic \(0\).**
   Every field of characteristic \(0\) is perfect, so any finite extension of \(\mathbb{Q}\) (e.g. \(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}\)) is automatically separable.

2. **Finite fields.**
   Any finite field \(\mathbb{F}_{p^n}\) is perfect (see [[algebra-fields-galois/finite-fields-perfect|finite fields are perfect]]), hence any finite extension \(\mathbb{F}_{p^m}/\mathbb{F}_{p^n}\) is separable.

3. **A non-perfect base gives inseparability.**
   Let \(K=\mathbb{F}_p(t)\). Then \(K\) is not perfect, and \(L=K(t^{1/p})\) is a finite (degree \(p\)) [[algebra-fields-galois/field-extension|extension]] that is [[algebra-fields-galois/inseparable-extension|inseparable]] (its defining polynomial \(x^p-t\) has zero derivative; see [[algebra-fields-galois/separable-distinct-roots|separable iff distinct roots]]).
