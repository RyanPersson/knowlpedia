---
title: "Slope inequalities for convex functions"
description: "Secant slopes of a convex function are ordered"
---

**Lemma.**
Let $f:I\to\mathbb{R}$ be a {{< knowl id="convex-function-via-epigraph" text="convex function" >}} on a nonempty interval $I\subset\mathbb{R}$. For any $a,b\in I$ with $a<b$ and any $x\in(a,b)$,
$$
\frac{f(x)-f(a)}{x-a}\;\le\;\frac{f(b)-f(a)}{b-a}\;\le\;\frac{f(b)-f(x)}{b-x}.
$$

**Context.** Convexity forces secant slopes to increase as you move to the right. This lemma is the key step in relating convexity to monotonicity of derivatives.

**Proof sketch.** Write $x=tb+(1-t)a$ with $t=(x-a)/(b-a)\in(0,1)$ and apply Jensen's inequality to compare $f(x)$ with the linear interpolation between $f(a)$ and $f(b)$; rearranging yields the slope bounds.
