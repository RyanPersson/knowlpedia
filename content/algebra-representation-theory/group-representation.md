---
title: "Group representation"
description: "A linear action of a group on a vector space, equivalently a homomorphism into a general linear group."
---

Let \(G\) be a group and let \(k\) be a field. A **(linear) representation** of \(G\) over \(k\) is a pair \((V,\rho)\) where

- \(V\) is a finite-dimensional {{< knowl id="vector-space" section="linear-algebra" text="vector space" >}} over \(k\), and
- \(\rho: G \to \mathrm{GL}(V)\) is a group homomorphism.

Equivalently, \(G\) acts on \(V\) by \(k\)-linear automorphisms via
\[
g\cdot v := \rho(g)(v),
\]
so that \(e\cdot v = v\) and \((gh)\cdot v = g\cdot(h\cdot v)\) for all \(g,h\in G\), \(v\in V\).

The **dimension** (or **degree**) of the representation is \(\dim_k(V)\).

### Module and group-algebra viewpoint
A representation \((V,\rho)\) is equivalently a left module over the {{< knowl id="group-algebra" text="group algebra" >}} \(k[G]\): extend \(\rho\) \(k\)-linearly to an algebra homomorphism
\[
k[G]\longrightarrow \mathrm{End}_k(V),
\]
where \(\mathrm{End}_k(V)\) consists of {{< knowl id="linear-map" section="linear-algebra" text="linear maps" >}} \(V\to V\).

### Morphisms of representations
A **homomorphism of representations** \(f:(V,\rho)\to (W,\sigma)\) is a \(k\)-linear map \(f:V\to W\) such that
\[
f(\rho(g)v)=\sigma(g)f(v)\quad\text{for all } g\in G,\ v\in V.
\]
Equivalently, \(f\) is a \(k[G]\)-module homomorphism (compare {{< knowl id="module-homomorphism" section="algebra-modules" text="module homomorphism" >}}).

### Character
To any representation one associates its {{< knowl id="character" text="character" >}} \(\chi_\rho(g)=\mathrm{tr}(\rho(g))\), using the {{< knowl id="trace" section="linear-algebra" text="trace" >}}.

## Examples
1. **Trivial representation (any group).**  
   Take \(V=k\) and \(\rho(g)=\mathrm{id}_k\) for all \(g\in G\). Then \(g\cdot v=v\) for all \(g\), and \(\chi(g)=1\).

2. **Sign representation of \(S_3\).**  
   Over any field \(k\) with \(\mathrm{char}(k)\neq 2\), define \(\rho:S_3\to k^\times\subset \mathrm{GL}_1(k)\) by \(\rho(\sigma)=\mathrm{sgn}(\sigma)\). This is 1-dimensional and nontrivial.

3. **One-dimensional representations of a cyclic group.**  
   Let \(C_n=\langle g\mid g^n=1\rangle\), and take \(k=\mathbb{C}\). For each integer \(j\), define \(\rho_j:C_n\to \mathbb{C}^\times\) by \(\rho_j(g)=\zeta_n^j\), where \(\zeta_n=e^{2\pi i/n}\). Then \(\rho_j(g^m)=\zeta_n^{jm}\) and \(\dim(\rho_j)=1\).

See also: {{< knowl id="subrepresentation" text="subrepresentation" >}}, {{< knowl id="irreducible-representation" text="irreducible representation" >}}, {{< knowl id="regular-representation" text="regular representation" >}}.
