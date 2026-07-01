+++
id = "algebra-fields-galois/perfect-field"
title = "Perfect field"
kind = "knowl"
summary = "A field for which every algebraic extension is separable."
aliases = ["perfect-field", "Perfect field"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/perfect-field.md"
+++

Let \(F\) be a [[algebra-rings/field|field]].

**Definition (perfect field).** The field \(F\) is *perfect* if every algebraic [[algebra-fields-galois/field-extension|field extension]] of \(F\) is a [[algebra-fields-galois/separable-extension|separable extension]].

There are standard equivalent characterizations:
- \(F\) is perfect iff every [[algebra-fields-galois/algebraic-element|algebraic element]] over \(F\) is a [[algebra-fields-galois/separable-element|separable element]].
- If \(\mathrm{char}(F)=0\), then \(F\) is perfect.
- If \(\mathrm{char}(F)=p>0\), then \(F\) is perfect iff the [[algebra-fields-galois/frobenius-endomorphism|Frobenius endomorphism]] \(\varphi:F\to F\), \(\varphi(a)=a^p\), is surjective (equivalently \(F=F^p\)).

Perfect fields are precisely the base fields over which “separable vs. algebraic” coincide: every algebraic extension automatically has no inseparable phenomena.

**Examples.**
1. \(\mathbb{Q}\), \(\mathbb{R}\), and \(\mathbb{C}\) are perfect because they have characteristic \(0\).
2. Every [[algebra-fields-galois/finite-field|finite field]] \(\mathbb{F}_{p^n}\) is perfect (in characteristic \(p\), Frobenius is automatically bijective on a finite set).
3. \(\mathbb{F}_p(t)\) is not perfect: Frobenius is not surjective since \(t\notin (\mathbb{F}_p(t))^p\). Equivalently, the extension \(\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)\) is [[algebra-fields-galois/inseparable-extension|inseparable]].
