+++
id = "real-analysis/stone-weierstrass-theorem"
title = "Stone–Weierstrass theorem"
kind = "knowl"
summary = "A subalgebra of continuous functions on a compact space that separates points and contains constants is dense in the full algebra."
aliases = ["stone-weierstrass-theorem", "Stone–Weierstrass theorem"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/stone-weierstrass-theorem.md"
+++

**Stone–Weierstrass theorem:** Let $K$ be a compact Hausdorff [[topology/topological-space|topological space]] and let $C(K,\mathbb{R})$ denote the real-valued continuous functions on $K$. Let $A\subseteq C(K,\mathbb{R})$ be a [[real-analysis/subalgebra-of-continuous-functions|subalgebra]] that contains the constant functions and [[real-analysis/separates-points|separates points]] of $K$. Then $A$ is dense in $C(K,\mathbb{R})$ with respect to the [[real-analysis/supremum-norm|supremum norm]]: for every $f\in C(K,\mathbb{R})$ and every $\varepsilon>0$ there exists $g\in A$ such that
\[
\sup_{x\in K}|f(x)-g(x)|<\varepsilon.
\]

This theorem explains many uniform approximation results as density statements in the [[real-analysis/space-of-continuous-functions|space of continuous functions]]; for example, the [[real-analysis/weierstrass-approximation-theorem|Weierstrass approximation theorem]] arises from a suitable choice of $K$ and $A$.
