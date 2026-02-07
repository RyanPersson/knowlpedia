---
title: "Critical value"
description: "A value attained at some point where the derivative is not surjective"
---

A **critical value** of a differentiable map $F:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$ and $m\le n$) is a point $y\in \mathbb{R}^m$ for which there exists $a\in U$ with $F(a)=y$ such that $a$ is not a {{< knowl id="regular-point" text="regular point" >}} of $F$.

Equivalently, $y$ is critical if the fiber $F^{-1}(\{y\})$ contains at least one point where the {{< knowl id="jacobian-matrix" text="Jacobian matrix" >}} fails to have full rank. Values that are not critical are precisely the {{< knowl id="regular-value" text="regular values" section="fiber-bundles">}}.

**Examples:**
- For $F(x,y)=x^2+y^2$, the value $0$ is a critical value, since $F^{-1}(\{0\})=\{(0,0)\}$ and the derivative is not surjective at $(0,0)$.
- For $F(x)=x^3$ as a map $\mathbb{R}\to\mathbb{R}$, the value $0$ is a critical value because $F'(0)=0$.
