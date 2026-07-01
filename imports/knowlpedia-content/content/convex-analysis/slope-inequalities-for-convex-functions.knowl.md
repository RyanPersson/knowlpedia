+++
id = "convex-analysis/slope-inequalities-for-convex-functions"
title = "Slope inequalities for convex functions"
kind = "knowl"
summary = "Secant slopes of a convex function are ordered"
aliases = ["slope-inequalities-for-convex-functions", "Slope inequalities for convex functions"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/slope-inequalities-for-convex-functions.md"
+++

**Lemma.**
Let $f:I\to\mathbb{R}$ be a [[convex-analysis/convex-function-via-epigraph|convex function]] on a nonempty interval $I\subset\mathbb{R}$. For any $a,b\in I$ with $a<b$ and any $x\in(a,b)$,
$$
\frac{f(x)-f(a)}{x-a}\;\le\;\frac{f(b)-f(a)}{b-a}\;\le\;\frac{f(b)-f(x)}{b-x}.
$$

**Context.** Convexity forces secant slopes to increase as you move to the right. This lemma is the key step in relating convexity to monotonicity of derivatives.

**Proof sketch.** Write $x=tb+(1-t)a$ with $t=(x-a)/(b-a)\in(0,1)$ and apply Jensen's inequality to compare $f(x)$ with the linear interpolation between $f(a)$ and $f(b)$; rearranging yields the slope bounds.
