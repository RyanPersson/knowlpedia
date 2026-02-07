---
title: "Bounded Linear Functional and Its Norm"
description: "A linear functional is bounded iff it is continuous; its operator norm is sup_{||x||≤1}|f(x)|."
---

Let $X$ be a {{< knowl id="norm-normed-vector-space" text="normed space" >}} over $\mathbb{R}$ or $\mathbb{C}$. A {{< knowl id="linear-operator-linear-transformation" text="linear map" >}} $f:X\to\mathbb{K}$ (where $\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}$) is a **linear functional**.

The functional $f$ is **bounded** if there exists $M>0$ such that
$$
|f(x)|\le M\|x\|\quad\text{for all }x\in X.
$$
In normed spaces, boundedness is equivalent to continuity.

The **norm** (operator norm) of $f$ is
$$
\|f\|:=\sup_{\|x\|\le 1}|f(x)|.
$$

Equivalently, $\|f\|=\inf\{M>0: |f(x)|\le M\|x\|\ \forall x\}$.

This notion is used in {{< knowl id="hahn-banach-theorem-in-normed-spaces" text="Hahn–Banach in normed spaces" >}} and in separation results such as {{< knowl id="separation-of-a-point-and-a-subspace" text="separating a point and a subspace" >}}.

**Examples:**
- On $X=\mathbb{R}^n$ with the Euclidean norm, $f(x)=\langle a,x\rangle$ is bounded and $\|f\|=\|a\|_2$.
- If $X=C[0,1]$ with $\|\cdot\|_\infty$, then $f(x)=x(t_0)$ is bounded with $\|f\|=1$.
