---
title: "Homology module"
description: "The nth homology H_n(C) = ker(d_n)/im(d_{n+1}) of a chain complex of modules."
---

Let \(R\) be a {{< knowl id="ring" section="algebra-rings" text="ring" >}} and let
\[
\cdots \xrightarrow{d_{n+1}} C_n \xrightarrow{d_n} C_{n-1} \xrightarrow{d_{n-1}} \cdots
\]
be a {{< knowl id="chain-complex" text="chain complex" >}} of {{< knowl id="module" section="algebra-modules" text="R-modules" >}}, i.e. \(d_n\circ d_{n+1}=0\) for all \(n\).

The **\(n\)th cycles** and **\(n\)th boundaries** of \(C_\bullet\) are the submodules
\[
Z_n(C_\bullet) := \ker(d_n)\subseteq C_n,
\qquad
B_n(C_\bullet) := \operatorname{im}(d_{n+1})\subseteq C_n.
\]
Since \(d_n\circ d_{n+1}=0\), one has \(B_n(C_\bullet)\subseteq Z_n(C_\bullet)\). The **\(n\)th homology module** is
\[
H_n(C_\bullet) := Z_n(C_\bullet) / B_n(C_\bullet).
\]

Equivalently, \(H_n(C_\bullet)=0\) for all \(n\) iff \(C_\bullet\) is an {{< knowl id="exact-complex" text="exact complex" >}}.

## Basic properties
- A {{< knowl id="chain-map" text="chain map" >}} \(f:C_\bullet\to D_\bullet\) induces \(R\)-linear maps \(H_n(f):H_n(C_\bullet)\to H_n(D_\bullet)\) for all \(n\).
- {{< knowl id="chain-homotopy" text="chain-homotopic" >}} chain maps induce the same maps on homology.

## Examples

### Example 1: Two-term complex over \(\mathbb Z\)
Consider the chain complex \(C_\bullet\) with \(C_1=\mathbb Z\), \(C_0=\mathbb Z\), and \(d_1:\mathbb Z\to\mathbb Z\) given by multiplication by \(n\), with all other \(C_i=0\).
Then
\[
H_1(C_\bullet)=\ker(\times n)=0,\qquad
H_0(C_\bullet)=\operatorname{coker}(\times n)\cong \mathbb Z/n\mathbb Z.
\]

### Example 2: Detecting exactness
Let \(0\to A\xrightarrow{u} B\xrightarrow{v} C\to 0\) be a {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}} of \(R\)-modules, viewed as a chain complex
\[
0\to A \xrightarrow{u} B \xrightarrow{v} C \to 0
\]
concentrated in degrees \(2,1,0\).
Then the sequence is exact iff \(H_2=H_1=H_0=0\), i.e. iff the complex is {{< knowl id="exact-complex" text="exact" >}}.

### Example 3: \(\mathrm{Tor}\) as homology (concrete computation)
Let \(M=\mathbb Z/n\mathbb Z\). A {{< knowl id="projective-resolution" text="projective resolution" >}} of \(M\) over \(\mathbb Z\) is
\[
0\to \mathbb Z \xrightarrow{\times n} \mathbb Z \to \mathbb Z/n\mathbb Z \to 0.
\]
Tensoring with \(\mathbb Z/m\mathbb Z\) gives the chain complex
\[
0\to \mathbb Z/m\mathbb Z \xrightarrow{\times n} \mathbb Z/m\mathbb Z \to 0.
\]
Its homology is
\[
H_1 \cong \ker(\times n:\mathbb Z/m\to \mathbb Z/m)\cong \mathbb Z/\gcd(m,n)\mathbb Z,
\]
so
\[
\mathrm{Tor}_1^{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong \mathbb Z/\gcd(m,n)\mathbb Z.
\]
(Here we are using the identification $H_1(P_\bullet\otimes -)\cong \mathrm{Tor}_1$; see {{< knowl id="tor" text="Tor" >}}.)
