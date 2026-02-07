---
title: "Implicitly defined function"
description: "A function specified indirectly by an equation involving its inputs and outputs"
---

An **implicitly defined function** is a function whose values are determined (locally) by an equation of the form
$$
F(x,y)=0,
$$

where $F$ is a function on a subset of $\mathbb{R}^{n+m}$, $x\in\mathbb{R}^n$ is viewed as the input, and $y\in\mathbb{R}^m$ is viewed as the output.

Typically, one seeks a function $\varphi$ such that $y=\varphi(x)$ and $F(x,\varphi(x))=0$ holds for $x$ near a point. The existence and differentiability of such a $\varphi$ are ensured under standard hypotheses by the {{< knowl id="implicit-function-theorem" text="implicit function theorem" >}}, often stated using the notion of a {{< knowl id="regular-point" text="regular point" >}} of $F$ (or, equivalently, invertibility of an appropriate Jacobian block).

**Examples:**
- The equation $x^2+y^2-1=0$ implicitly defines $y=\sqrt{1-x^2}$ near the point $(0,1)$ (and $y=-\sqrt{1-x^2}$ near $(0,-1)$).
- The equation $x+y+z=0$ implicitly defines $z=-(x+y)$ as a function of $(x,y)$ on all of $\mathbb{R}^2$.
