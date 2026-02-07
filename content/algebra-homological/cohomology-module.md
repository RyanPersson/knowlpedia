---
title: "Cohomology module"
description: "The nth cohomology H^n(C) = ker(d^n)/im(d^{n-1}) of a cochain complex of modules."
---

Let \(R\) be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and let
\[
\cdots \xrightarrow{d^{n-1}} C^n \xrightarrow{d^{n}} C^{n+1} \xrightarrow{d^{n+1}} \cdots
\]
be a {{< knowl id="cochain-complex" text="cochain complex" >}} of {{< knowl id="module" section="algebra-modules" text="R-modules" >}}, i.e. \(d^{n+1}\circ d^{n}=0\) for all \(n\).

The **\(n\)th cocycles** and **\(n\)th coboundaries** are
\[
Z^n(C^\bullet) := \ker(d^{n})\subseteq C^n,
\qquad
B^n(C^\bullet) := \operatorname{im}(d^{n-1})\subseteq C^n.
\]
Since \(d^{n}\circ d^{n-1}=0\), one has \(B^n(C^\bullet)\subseteq Z^n(C^\bullet)\). The **\(n\)th cohomology module** is
\[
H^n(C^\bullet) := Z^n(C^\bullet) / B^n(C^\bullet).
\]

A cochain complex is exact (as a sequence of modules) iff all its cohomology modules vanish; see {{< knowl id="exact-complex" text="exact complex" >}}.

## Examples

### Example 1: Two-term cochain complex over \(\mathbb Z\)
Let \(C^0=\mathbb Z\), \(C^1=\mathbb Z\), \(d^0=\times n\), and \(C^i=0\) otherwise. Then
\[
H^0(C^\bullet)=\ker(\times n)=0,\qquad
H^1(C^\bullet)=\operatorname{coker}(\times n)\cong \mathbb Z/n\mathbb Z.
\]

### Example 2: \(\mathrm{Ext}\) as cohomology (concrete computation)
Let \(R=\mathbb Z\). A {{< knowl id="projective-resolution" text="projective resolution" >}} of \(\mathbb Z/n\mathbb Z\) is
\[
0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0.
\]
Apply {{< knowl id="hom-module" section="algebra-modules" text="Hom" >}}\((-,\mathbb Z)\) to get a cochain complex
\[
0 \to \operatorname{Hom}(\mathbb Z,\mathbb Z)
\xrightarrow{\times n}
\operatorname{Hom}(\mathbb Z,\mathbb Z)\to 0,
\]
which identifies with
\[
0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to 0.
\]
Thus
\[
\mathrm{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z)
\;\cong\;
H^1(\operatorname{Hom}(P_\bullet,\mathbb Z))
\;\cong\;
\mathbb Z/n\mathbb Z.
\]
(See {{< knowl id="ext" text="Ext" >}}.)

### Example 3: Vanishing over a field
If \(k\) is a field and \(V,W\) are \(k\)-vector spaces, then every \(k\)-module is {{< knowl id="projective-module" section="algebra-modules" text="projective" >}} and {{< knowl id="injective-module" section="algebra-modules" text="injective" >}}. Hence
\[
\mathrm{Ext}^n_k(V,W)=0\quad \text{for all }n>0
\]
(see {{< knowl id="ext" text="Ext" >}}),
because one may take a length-0 projective (or injective) resolution and the resulting cochain complex has zero cohomology in positive degrees.
