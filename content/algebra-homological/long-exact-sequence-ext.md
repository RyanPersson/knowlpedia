---
title: "Long exact sequence for Ext"
description: "The natural long exact sequence in Ext induced by a short exact sequence of modules."
---

Let \(R\) be a ring. Recall that {{< knowl id="ext" text="Ext" >}} is a right-derived functor of {{< knowl id="hom-module" section="algebra-modules" text="Hom" >}} ({{< knowl id="hom-left-exact" text="left exactness of Hom" >}}), constructed using an {{< knowl id="injective-resolution" text="injective resolution" >}} (or a {{< knowl id="projective-resolution" text="projective resolution" >}} in the first variable). See also {{< knowl id="derived-functor" text="derived functor" >}}.

## Theorem (long exact sequence in Ext, both variables)

### (A) Short exact sequence in the **first** variable (contravariant)
Let
\[
0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0
\]
be a {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}} of left \(R\)-modules, and let \(B\) be a left \(R\)-module. Then there are natural connecting maps
\[
\delta^n:\operatorname{Ext}_R^{n}(A',B)\longrightarrow \operatorname{Ext}_R^{n+1}(A'',B)
\quad (n\ge 0),
\]
(see {{< knowl id="connecting-homomorphism-lemma" text="connecting homomorphism" >}}) and a natural long exact sequence
\[
0\to \operatorname{Hom}_R(A'',B)\to \operatorname{Hom}_R(A,B)\to \operatorname{Hom}_R(A',B)
\to \operatorname{Ext}_R^{1}(A'',B)\to \operatorname{Ext}_R^{1}(A,B)\to \operatorname{Ext}_R^{1}(A',B)
\to \operatorname{Ext}_R^{2}(A'',B)\to \cdots .
\]

This is a special case of the general {{< knowl id="long-exact-sequence-derived" text="long exact sequence for derived functors" >}}.

### (B) Short exact sequence in the **second** variable (covariant)
Let
\[
0 \longrightarrow B' \xrightarrow{u} B \xrightarrow{v} B'' \longrightarrow 0
\]
be a short exact sequence of left \(R\)-modules, and let \(A\) be a left \(R\)-module. Then there is a natural long exact sequence
\[
0\to \operatorname{Hom}_R(A,B')\to \operatorname{Hom}_R(A,B)\to \operatorname{Hom}_R(A,B'')
\to \operatorname{Ext}_R^{1}(A,B')\to \operatorname{Ext}_R^{1}(A,B)\to \operatorname{Ext}_R^{1}(A,B'')
\to \operatorname{Ext}_R^{2}(A,B')\to \cdots .
\]

## Examples

1. **Computing \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n, A)\cong A/nA\).**  
   Start from
   \[
   0\to \mathbb Z \xrightarrow{\cdot n}\mathbb Z \to \mathbb Z/n \to 0.
   \]
   Apply \(\operatorname{Hom}_{\mathbb Z}(-,A)\). Since \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z,A)\cong A\), the relevant piece of the long exact sequence is
   \[
   A \xrightarrow{\cdot n} A \to \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\to 0,
   \]
   so
   \[
   \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong \operatorname{coker}(\cdot n:A\to A)\cong A/nA.
   \]
   (Also \(\operatorname{Ext}^i_{\mathbb Z}(\mathbb Z/n,-)=0\) for \(i\ge 2\) because \(\mathbb Z/n\) has a length-1 projective resolution.)

2. **Computing \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n, \mathbb Z/m)\cong \mathbb Z/\gcd(n,m)\).**  
   Take \(A=\mathbb Z/m\) in the previous example:
   \[
   \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong (\mathbb Z/m)/n(\mathbb Z/m)
   \cong \mathbb Z/\gcd(n,m).
   \]

3. **Dual numbers: \(\operatorname{Ext}^1_{k[\varepsilon]/(\varepsilon^2)}(k,k)\cong k\).**  
   Let \(R=k[\varepsilon]/(\varepsilon^2)\), \(k=R/(\varepsilon)\), and use the projective resolution
   \[
   0\to R\xrightarrow{\cdot\varepsilon}R\to k\to 0.
   \]
   Applying \(\operatorname{Hom}_R(-,k)\) yields the cochain complex
   \[
   0\to \operatorname{Hom}_R(R,k)\xrightarrow{(\cdot\varepsilon)^\ast}\operatorname{Hom}_R(R,k)\to 0,
   \]
   and \((\cdot\varepsilon)^\ast=0\) because \(\varepsilon\) acts as \(0\) on \(k\). Hence
   \[
   \operatorname{Ext}^1_R(k,k)\cong \operatorname{coker}(0:k\to k)\cong k.
   \]
