+++
id = "real-analysis/subalgebra-of-continuous-functions"
title = "Subalgebra of continuous functions"
kind = "knowl"
summary = "A subset of continuous functions closed under linear combinations and pointwise products."
aliases = ["subalgebra-of-continuous-functions", "Subalgebra of continuous functions"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/subalgebra-of-continuous-functions.md"
+++

A **subalgebra of continuous functions** on a [[topology/topological-space|topological space]] $X$ is a subset $A\subseteq C(X)$ (where $C(X)$ is the [[real-analysis/space-of-continuous-functions|space of continuous functions]]) such that whenever $f,g\in A$ and $\alpha,\beta\in\mathbb{R}$, the functions $\alpha f+\beta g$ and $f\cdot g$ (pointwise product) also belong to $A$. If $A$ contains the constant function $1$, it is called a unital subalgebra.

With pointwise operations, $C(X)$ is a commutative [[algebra-rings/ring|ring]], and a subalgebra is a subset stable under the same structure. Subalgebras that [[real-analysis/separates-points|separate points]] are central in the [[real-analysis/stone-weierstrass-theorem|Stone–Weierstrass theorem]].

**Examples:**
- On a closed interval $[a,b]$, the set of restrictions of real [[real-analysis/polynomial|polynomials]] to $[a,b]$ is a subalgebra of $C([a,b])$.
- On $[-1,1]$, the set of even continuous functions $\{f\in C([-1,1]) : f(x)=f(-x)\}$ is a subalgebra of $C([-1,1])$.
