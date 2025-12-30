---
title: "Annihilator of an element"
description: "The ideal of ring elements that kill a given module element."
---

Let $M$ be a left $R$-{{< knowl id="module" text="module" >}} and $m\in M$. The **annihilator** of $m$ is
\[
\operatorname{ann}_R(m)=\{r\in R: rm=0\}.
\]
It is a (left) {{< knowl id="ideal" text="ideal" >}} of the {{< knowl id="ring" text="ring" >}} $R$; if $R$ is commutative, it is an ideal in the usual sense.

Annihilators quantify how far an element is from being “faithfully acted on” by the ring and are closely related to torsion and cyclic quotients.

**Examples:**
- In the $\mathbb Z$-module $\mathbb Z/n\mathbb Z$, $\operatorname{ann}(1\bmod n)=n\mathbb Z$.
- In the left $R$-module $R$, $\operatorname{ann}(1)=0$.
- If $m=0$, then $\operatorname{ann}(m)=R$.
