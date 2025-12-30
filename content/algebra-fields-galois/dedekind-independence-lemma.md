---
title: "Dedekind Independence Lemma"
description: "Distinct field homomorphisms are linearly independent as functions."
---

**Lemma (Dedekind independence).**  
Let \(L\) be a field and \(\sigma_1,\dots,\sigma_m: L\to \Omega\) be **distinct** field homomorphisms into a commutative ring (or field) \(\Omega\). If
\[
a_1\sigma_1(x)+\cdots+a_m\sigma_m(x)=0 \quad \text{for all }x\in L
\]
with coefficients \(a_i\in \Omega\), then \(a_1=\cdots=a_m=0\).  
Equivalently, \(\{\sigma_1,\dots,\sigma_m\}\) is linearly independent over \(\Omega\) inside the \(\Omega\)-module of functions \(L\to\Omega\).

This is a key input for {{< knowl id="artins-theorem-fixed-fields" text="Artin's theorem on fixed fields" >}}.

**Examples.**
1. Over \(L=\mathbb{C}\), the maps \(\mathrm{id}\) and complex conjugation \(\overline{\phantom{x}}\) are distinct, hence linearly independent as \(\mathbb{C}\)-valued functions on \(\mathbb{C}\).
2. If \(L/K\) is {{< knowl id="galois-extension" text="Galois" >}} and \(G=\mathrm{Gal}(L/K)\), then the distinct \(\sigma\in G\) are linearly independent. In particular, a relation \(\sum_{\sigma\in G}a_\sigma\sigma=0\) forces all \(a_\sigma=0\).
3. For \(L=\mathbb{F}_{p^n}\), the maps \(x\mapsto x^{p^i}\) (\(0\le i<n\)) are distinct automorphisms, hence independent.

**Related.** {{< knowl id="field-automorphism" text="field automorphisms" >}}, {{< knowl id="trace-field" text="trace" >}}.
