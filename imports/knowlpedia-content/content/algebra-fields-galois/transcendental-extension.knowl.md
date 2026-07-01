+++
id = "algebra-fields-galois/transcendental-extension"
title = "Transcendental extension"
kind = "knowl"
summary = "An extension E/F that contains at least one element transcendental over F (i.e. is not algebraic)."
aliases = ["transcendental-extension", "Transcendental extension"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/transcendental-extension.md"
+++

A [[algebra-fields-galois/field-extension|field extension]] \(E/F\) is called a **transcendental extension** if it is not an [[algebra-fields-galois/algebraic-extension|algebraic extension]]. Equivalently, \(E/F\) is transcendental iff there exists some \(\alpha\in E\) that is a [[algebra-fields-galois/transcendental-element|transcendental element]] over \(F\).

Thus “transcendental” is an existence condition: it is enough for \(E\) to contain *one* transcendental element over \(F\). (Stronger notions such as “purely transcendental” impose additional structure, but are not part of the basic definition.)

### Examples
1. The rational function field \(F(t)\) is transcendental over \(F\): the element \(t\) is transcendental over \(F\), so \(F(t)/F\) is a [[algebra-fields-galois/simple-extension|simple]] transcendental extension.
2. \(\mathbb{C}/\mathbb{Q}\) is transcendental, since \(\mathbb{C}\) contains elements (e.g. \(\pi\)) that are transcendental over \(\mathbb{Q}\).
3. \(\mathbb{Q}(t,\sqrt2)/\mathbb{Q}\) is transcendental: it contains \(t\), which is transcendental over \(\mathbb{Q}\), even though \(\sqrt2\) is algebraic over \(\mathbb{Q}\).
