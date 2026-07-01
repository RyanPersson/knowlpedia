+++
id = "convex-analysis/bounded-linear-functional-norm-of-a-functional"
title = "Bounded Linear Functional and Its Norm"
kind = "knowl"
summary = "A linear functional is bounded iff it is continuous; its operator norm is sup_{||x||≤1}|f(x)|."
aliases = ["bounded-linear-functional-norm-of-a-functional", "Bounded Linear Functional and Its Norm"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/bounded-linear-functional-norm-of-a-functional.md"
+++

Let $X$ be a [[convex-analysis/norm-normed-vector-space|normed space]] over $\mathbb{R}$ or $\mathbb{C}$. A [[convex-analysis/linear-operator-linear-transformation|linear map]] $f:X\to\mathbb{K}$ (where $\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}$) is a **linear functional**.

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

This notion is used in [[convex-analysis/hahn-banach-theorem-in-normed-spaces|Hahn–Banach in normed spaces]] and in separation results such as [[convex-analysis/separation-of-a-point-and-a-subspace|separating a point and a subspace]].

**Examples:**
- On $X=\mathbb{R}^n$ with the Euclidean norm, $f(x)=\langle a,x\rangle$ is bounded and $\|f\|=\|a\|_2$.
- If $X=C[0,1]$ with $\|\cdot\|_\infty$, then $f(x)=x(t_0)$ is bounded with $\|f\|=1$.
