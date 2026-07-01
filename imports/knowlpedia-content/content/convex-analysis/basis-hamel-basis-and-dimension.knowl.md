+++
id = "convex-analysis/basis-hamel-basis-and-dimension"
title = "Basis and dimension"
kind = "knowl"
summary = "A Hamel basis is a linearly independent set that spans the whole vector space"
aliases = ["basis-hamel-basis-and-dimension", "Basis and dimension"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/basis-hamel-basis-and-dimension.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] over $K$, and let $B\subset X$.

A set $B$ is a **basis** (also called a **Hamel basis**) of $X$ if:

1. $B$ is [[convex-analysis/linearly-independent-and-linearly-dependent-sets|linearly independent]], and
2. every $x\in X$ can be written as a finite linear combination of elements of $B$, i.e., there exist $m\in\mathbb{N}$, $x_1,\dots,x_m\in B$, and $\alpha_1,\dots,\alpha_m\in K$ such that
   $$
   x=\sum_{i=1}^m \alpha_i x_i.
   $$

If $X$ has a basis with finitely many elements, then $X$ is **finite-dimensional**, and the number of basis vectors is the **dimension** $\dim(X)$. If no finite basis exists, $X$ is **infinite-dimensional** (often written $\dim(X)=\infty$).

The existence of a Hamel basis in full generality uses set-theoretic choice; see [[convex-analysis/extension-of-a-linearly-independent-set-to-a-basis|extension to a basis]].

**Examples:**
- The set $\{e_1,\dots,e_n\}$ is a basis of $\mathbb{R}^n$, so $\dim(\mathbb{R}^n)=n$.
- The polynomials of degree $\le m$ form a vector space with basis $\{1,t,\dots,t^m\}$, so its dimension is $m+1$.
- The space of all sequences $s$ is infinite-dimensional (no finite set can generate all sequences by finite linear combinations).
