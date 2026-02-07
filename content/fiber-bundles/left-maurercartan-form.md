---
title: "Left Maurer–Cartan form"
description: "The canonical Lie-algebra-valued 1-form on a Lie group that identifies each tangent space with the Lie algebra by left translation."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" >}} with Lie algebra {{< knowl id="lie-algebra" text="Lie algebra" section="lie-groups">}} $\mathfrak{g}=T_eG$. The **left Maurer–Cartan form** is the $\mathfrak{g}$-valued 1-form $\theta^L$ on $G$ defined at each $g\in G$ by the linear map
\[
\theta^L_g:T_gG\longrightarrow \mathfrak{g},
\qquad
\theta^L_g(v)= (\mathrm{d}L_{g^{-1}})_g(v),
\]
where $L_{g^{-1}}$ is {{< knowl id="left-translation" section="lie-groups" text="left translation" >}} by $g^{-1}$.

Equivalently, $\theta^L$ is the unique $\mathfrak{g}$-valued 1-form such that:
- for every $g\in G$, $\theta^L_g$ is the inverse of $(\mathrm{d}L_g)_e:\mathfrak{g}\to T_gG$;
- $\theta^L$ is left-invariant: $(L_g)^*\theta^L=\theta^L$ for all $g\in G$.

Thus $\theta^L$ provides a canonical “left trivialization” of the tangent bundle $TG\cong G\times\mathfrak{g}$.

## Examples
1. **Matrix Lie groups.** For $G\subset \mathrm{GL}(n,\mathbb{R})$, the left Maurer–Cartan form is $\theta^L=g^{-1}\mathrm{d}g$ (interpreted as a matrix of 1-forms with values in $\mathfrak{g}$).
2. **Additive group.** For $G=\mathbb{R}^n$ under addition, $\mathfrak{g}\cong\mathbb{R}^n$ and $\theta^L$ is the identity-valued 1-form; in coordinates it is the column vector $(\mathrm{d}x^1,\dots,\mathrm{d}x^n)$.
3. **Circle group.** For $G=S^1$, identifying $\mathfrak{g}\cong\mathbb{R}$, the form $\theta^L$ is the standard angular 1-form; in the coordinate $\theta$ on $S^1\setminus\{\text{point}\}$ it is $\mathrm{d}\theta$.
