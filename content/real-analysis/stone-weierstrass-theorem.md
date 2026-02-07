---
title: "Stone–Weierstrass theorem"
description: "A subalgebra of continuous functions on a compact space that separates points and contains constants is dense in the full algebra."
---

**Stone–Weierstrass theorem:** Let $K$ be a compact Hausdorff {{< knowl id="topological-space" section="topology" text="topological space" >}} and let $C(K,\mathbb{R})$ denote the real-valued continuous functions on $K$. Let $A\subseteq C(K,\mathbb{R})$ be a {{< knowl id="subalgebra-of-continuous-functions" text="subalgebra" >}} that contains the constant functions and {{< knowl id="separates-points" text="separates points" >}} of $K$. Then $A$ is dense in $C(K,\mathbb{R})$ with respect to the {{< knowl id="supremum-norm" text="supremum norm" >}}: for every $f\in C(K,\mathbb{R})$ and every $\varepsilon>0$ there exists $g\in A$ such that
\[
\sup_{x\in K}|f(x)-g(x)|<\varepsilon.
\]

This theorem explains many uniform approximation results as density statements in the {{< knowl id="space-of-continuous-functions" text="space of continuous functions" >}}; for example, the {{< knowl id="weierstrass-approximation-theorem" text="Weierstrass approximation theorem" >}} arises from a suitable choice of $K$ and $A$.
