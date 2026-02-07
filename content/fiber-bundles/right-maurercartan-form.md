---
title: "Right Maurer–Cartan form"
description: "The canonical Lie-algebra-valued 1-form on a Lie group that identifies each tangent space with the Lie algebra by right translation."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} with Lie algebra {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak{g}=T_eG$. The **right Maurer–Cartan form** is the $\mathfrak{g}$-valued 1-form $\theta^R$ on $G$ defined at each $g\in G$ by
\[
\theta^R_g:T_gG\longrightarrow \mathfrak{g},
\qquad
\theta^R_g(v)= (\mathrm{d}R_{g^{-1}})_g(v),
\]
where $R_{g^{-1}}$ is {{< knowl id="right-translation" section="lie-groups" text="right translation" >}} by $g^{-1}$.

It is characterized by:
- for each $g$, $\theta^R_g$ is the inverse of $(\mathrm{d}R_g)_e:\mathfrak{g}\to T_gG$;
- $\theta^R$ is right-invariant: $(R_g)^*\theta^R=\theta^R$ for all $g\in G$.

This form provides a canonical “right trivialization” of the tangent bundle $TG\cong G\times\mathfrak{g}$.

## Examples
1. **Matrix Lie groups.** For $G\subset \mathrm{GL}(n,\mathbb{R})$, the right Maurer–Cartan form is $\theta^R=\mathrm{d}g\,g^{-1}$.
2. **Abelian groups.** If $G$ is abelian (e.g. $\mathbb{R}^n$ or $T^n$), then left and right Maurer–Cartan forms agree under the natural identifications because left and right translations coincide.
3. **Circle group.** For $G=S^1$ with $\mathfrak{g}\cong\mathbb{R}$, $\theta^R$ is again the angular 1-form; on a standard angle chart it is $\mathrm{d}\theta$.
