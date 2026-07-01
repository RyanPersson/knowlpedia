+++
id = "algebra-fields-galois/separable-extension"
title = "Separable extension"
kind = "knowl"
summary = "An algebraic extension in which every element is separable over the base field."
aliases = ["separable-extension", "Separable extension"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/separable-extension.md"
+++

Let \(K/F\) be an algebraic [[algebra-fields-galois/field-extension|field extension]].

**Definition (separable extension).** The extension \(K/F\) is *separable* if every element \(\alpha\in K\) is a [[algebra-fields-galois/separable-element|separable element]] over \(F\).

When \(K/F\) is finite, separability admits useful equivalent formulations. For example, if \(\overline F\) is an [[algebra-fields-galois/algebraic-closure|algebraic closure]] of \(F\), then \(K/F\) is separable iff there are exactly \([K:F]\) distinct \(F\)-[[algebra-fields-galois/field-embedding|embeddings]] \(K\hookrightarrow \overline F\). Separability behaves well in towers, as summarized in [[algebra-fields-galois/separability-towers|separability in towers]].

**Examples.**
1. Every algebraic extension of a characteristic \(0\) field is separable. In particular, \(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}\) is separable (even though it is not [[algebra-fields-galois/normal-extension|normal]]).
2. For finite fields, \(\mathbb{F}_{p^n}/\mathbb{F}_p\) is separable; in fact it is [[algebra-fields-galois/galois-extension|Galois]].
3. The extension \(\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)\) is not separable: the element \(t^{1/p}\) is not separable over \(\mathbb{F}_p(t)\).
