---
title: "Jordan content"
description: "A finite-additivity notion of volume for certain bounded subsets of Euclidean space."
---

A **Jordan content** of a bounded set $A\subseteq \mathbb R^n$ is the common value $c(A)=c^*(A)=c_*(A)$ (when it exists), where for rectangles $R=\prod_{i=1}^n [a_i,b_i]$ one sets $\operatorname{vol}(R)=\prod_{i=1}^n (b_i-a_i)$, the outer content is
\[
c^*(A)=\inf\left\{\sum_{k=1}^m \operatorname{vol}(R_k)\,:\, A\subseteq \bigcup_{k=1}^m R_k\right\},
\]
and the inner content is
\[
c_*(A)=\sup\left\{\sum_{k=1}^m \operatorname{vol}(R_k)\,:\, \bigcup_{k=1}^m R_k\subseteq A,\ \text{the }R_k\text{ are pairwise disjoint}\right\}.
\]

Jordan content is an older notion of “volume” based on finite coverings by axis-aligned products of {{< knowl id="interval" section="real-analysis" text="intervals" >}}. It is closely connected to Riemann integration and is more restrictive than {{< knowl id="lebesgue-measure" text="Lebesgue measure" >}}, which can assign sizes to far more sets.

**Examples:**
- For an interval $[a,b]\subseteq\mathbb R$, the Jordan content exists and equals $b-a$.
- If $A\subseteq\mathbb R^n$ is a finite disjoint union of rectangles $\prod_{i=1}^n [a_i,b_i]$, then the Jordan content exists and equals the sum of their volumes.
- The set $\mathbb Q\cap[0,1]\subseteq\mathbb R$ does not have a Jordan content: its inner content is $0$, while any finite rectangle cover forces outer content $1$.
