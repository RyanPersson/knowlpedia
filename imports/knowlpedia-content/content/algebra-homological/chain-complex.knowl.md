+++
id = "algebra-homological/chain-complex"
title = "Chain complex"
kind = "knowl"
summary = "A graded sequence of modules with differentials d lowering degree and satisfying d∘d=0."
aliases = ["chain-complex", "Chain complex"]
domains = ["algebra-homological"]
legacy_source_path = "algebra-homological/chain-complex.md"
+++

Let \(R\) be a ring and let \(\{C_n\}_{n\in\mathbb Z}\) be a family of [[algebra-modules/module|(left) R-modules]].
A **chain complex** \( (C_\bullet, d)\) is a collection of \(R\)-linear maps (called **differentials**)
\[
d_n : C_n \longrightarrow C_{n-1}\qquad (n\in\mathbb Z)
\]
such that
\[
d_{n-1}\circ d_n = 0\quad\text{for all }n.
\]
Equivalently, \(\operatorname{im}(d_n)\subseteq \ker(d_{n-1})\) for all \(n\).

The associated **homology modules** are
\[
H_n(C_\bullet)=\ker(d_n)/\operatorname{im}(d_{n+1}),
\]
see [[algebra-homological/homology-module|homology module]].

## Cross-links
- Morphisms between complexes: [[algebra-homological/chain-map|chain map]].
- When all homology vanishes: [[algebra-homological/exact-complex|exact complex]].
- Categorical setting: in an [[algebra-category-theory/abelian-category|abelian category]], a chain complex is defined the same way using kernels and images.

## Examples
1. **Complex concentrated in degree 0.**
   For an \(R\)-module \(M\), the diagram
   \[
   \cdots \to 0 \to M \to 0 \to \cdots
   \]
   with \(M\) in degree \(0\) and all differentials \(0\), is a chain complex. Its homology is \(H_0\cong M\) and \(H_n=0\) for \(n\neq 0\).

2. **A map as a 2-term complex.**
   Any \(R\)-linear map \(f:M\to N\) gives a chain complex
   \[
   0 \longrightarrow M \xrightarrow{\,f\,} N \longrightarrow 0
   \]
   with \(M\) in degree \(1\) and \(N\) in degree \(0\). Then
   \[
   H_1 \cong \ker(f),\qquad H_0 \cong \operatorname{coker}(f),
   \]
   using [[algebra-rings/kernel-ring|kernel]] / [[algebra-modules/cokernel-module|cokernel]].

3. **“Multiplication by \(x\)” complex.**
   For \(x\in R\), the 2-term complex
   \[
   0 \to R \xrightarrow{\,\cdot x\,} R \to 0
   \]
   (degrees \(1\to 0\)) has
   \[
   H_1 \cong \{r\in R: xr=0\} = \operatorname{Ann}_R(x),
   \qquad
   H_0 \cong R/xR.
   \]
   If \(R\) is a domain and \(x\neq 0\), then \(H_1=0\).
