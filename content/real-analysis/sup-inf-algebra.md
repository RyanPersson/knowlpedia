---
title: "Supremum and Infimum Algebra"
description: "How supremum and infimum interact with basic set operations such as translation and scaling."
---

**Supremum/infimum algebra:** Let $A,B \subseteq \mathbb{R}$ be nonempty {{< knowl id="subset" section="shared-foundations" text="subsets" >}}. Define
$A+B=\{a+b:\ a\in A,\ b\in B\}$ and, for $c\in\mathbb{R}$, $cA=\{ca:\ a\in A\}$.
Assume the displayed quantities are finite (for example, by assuming the relevant {{< knowl id="bounded-above" text="bounded above" >}} or {{< knowl id="bounded-below" text="bounded below" >}} hypotheses). Then:

- $\sup(A+B)=\sup(A)+\sup(B)$ and $\inf(A+B)=\inf(A)+\inf(B)$.
- If $c\ge 0$, then $\sup(cA)=c\,\sup(A)$ and $\inf(cA)=c\,\inf(A)$.
- If $c\le 0$, then $\sup(cA)=c\,\inf(A)$ and $\inf(cA)=c\,\sup(A)$.
- Writing $-A=\{-a:\ a\in A\}$, one has $\sup(-A)=-\inf(A)$ and $\inf(-A)=-\sup(A)$.

These rules are frequently paired with the {{< knowl id="supremum-approximation-lemma" text="supremum approximation lemma" >}} to turn statements about {{< knowl id="supremum" text="suprema" >}} and {{< knowl id="infimum" text="infima" >}} into $\varepsilon$-estimates.
