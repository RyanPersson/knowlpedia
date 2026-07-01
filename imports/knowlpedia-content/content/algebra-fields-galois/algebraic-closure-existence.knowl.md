+++
id = "algebra-fields-galois/algebraic-closure-existence"
title = "Existence of algebraic closures"
kind = "knowl"
summary = "Every field admits an algebraic closure."
aliases = ["algebraic-closure-existence", "Existence of algebraic closures"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/algebraic-closure-existence.md"
+++

Let \(K\) be a [[algebra-rings/field|field]].

**Theorem (Existence of algebraic closure).** There exists a [[algebra-fields-galois/field-extension|field extension]] \(\overline{K}/K\) such that:
1. \(\overline{K}\) is algebraically closed (every nonconstant polynomial in \(\overline{K}[x]\) splits into linear factors), and
2. \(\overline{K}/K\) is an [[algebra-fields-galois/algebraic-extension|algebraic extension]] (equivalently, every element of \(\overline{K}\) is an [[algebra-fields-galois/algebraic-element|algebraic element]] over \(K\)).

Such an extension \(\overline{K}\) is called an [[algebra-fields-galois/algebraic-closure|algebraic closure]] of \(K\). A standard proof uses Zorn’s lemma (hence the [[shared-foundations/axiom-of-choice|axiom of choice]]) to build a maximal algebraic extension and then shows it must be algebraically closed.

Moreover, any two algebraic closures of \(K\) are \(K\)-isomorphic; see [[algebra-fields-galois/algebraic-closure-uniqueness|uniqueness of algebraic closures]].

### Examples
1. \(\mathbb{C}\) is an algebraic closure of \(\mathbb{R}\): it is algebraically closed, and \([\mathbb{C}:\mathbb{R}]=2\), so every complex number is algebraic over \(\mathbb{R}\).

2. The field \(\overline{\mathbb{Q}}\) of algebraic numbers (elements algebraic over \(\mathbb{Q}\)) is an algebraic closure of \(\mathbb{Q}\).

3. An algebraic closure of \(\mathbb{F}_p\) can be realized as the union
   \[
   \overline{\mathbb{F}_p}=\bigcup_{n\ge1}\mathbb{F}_{p^n}
   \]
   inside a fixed ambient algebraic closure. This viewpoint is compatible with the [[algebra-fields-galois/finite-field-existence-uniqueness|existence and uniqueness of finite fields]].
