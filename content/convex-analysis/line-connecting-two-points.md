---
title: "Line Connecting Two Points"
description: "The affine line through a and b: {λa+(1−λ)b : λ∈R}."
---

Let $X$ be a {{< knowl id="vector-space" section="linear-algebra" section="linear-algebra" text="vector space" >}} and let $a,b\in X$. The **line connecting $a$ and $b$** is
$$
L[a,b]:=\{\lambda a+(1-\lambda)b\mid \lambda\in\mathbb{R}\}.
$$

This is the smallest {{< knowl id="affine-set" text="affine set" >}} containing $\{a,b\}$ and is the affine analogue of the {{< knowl id="line-segments-in-a-vector-space" text="line segment" >}} $[a,b]$ (where $\lambda\in[0,1]$).

**Examples:**
- In $\mathbb{R}^2$, $L[a,b]$ is the usual straight line through $a$ and $b$.
- If $a=b$, then $L[a,a]=\{a\}$.
