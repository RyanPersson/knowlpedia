---
title: "Maurer–Cartan equation"
description: "A structural identity satisfied by the Maurer–Cartan form expressing flatness of the canonical trivialization on a Lie group."
---

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$. Consider the {{< knowl id="left-maurercartan-form" text="left Maurer–Cartan form" >}} $\theta^L\in\Omega^1(G;\mathfrak{g})$.

Define the bracket of $\mathfrak{g}$-valued 1-forms by using the {{< knowl id="lie-bracket" text="Lie bracket" >}} on $\mathfrak{g}$: for tangent vectors $u,v\in T_gG$ set
\[
[\theta^L\wedge \theta^L]_g(u,v) = [\theta^L_g(u),\,\theta^L_g(v)]\in\mathfrak{g},
\]
and extend by bilinearity and antisymmetry. Then the **Maurer–Cartan equation** is the identity
\[
\mathrm{d}\theta^L+\tfrac12[\theta^L\wedge\theta^L]=0,
\]
where $\mathrm{d}$ is the {{< knowl id="exterior-derivative" text="exterior derivative" >}} applied componentwise.

With the same convention, the {{< knowl id="right-maurercartan-form" text="right Maurer–Cartan form" >}} $\theta^R$ satisfies
\[
\mathrm{d}\theta^R-\tfrac12[\theta^R\wedge\theta^R]=0.
\]
(These sign conventions match the standard matrix identities for $g^{-1}\mathrm{d}g$ and $\mathrm{d}g\,g^{-1}$.)

## Examples
1. **Abelian Lie groups.** If $\mathfrak{g}$ is abelian, the bracket term vanishes and the equation reduces to $\mathrm{d}\theta^L=0$ (and likewise for $\theta^R$). For $G=\mathbb{R}^n$, this is just $\mathrm{d}(\mathrm{d}x^i)=0$.
2. **Matrix computation.** For a matrix Lie group with $\theta^L=g^{-1}\mathrm{d}g$, the equation becomes $\mathrm{d}(g^{-1}\mathrm{d}g)+ (g^{-1}\mathrm{d}g)\wedge(g^{-1}\mathrm{d}g)=0$, which is the differential identity obtained by differentiating $g^{-1}g=I$.
3. **Structure constants viewpoint.** If $\{e_i\}$ is a basis of $\mathfrak{g}$ with $[e_i,e_j]=c_{ij}^k e_k$ and $\theta^L=\theta^i e_i$, the equation becomes $\mathrm{d}\theta^k + \tfrac12 c_{ij}^k\,\theta^i\wedge\theta^j=0$, recovering the standard structure equations.
