---
title: "Nowhere dense set"
description: "A set whose closure has empty interior."
---

Let $(X,d)$ be a metric space and let $A\subseteq X$. The set $A$ is **nowhere dense** in $X$ if
$$\operatorname{int}(\overline{A})=\varnothing.$$

Equivalently, $A$ is nowhere dense iff every nonempty open set $U\subseteq X$ contains a nonempty open set $V\subseteq U$ with $V\cap A=\varnothing$. Nowhere dense sets are "small" from the point of view of category (not measure).

**Examples:**
- In $\mathbb{R}$, the set $\mathbb{Z}$ is nowhere dense: its closure is $\mathbb{Z}$ and its interior is empty.
- The Cantor set in $\mathbb{R}$ is nowhere dense (its closure is itself and it contains no interval).
- A dense set need not be non-nowhere-dense: $\mathbb{Q}$ is dense in $\mathbb{R}$, but it is not nowhere dense since $\overline{\mathbb{Q}}=\mathbb{R}$ and $\operatorname{int}(\mathbb{R})=\mathbb{R}\neq\varnothing$.
