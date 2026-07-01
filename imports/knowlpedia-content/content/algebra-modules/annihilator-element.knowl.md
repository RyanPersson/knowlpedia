+++
id = "algebra-modules/annihilator-element"
title = "Annihilator of an element"
kind = "knowl"
summary = "The ideal of ring elements that kill a given module element."
aliases = ["annihilator-element", "Annihilator of an element"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/annihilator-element.md"
+++

Let $M$ be a left $R$-[[algebra-modules/module|module]] and $m\in M$. The **annihilator** of $m$ is
\[
\operatorname{ann}_R(m)=\{r\in R: rm=0\}.
\]
It is a (left) [[algebra-rings/ideal|ideal]] of the [[algebra-rings/ring|ring]] $R$; if $R$ is commutative, it is an ideal in the usual sense.

Annihilators quantify how far an element is from being “faithfully acted on” by the ring and are closely related to torsion and cyclic quotients.

**Examples:**
- In the $\mathbb Z$-module $\mathbb Z/n\mathbb Z$, $\operatorname{ann}(1\bmod n)=n\mathbb Z$.
- In the left $R$-module $R$, $\operatorname{ann}(1)=0$.
- If $m=0$, then $\operatorname{ann}(m)=R$.
