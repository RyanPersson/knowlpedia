---
title: "Separates points"
description: "A property of a family of functions distinguishing any two different points."
---

A family $\mathcal{F}$ of functions on a set $X$ **separates points** if for every pair of distinct points $x,y\in X$ there exists $f\in\mathcal{F}$ such that $f(x)\ne f(y)$.

This property is often imposed on a {{< knowl id="subalgebra-of-continuous-functions" text="subalgebra of continuous functions" >}} in approximation theorems, notably the {{< knowl id="stone-weierstrass-theorem" text="Stone–Weierstrass theorem" >}}. Intuitively, separating points means the family contains enough {{< knowl id="function" section="shared-foundations" text="functions" >}} to distinguish elements of $X$ by their images.

**Examples:**
- The set of real {{< knowl id="polynomial" text="polynomials" >}} restricted to $[a,b]$ separates points of $[a,b]$ (if $x\ne y$, the polynomial $p(t)=t$ already satisfies $p(x)\ne p(y)$).
- The family of constant functions on $X$ does not separate points (all constants take the same value at every point).
