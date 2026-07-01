+++
id = "real-analysis/derivative"
title = "Derivative"
kind = "knowl"
summary = "The limit of the difference quotient, measuring instantaneous rate of change."
aliases = ["derivative"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/derivative.md"
+++

A **derivative** is the number $f'(a)$ defined for a [[shared-foundations/function|function]] $f:I\to\mathbb{R}$ at a point $a\in I$ by
$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$, provided this limit exists.

This is a special instance of a [[real-analysis/limit-at-a-point|limit at a point]] applied to the difference quotient. Existence of the derivative is the basic notion behind [[real-analysis/differentiability-1d|differentiability in one variable]], and it implies continuity via [[real-analysis/differentiability-implies-continuity|differentiability implies continuity]].

**Examples:**
- For $f(x)=x^2$, the derivative exists everywhere and $f'(x)=2x$.
- For $f(x)=|x|$, the derivative does not exist at $a=0$.
