---
title: "Cochain complex"
description: "A graded sequence of modules with differentials d raising degree and satisfying d∘d=0."
---

Let \(R\) be a ring and let \(\{C^n\}_{n\in\mathbb Z}\) be {{< knowl id="module" section="algebra-modules" text="R-modules" >}}.
A **cochain complex** \( (C^\bullet, d)\) is a collection of \(R\)-linear maps
\[
d^n : C^n \longrightarrow C^{n+1}\qquad (n\in\mathbb Z)
\]
such that
\[
d^{n+1}\circ d^n = 0\quad\text{for all }n.
\]
Its **cohomology modules** are
\[
H^n(C^\bullet)=\ker(d^n)/\operatorname{im}(d^{n-1}),
\]
see {{< knowl id="cohomology-module" text="cohomology module" >}}.

## Cross-links
- Chain vs. cochain conventions: compare {{< knowl id="chain-complex" text="chain complex" >}}.
- Cochain complexes from \(\mathrm{Hom}\): {{< knowl id="hom-module" section="algebra-modules" text="Hom" >}} and {{< knowl id="hom-left-exact" text="left exactness of Hom" >}}.
- Cohomology as a derived functor: {{< knowl id="derived-functor" text="derived functor" >}} and {{< knowl id="ext" text="Ext" >}}.

## Examples
1. **Cochain complex concentrated in degree 0.**  
   For an \(R\)-module \(M\), the diagram
   \[
   \cdots \to 0 \to M \to 0 \to \cdots
   \]
   with \(M\) in degree \(0\) is a cochain complex. Then \(H^0\cong M\) and \(H^n=0\) for \(n\neq 0\).

2. **Hom of a chain complex is a cochain complex.**  
   If \((C_\bullet,d)\) is a {{< knowl id="chain-complex" text="chain complex" >}} and \(M\) is an \(R\)-module, define
   \[
   \operatorname{Hom}_R(C_\bullet,M)^n := \operatorname{Hom}_R(C_n,M),
   \]
   and set
   \[
   \delta^n(\varphi) := \varphi\circ d_{n+1} \in \operatorname{Hom}_R(C_{n+1},M).
   \]
   Then \(\delta^{n+1}\circ \delta^n=0\) because \(d\circ d=0\), so this is a cochain complex. This construction underlies the computation of {{< knowl id="ext" text="Ext" >}} from a {{< knowl id="projective-resolution" text="projective resolution" >}}.

3. **“Multiplication by \(x\)” as a cochain complex.**  
   For \(x\in R\), the 2-term cochain complex
   \[
   0 \to R \xrightarrow{\,\cdot x\,} R \to 0
   \]
   (degrees \(0\to 1\)) has
   \[
   H^0 \cong \operatorname{Ann}_R(x),\qquad H^1 \cong R/xR.
   \]
