---
title: "Trace and norm in towers"
description: "In a tower K⊂E⊂L of finite extensions, trace and norm compose multiplicatively/additively."
---

Let \(K\subseteq E\subseteq L\) be a {{< knowl id="tower-of-fields" text="tower of fields" >}} of finite extensions. For \(x\in L\), write
\[
\mathrm{Tr}_{L/K}(x)\in K,\qquad N_{L/K}(x)\in K
\]
for the {{< knowl id="trace-field" text="field trace" >}} and {{< knowl id="norm-field" text="field norm" >}}. Then trace and norm are compatible with towers:

**Theorem (tower formulas).**
\[
\mathrm{Tr}_{L/K}=\mathrm{Tr}_{E/K}\circ \mathrm{Tr}_{L/E},\qquad
N_{L/K}=N_{E/K}\circ N_{L/E}.
\]
Equivalently, for all \(x\in L\),
\[
\mathrm{Tr}_{L/K}(x)=\mathrm{Tr}_{E/K}\!\big(\mathrm{Tr}_{L/E}(x)\big),\quad
N_{L/K}(x)=N_{E/K}\!\big(N_{L/E}(x)\big).
\]

These identities are compatible with degree calculations from the {{< knowl id="tower-law" text="tower law" >}} and reflect the fact that trace and norm can be defined as the trace/determinant of the \(K\)-linear map “multiplication by \(x\)” on \(L\).

### Examples

1. **A quadratic subextension.**  
   Take \(K=\mathbb{Q}\), \(E=\mathbb{Q}(\sqrt2)\), \(L=E(\sqrt3)=\mathbb{Q}(\sqrt2,\sqrt3)\). For \(y=a+b\sqrt2\in E\),
   \(\mathrm{Tr}_{E/K}(y)=2a\) and \(N_{E/K}(y)=a^2-2b^2\). The tower formulas then compute \(\mathrm{Tr}_{L/K}\) and \(N_{L/K}\) by first taking \(\mathrm{Tr}_{L/E}\), \(N_{L/E}\) and then applying the quadratic formulas above.

2. **Cyclotomic example.**  
   With \(K=\mathbb{Q}\subseteq E=\mathbb{Q}(\zeta_3)\subseteq L=\mathbb{Q}(\zeta_9)\), the tower identities express \(\mathrm{Tr}_{L/\mathbb{Q}}\) and \(N_{L/\mathbb{Q}}\) in terms of intermediate traces/norms, often simplifying computations because \(\mathrm{Gal}(L/E)\) is smaller than \(\mathrm{Gal}(L/\mathbb{Q})\).

3. **Finite fields.**  
   For \(\mathbb{F}_p \subseteq \mathbb{F}_{p^m}\subseteq \mathbb{F}_{p^n}\) with \(m\mid n\), the trace and norm are given by explicit Frobenius sums/products, and the tower formulas reflect the composition of these Frobenius patterns (see {{< knowl id="finite-field-galois-group-cyclic" text="finite-field cyclic Galois group" >}}).
