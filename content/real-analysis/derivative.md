---
title: "Derivative"
description: "The limit of the difference quotient, measuring instantaneous rate of change."
---

A **derivative** is the number $f'(a)$ defined for a {{< knowl id="function" section="shared-foundations" text="function" >}} $f:I\to\mathbb{R}$ at a point $a\in I$ by
$f'(a)=\lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$, provided this limit exists.

This is a special instance of a {{< knowl id="limit-at-a-point" text="limit at a point" >}} applied to the difference quotient. Existence of the derivative is the basic notion behind {{< knowl id="differentiability-1d" text="differentiability in one variable" >}}, and it implies continuity via {{< knowl id="differentiability-implies-continuity" text="differentiability implies continuity" >}}.

**Examples:**
- For $f(x)=x^2$, the derivative exists everywhere and $f'(x)=2x$.
- For $f(x)=|x|$, the derivative does not exist at $a=0$.
