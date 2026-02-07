---
title: "Galois Correspondence"
description: "For a finite Galois extension, intermediate fields correspond bijectively to subgroups of the Galois group."
---

Let $L/K$ be a finite {{< knowl id="galois-extension" text="Galois extension" >}} with {{< knowl id="galois-group" text="Galois group" >}} $G = \mathrm{Gal}(L/K)$.

Let $\mathcal{I}(L/K)$ denote the set of {{< knowl id="intermediate-field" text="intermediate fields" >}} $E$ with $K\subseteq E\subseteq L$, and let $\mathrm{Sub}(G)$ be the set of subgroups of $G$.

For $E\in\mathcal{I}(L/K)$ define
\[
\Phi(E) = \mathrm{Gal}(L/E)=\{\sigma\in G:\sigma|_E=\mathrm{id}_E\},
\]
and for a subgroup $H\le G$ define its {{< knowl id="fixed-field" text="fixed field" >}}
\[
\Psi(H)=L^H=\{x\in L:\sigma(x)=x\ \text{for all }\sigma\in H\}.
\]

**Theorem (Galois correspondence).**  
The assignments $\Phi$ and $\Psi$ are inverse bijections
\[
\mathcal{I}(L/K)\ \longleftrightarrow\ \mathrm{Sub}(G),
\]
and they reverse inclusions: if $E_1\subseteq E_2$ then $\mathrm{Gal}(L/E_2)\le \mathrm{Gal}(L/E_1)$, and if $H_1\le H_2$ then $L^{H_2}\subseteq L^{H_1}$.

Moreover, for $H\le G$ one has the degree/index formulas
\[
[L:L^H]=|H|,\qquad [L^H:K]=[G:H],
\]
which combine {{< knowl id="galois-degree-equals-group-order" text="degree = group order for finite Galois extensions" >}} with the {{< knowl id="tower-law" text="tower law" >}}.

Finally, for $E\in\mathcal{I}(L/K)$ with corresponding subgroup $H=\mathrm{Gal}(L/E)$, the subextension $E/K$ is {{< knowl id="normal-extension" text="normal" >}} (equivalently, Galois) if and only if $H$ is a normal subgroup of $G$, and then restriction induces an isomorphism
\[
\mathrm{Gal}(E/K)\ \cong\ G/H.
\]
This correspondence is one standard formulation of the {{< knowl id="fundamental-theorem-galois-theory" text="Fundamental Theorem of Galois Theory" >}}.

### Examples
1. **A biquadratic extension with Klein four group.**  
   Let $L=\mathbb{Q}(\sqrt2,\sqrt3)$ and $K=\mathbb{Q}$. This is the {{< knowl id="splitting-field" text="splitting field" >}} of $(x^2-2)(x^2-3)$, hence a finite Galois extension. The group $G=\mathrm{Gal}(L/\mathbb{Q})$ has four elements, determined by independent sign changes of $\sqrt2$ and $\sqrt3$:
   - $\tau_2(\sqrt2)=-\sqrt2,\ \tau_2(\sqrt3)=\sqrt3$,
   - $\tau_3(\sqrt2)=\sqrt2,\ \tau_3(\sqrt3)=-\sqrt3$,
   - $\tau_6=\tau_2\tau_3$.
   
   The three subgroups of order $2$ correspond to the three quadratic intermediate fields:
   \[
   L^{\langle\tau_2\rangle}=\mathbb{Q}(\sqrt3),\quad
   L^{\langle\tau_3\rangle}=\mathbb{Q}(\sqrt2),\quad
   L^{\langle\tau_6\rangle}=\mathbb{Q}(\sqrt6).
   \]
   The full group fixes $\mathbb{Q}$, and the trivial subgroup fixes $L$.

2. **A cyclotomic example.**  
   Let $L=\mathbb{Q}(\zeta_5)$ (a {{< knowl id="cyclotomic-extension" text="cyclotomic extension" >}}) and $K=\mathbb{Q}$. Then $G\cong(\mathbb{Z}/5\mathbb{Z})^\times$ is cyclic of order $4$. There is exactly one subgroup of order $2$, hence exactly one intermediate field $E$ with $[E:\mathbb{Q}]=2$, namely the maximal real subfield
   \[
   E=\mathbb{Q}(\zeta_5+\zeta_5^{-1})=\mathbb{Q}(\sqrt5).
   \]

3. **Finite fields.**  
   For $L=\mathbb{F}_{p^n}$ and $K=\mathbb{F}_p$, the extension is Galois with cyclic group (see {{< knowl id="finite-field-galois-cyclic" text="finite-field Galois cyclicity" >}}). Subgroups of a cyclic group correspond to divisors of $n$, so the intermediate fields are exactly
   \[
   \mathbb{F}_{p^d}\quad (d\mid n),
   \]
   with $\mathbb{F}_{p^d}$ corresponding to the unique subgroup of $G$ of index $d$.
