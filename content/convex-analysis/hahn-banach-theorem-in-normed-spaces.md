---
title: "Hahn–Banach Theorem in Normed Spaces"
description: "A bounded linear functional on a subspace extends to the whole space without increasing its norm."
---

Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed space" >}}, let $Y\subset X$ be a {{< knowl id="linear-subspace" text="subspace" >}}, and let $f:Y\to\mathbb{K}$ be a {{< knowl id="bounded-linear-functional-norm-of-a-functional" text="bounded linear functional" >}}.

**Theorem (Hahn–Banach, normed spaces)**: There exists a bounded linear functional $F:X\to\mathbb{K}$ such that
- $F|_Y=f$, and
- $\|F\|=\|f\|$.

**Context:**
This is obtained by applying {{< knowl id="hahn-banach-extension-dominated-by-a-seminorm-real-case" text="the seminorm version of Hahn–Banach" >}} with the {{< knowl id="seminorm" text="seminorm" >}} $p(x)=\|f\|\|x\|$. It is one of the main tools for constructing supporting functionals and proving geometric separation theorems in normed spaces.
