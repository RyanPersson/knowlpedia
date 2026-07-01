+++
id = "algebra-fields-galois/fixed-field"
title = "Fixed field"
kind = "knowl"
summary = "The subfield consisting of elements fixed by every automorphism in a given group."
aliases = ["fixed-field", "Fixed field"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/fixed-field.md"
+++

Let \(E\) be a [[algebra-rings/field|field]], and let \(G\) be a set (typically a subgroup) of field automorphisms of \(E\).

**Definition (fixed field).** The *fixed field* of \(G\) is
\[
E^G \;=\; \{\, a\in E \mid \sigma(a)=a \text{ for every } \sigma\in G \,\}.
\]

Then \(E^G\) is a subfield of \(E\). Moreover, when \(G\) contains the identity (as it does for any subgroup), \(E^G\subseteq E\) is an [[algebra-fields-galois/intermediate-field|intermediate field]] for the extension \(E/E^G\).

Fixed fields are central to Galois theory: if \(E/F\) is a [[algebra-fields-galois/galois-extension|Galois extension]], then the [[algebra-fields-galois/galois-group|Galois group]] \(\mathrm{Gal}(E/F)\) has fixed field exactly \(F\), and subgroups \(H\le \mathrm{Gal}(E/F)\) correspond to intermediate fields via the [[algebra-fields-galois/galois-correspondence|Galois correspondence]]. For finite groups of automorphisms, [[algebra-fields-galois/artins-theorem-fixed-fields|Artin’s theorem on fixed fields]] describes \([E:E^G]\) and identifies \(\mathrm{Gal}(E/E^G)\) with \(G\).

**Examples.**
1. Let \(E=\mathbb{Q}(\sqrt2)\) and \(G=\mathrm{Gal}(E/\mathbb{Q})=\{1,\sigma\}\) with \(\sigma(\sqrt2)=-\sqrt2\). Then \(E^G=\mathbb{Q}\). At the other extreme, if \(G=\{1\}\) then \(E^G=E\).
2. Let \(E=\mathbb{C}\) and let \(G=\{1,\text{conj}\}\), where \(\text{conj}(a+bi)=a-bi\). Then \(E^G=\mathbb{R}\).
3. Let \(E=\mathbb{F}_{p^n}\) and let \(\mathrm{Frob}(x)=x^p\). If \(G=\langle \mathrm{Frob}^d\rangle\) (so \(d\mid n\)), then the fixed field is \(E^G=\mathbb{F}_{p^d}\).
