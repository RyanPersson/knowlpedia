---
title: "Regular value and critical value"
description: "Values whose preimages contain only regular points, versus values hit at some critical point"
---

Let $U\subseteq \mathbb{R}^n$ be open and let $f:U\to \mathbb{R}^m$ be {{< knowl id="differentiable-map" text="differentiable" >}}.

A value $b\in \mathbb{R}^m$ is a **regular value** of $f$ if for every $a\in f^{-1}(\{b\})$ the point $a$ is a {{< knowl id="regular-point-critical-point-multivariable" text="regular point" >}}, i.e.
$\forall a\in U,\; f(a)=b \implies \operatorname{rank} Df(a)=m.$
A value $b$ is a **critical value** if it is not a regular value; equivalently, there exists $a\in U$ such that $f(a)=b$ and $\operatorname{rank}Df(a)<m$.

Regular values are those at which the level set $f^{-1}(b)$ is expected to be a smooth $(n-m)$-dimensional set (under appropriate hypotheses). Critical values correspond to "singular" level sets.

**Examples:**
- For $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x^2+y^2$, the value $0$ is a critical value (attained at the critical point $(0,0)$), while every $b>0$ is a regular value.
- For $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^3$, the value $0$ is a critical value since $f'(0)=0$ and $f(0)=0$; any $b\neq 0$ is a regular value.
