+++
id = "real-analysis/separates-points"
title = "Separates points"
kind = "knowl"
summary = "A property of a family of functions distinguishing any two different points."
aliases = ["separates-points", "Separates points"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/separates-points.md"
+++

A family $\mathcal{F}$ of functions on a set $X$ **separates points** if for every pair of distinct points $x,y\in X$ there exists $f\in\mathcal{F}$ such that $f(x)\ne f(y)$.

This property is often imposed on a [[real-analysis/subalgebra-of-continuous-functions|subalgebra of continuous functions]] in approximation theorems, notably the [[real-analysis/stone-weierstrass-theorem|Stone–Weierstrass theorem]]. Intuitively, separating points means the family contains enough [[shared-foundations/function|functions]] to distinguish elements of $X$ by their images.

**Examples:**
- The set of real [[real-analysis/polynomial|polynomials]] restricted to $[a,b]$ separates points of $[a,b]$ (if $x\ne y$, the polynomial $p(t)=t$ already satisfies $p(x)\ne p(y)$).
- The family of constant functions on $X$ does not separate points (all constants take the same value at every point).
