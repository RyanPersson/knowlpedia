+++
id = "real-analysis/critical-value"
title = "Critical value"
kind = "knowl"
summary = "A value attained at some point where the derivative is not surjective"
aliases = ["critical-value", "Critical value"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/critical-value.md"
+++

A **critical value** of a differentiable map $F:U\to \mathbb{R}^m$ (with $U\subseteq \mathbb{R}^n$ and $m\le n$) is a point $y\in \mathbb{R}^m$ for which there exists $a\in U$ with $F(a)=y$ such that $a$ is not a [[real-analysis/regular-point|regular point]] of $F$.

Equivalently, $y$ is critical if the fiber $F^{-1}(\{y\})$ contains at least one point where the [[real-analysis/jacobian-matrix|Jacobian matrix]] fails to have full rank. Values that are not critical are precisely the [[fiber-bundles/regular-value|regular values]].

**Examples:**
- For $F(x,y)=x^2+y^2$, the value $0$ is a critical value, since $F^{-1}(\{0\})=\{(0,0)\}$ and the derivative is not surjective at $(0,0)$.
- For $F(x)=x^3$ as a map $\mathbb{R}\to\mathbb{R}$, the value $0$ is a critical value because $F'(0)=0$.
