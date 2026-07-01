+++
id = "algebra-modules/injective-module"
title = "Injective module"
kind = "knowl"
summary = "A module with the extension property against injective homomorphisms."
aliases = ["injective-module", "Injective module"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/injective-module.md"
+++

An **injective module** is a left [[algebra-modules/module|module]] \(E\) over a [[algebra-rings/ring|ring]] \(R\) such that for every injective [[algebra-modules/module-homomorphism|module homomorphism]] \(i\colon A\hookrightarrow B\) and every homomorphism \(f\colon A\to E\), there exists a homomorphism \(g\colon B\to E\) with \(g\circ i=f\).

Equivalently, the contravariant functor \(\mathrm{Hom}_R(-,E)\) is exact on [[algebra-modules/exact-sequence-modules|exact sequences]] (or, equivalently, \(\mathrm{Ext}^1_R(-,E)=0\)). Injective modules are the categorical dual of [[algebra-modules/projective-module|projective modules]], and they can be recognized by [[algebra-modules/baers-criterion|Baer’s criterion]] in many settings.

**Examples:**
- Over a [[algebra-rings/field|field]], every [[linear-algebra/vector-space|vector space]] is injective as a module.
- As a \(\mathbb Z\)-module, \(\mathbb Q/\mathbb Z\) is injective (more generally, divisible abelian groups are injective \(\mathbb Z\)-modules).
- If \(\{E_i\}_{i\in I}\) are injective \(R\)-modules, then \(\prod_{i\in I} E_i\) is injective.
