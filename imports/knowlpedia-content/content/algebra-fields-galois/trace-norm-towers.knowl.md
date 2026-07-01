+++
id = "algebra-fields-galois/trace-norm-towers"
title = "Trace and norm in towers"
kind = "knowl"
summary = "In a tower K⊂E⊂L of finite extensions, trace and norm compose multiplicatively/additively."
aliases = ["trace-norm-towers", "Trace and norm in towers"]
domains = ["algebra-fields-galois"]
legacy_source_path = "algebra-fields-galois/trace-norm-towers.md"
+++

Let \(K\subseteq E\subseteq L\) be a [[algebra-fields-galois/tower-of-fields|tower of fields]] of finite extensions. For \(x\in L\), write
\[
\mathrm{Tr}_{L/K}(x)\in K,\qquad N_{L/K}(x)\in K
\]
for the [[algebra-fields-galois/trace-field|field trace]] and [[algebra-fields-galois/norm-field|field norm]]. Then trace and norm are compatible with towers:

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

These identities are compatible with degree calculations from the [[algebra-fields-galois/tower-law|tower law]] and reflect the fact that trace and norm can be defined as the trace/determinant of the \(K\)-linear map “multiplication by \(x\)” on \(L\).

### Examples

1. **A quadratic subextension.**
   Take \(K=\mathbb{Q}\), \(E=\mathbb{Q}(\sqrt2)\), \(L=E(\sqrt3)=\mathbb{Q}(\sqrt2,\sqrt3)\). For \(y=a+b\sqrt2\in E\),
   \(\mathrm{Tr}_{E/K}(y)=2a\) and \(N_{E/K}(y)=a^2-2b^2\). The tower formulas then compute \(\mathrm{Tr}_{L/K}\) and \(N_{L/K}\) by first taking \(\mathrm{Tr}_{L/E}\), \(N_{L/E}\) and then applying the quadratic formulas above.

2. **Cyclotomic example.**
   With \(K=\mathbb{Q}\subseteq E=\mathbb{Q}(\zeta_3)\subseteq L=\mathbb{Q}(\zeta_9)\), the tower identities express \(\mathrm{Tr}_{L/\mathbb{Q}}\) and \(N_{L/\mathbb{Q}}\) in terms of intermediate traces/norms, often simplifying computations because \(\mathrm{Gal}(L/E)\) is smaller than \(\mathrm{Gal}(L/\mathbb{Q})\).

3. **Finite fields.**
   For \(\mathbb{F}_p \subseteq \mathbb{F}_{p^m}\subseteq \mathbb{F}_{p^n}\) with \(m\mid n\), the trace and norm are given by explicit Frobenius sums/products, and the tower formulas reflect the composition of these Frobenius patterns (see [[algebra-fields-galois/finite-field-galois-group-cyclic|finite-field cyclic Galois group]]).
