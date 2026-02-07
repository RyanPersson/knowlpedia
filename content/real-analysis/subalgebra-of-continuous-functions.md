---
title: "Subalgebra of continuous functions"
description: "A subset of continuous functions closed under linear combinations and pointwise products."
---

A **subalgebra of continuous functions** on a {{< knowl id="topological-space" section="topology" text="topological space" >}} $X$ is a subset $A\subseteq C(X)$ (where $C(X)$ is the {{< knowl id="space-of-continuous-functions" text="space of continuous functions" >}}) such that whenever $f,g\in A$ and $\alpha,\beta\in\mathbb{R}$, the functions $\alpha f+\beta g$ and $f\cdot g$ (pointwise product) also belong to $A$. If $A$ contains the constant function $1$, it is called a unital subalgebra.

With pointwise operations, $C(X)$ is a commutative {{< knowl id="ring" section="algebra-rings" text="ring" >}}, and a subalgebra is a subset stable under the same structure. Subalgebras that {{< knowl id="separates-points" text="separate points" >}} are central in the {{< knowl id="stone-weierstrass-theorem" text="Stone–Weierstrass theorem" >}}.

**Examples:**
- On a closed interval $[a,b]$, the set of restrictions of real {{< knowl id="polynomial" text="polynomials" >}} to $[a,b]$ is a subalgebra of $C([a,b])$.
- On $[-1,1]$, the set of even continuous functions $\{f\in C([-1,1]) : f(x)=f(-x)\}$ is a subalgebra of $C([-1,1])$.
