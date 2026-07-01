+++
id = "real-analysis/implicitly-defined-function"
title = "Implicitly defined function"
kind = "knowl"
summary = "A function specified indirectly by an equation involving its inputs and outputs"
aliases = ["implicitly-defined-function", "Implicitly defined function"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/implicitly-defined-function.md"
+++

An **implicitly defined function** is a function whose values are determined (locally) by an equation of the form
$$
F(x,y)=0,
$$

where $F$ is a function on a subset of $\mathbb{R}^{n+m}$, $x\in\mathbb{R}^n$ is viewed as the input, and $y\in\mathbb{R}^m$ is viewed as the output.

Typically, one seeks a function $\varphi$ such that $y=\varphi(x)$ and $F(x,\varphi(x))=0$ holds for $x$ near a point. The existence and differentiability of such a $\varphi$ are ensured under standard hypotheses by the [[real-analysis/implicit-function-theorem|implicit function theorem]], often stated using the notion of a [[real-analysis/regular-point|regular point]] of $F$ (or, equivalently, invertibility of an appropriate Jacobian block).

**Examples:**
- The equation $x^2+y^2-1=0$ implicitly defines $y=\sqrt{1-x^2}$ near the point $(0,1)$ (and $y=-\sqrt{1-x^2}$ near $(0,-1)$).
- The equation $x+y+z=0$ implicitly defines $z=-(x+y)$ as a function of $(x,y)$ on all of $\mathbb{R}^2$.
