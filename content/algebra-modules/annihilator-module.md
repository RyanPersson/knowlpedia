---
title: "Annihilator of a module"
description: "The ideal of scalars that kill the entire module."
---

Let $M$ be a left $R$-{{< knowl id="module" text="module" >}}. The **annihilator** of $M$ is
\[
\operatorname{ann}_R(M)=\{r\in R: rM=0\}.
\]
It equals the {{< knowl id="intersection" section="analysis" text="intersection" >}} of the elementwise annihilators:
\[
\operatorname{ann}_R(M)=\bigcap_{m\in M}\operatorname{ann}_R(m),
\]
where $\operatorname{ann}_R(m)$ is the {{< knowl id="annihilator-element" text="annihilator of an element" >}}. For a left module, $\operatorname{ann}_R(M)$ is a {{< knowl id="two-sided-ideal" section="algebra-rings" text="two-sided ideal" >}}, since it is stable under multiplication on both sides by arbitrary ring elements.

The annihilator measures faithfulness: $M$ is faithful iff $\operatorname{ann}_R(M)=0$.

**Examples:**
- For a commutative ring $R$ and ideal $I$, the module $R/I$ satisfies $\operatorname{ann}_R(R/I)=I$.
- If $M=0$, then $\operatorname{ann}_R(M)=R$.
- If $M=R$ as a left module over itself, then $\operatorname{ann}_R(M)=0$.
