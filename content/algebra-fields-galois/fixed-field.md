---
title: "Fixed field"
description: "The subfield consisting of elements fixed by every automorphism in a given group."
---

Let \(E\) be a {{< knowl id="field" section="algebra-rings" text="field" >}}, and let \(G\) be a set (typically a subgroup) of field automorphisms of \(E\).

**Definition (fixed field).** The *fixed field* of \(G\) is
\[
E^G \;=\; \{\, a\in E \mid \sigma(a)=a \text{ for every } \sigma\in G \,\}.
\]

Then \(E^G\) is a subfield of \(E\). Moreover, when \(G\) contains the identity (as it does for any subgroup), \(E^G\subseteq E\) is an {{< knowl id="intermediate-field" text="intermediate field" >}} for the extension \(E/E^G\).

Fixed fields are central to Galois theory: if \(E/F\) is a {{< knowl id="galois-extension" text="Galois extension" >}}, then the {{< knowl id="galois-group" text="Galois group" >}} \(\mathrm{Gal}(E/F)\) has fixed field exactly \(F\), and subgroups \(H\le \mathrm{Gal}(E/F)\) correspond to intermediate fields via the {{< knowl id="galois-correspondence" text="Galois correspondence" >}}. For finite groups of automorphisms, {{< knowl id="artins-theorem-fixed-fields" text="Artin’s theorem on fixed fields" >}} describes \([E:E^G]\) and identifies \(\mathrm{Gal}(E/E^G)\) with \(G\).

**Examples.**
1. Let \(E=\mathbb{Q}(\sqrt2)\) and \(G=\mathrm{Gal}(E/\mathbb{Q})=\{1,\sigma\}\) with \(\sigma(\sqrt2)=-\sqrt2\). Then \(E^G=\mathbb{Q}\). At the other extreme, if \(G=\{1\}\) then \(E^G=E\).
2. Let \(E=\mathbb{C}\) and let \(G=\{1,\text{conj}\}\), where \(\text{conj}(a+bi)=a-bi\). Then \(E^G=\mathbb{R}\).
3. Let \(E=\mathbb{F}_{p^n}\) and let \(\mathrm{Frob}(x)=x^p\). If \(G=\langle \mathrm{Frob}^d\rangle\) (so \(d\mid n\)), then the fixed field is \(E^G=\mathbb{F}_{p^d}\).
