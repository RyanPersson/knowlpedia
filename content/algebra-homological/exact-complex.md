---
title: "Exact complex"
description: "A chain complex whose homology vanishes in every degree (equivalently, im d = ker d)."
---

A {{< knowl id="chain-complex" text="chain complex" >}} \((C_\bullet,d)\) is **exact** if any (hence all) of the following equivalent conditions hold:

1. \(H_n(C_\bullet)=0\) for all \(n\), where {{< knowl id="homology-module" text="homology module" >}} is used.
2. For every \(n\),
   \[
   \operatorname{im}(d_{n+1}) = \ker(d_n).
   \]
3. The sequence
   \[
   \cdots \xrightarrow{d_{n+2}} C_{n+1} \xrightarrow{d_{n+1}} C_n \xrightarrow{d_n} C_{n-1}\xrightarrow{d_{n-1}} \cdots
   \]
   is exact at each \(C_n\) in the sense of kernels/images; compare {{< knowl id="exactness-via-kernels-images" section="algebra-modules" text="exactness via kernels and images" >}}.

In an {{< knowl id="abelian-category" section="algebra-category-theory" text="abelian category" >}}, the same definition makes sense using categorical kernels and images.

## Cross-links
- Exactness for short sequences: {{< knowl id="short-exact-sequence" section="algebra-modules" text="short exact sequence" >}}.
- A strong way to prove exactness is via a contracting homotopy: {{< knowl id="chain-homotopy" text="chain homotopy" >}}.
- Exact complexes appear as resolutions: {{< knowl id="projective-resolution" text="projective resolution" >}} and {{< knowl id="injective-resolution" text="injective resolution" >}}.

## Examples
1. **A short exact sequence as an exact complex.**  
   Any short exact sequence \(0\to A\to B\to C\to 0\) of \(R\)-modules is an exact complex with \(A,B,C\) placed in degrees \(1,0,-1\) (or \(2,1,0\), depending on convention). See {{< knowl id="exact-sequence-modules" section="algebra-modules" text="exact sequence of modules" >}}.

2. **Identity map complex.**  
   The 2-term complex
   \[
   0 \to R \xrightarrow{\,\mathrm{id}\,} R \to 0
   \]
   is exact: \(\ker(\mathrm{id})=0\) and \(\operatorname{coker}(\mathrm{id})=0\). In fact, it is contractible (see {{< knowl id="chain-homotopy" text="chain homotopy" >}} example), so its homology vanishes.

3. **A standard exact sequence over \(\mathbb Z\).**  
   For \(n\ge 1\), the sequence
   \[
   0 \longrightarrow \mathbb Z \xrightarrow{\,\cdot n\,} \mathbb Z \longrightarrow \mathbb Z/n\mathbb Z \longrightarrow 0
   \]
   is short exact, hence an exact complex. This 2-term free resolution of \(\mathbb Z/n\mathbb Z\) is the starting point for concrete computations of {{< knowl id="tor" text="Tor" >}} and {{< knowl id="ext" text="Ext" >}}.
