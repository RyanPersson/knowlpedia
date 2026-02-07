---
title: "Carathéodory construction"
description: "A method that turns an outer measure into a measure by selecting Carathéodory measurable sets."
---

**Carathéodory construction:** Let $\mu^*$ be an {{< knowl id="outer-measure" text="outer measure" >}} on a set $X$. Define
$$
\mathcal{M}
=\Bigl\{E\subseteq X : \mu^*(A)=\mu^*(A\cap E)+\mu^*(A\setminus E)\ \text{for every } A\subseteq X\Bigr\}.
$$

Then $\mathcal{M}$ is a {{< knowl id="sigma-algebra" text="sigma-algebra" >}} on $X$, and the restriction $\mu:=\mu^*|_{\mathcal{M}}$ is a {{< knowl id="measure" text="measure" >}} on $\mathcal{M}$. The sets in $\mathcal{M}$ are exactly the {{< knowl id="caratheodory-measurable-set" text="Carathéodory measurable sets" >}} associated to $\mu^*$.

This construction is a standard way to build a {{< knowl id="measurable-space" text="measurable space" >}} and a measure from an outer measure; in particular it underlies the definition of {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}} on $\mathbb{R}^n$.
