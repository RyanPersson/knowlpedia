---
title: "Simple function"
description: "A measurable function that takes only finitely many values."
---

A **simple function** on a measurable space $(X,\Sigma)$ is a {{< knowl id="measurable-function" text="measurable function" >}} $s:X\to \mathbb R$ (or into $[0,\infty]$) that takes only finitely many distinct values; equivalently, $s$ can be written as $s=\sum_{k=1}^n a_k\,\mathbf 1_{A_k}$ for some real numbers $a_k$ and some {{< knowl id="measurable-set" text="measurable sets" >}} $A_k\in\Sigma$.

Simple functions are the standard starting point for defining integration (they are finite linear combinations of {{< knowl id="indicator-function" text="indicator functions" >}}). More complicated measurable functions are often approximated by increasing sequences of simple functions.

**Examples:**
- A step function on $\mathbb R$ that is constant on finitely many {{< knowl id="interval" section="real-analysis" text="intervals" >}} and zero elsewhere is a simple function (with respect to the Borel sigma-algebra).
- If $A,B$ are measurable sets in $(X,\Sigma)$, then $2\,\mathbf 1_A - 3\,\mathbf 1_B$ is a simple function.
