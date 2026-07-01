+++
id = "convex-analysis/linearly-independent-and-linearly-dependent-sets"
title = "Linear independence and dependence"
kind = "knowl"
summary = "A set is linearly independent if only the trivial finite linear combination equals zero"
aliases = ["linearly-independent-and-linearly-dependent-sets", "Linear independence and dependence"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/linearly-independent-and-linearly-dependent-sets.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] over $K$, and let $M\subset X$.

The set $M$ is **linearly independent** if for every finite subset $\{x_1,\dots,x_m\}\subset M$ and every choice of scalars $\alpha_1,\dots,\alpha_m\in K$,
$$
\sum_{i=1}^m \alpha_i x_i = 0 \quad\Longrightarrow\quad \alpha_1=\cdots=\alpha_m=0.
$$

If $M$ is not linearly independent, it is **linearly dependent**, i.e., there exists a finite subset and scalars, not all zero, giving a zero [[convex-analysis/linear-combination|linear combination]].

Linear independence is one of the two defining properties of a [[convex-analysis/basis-hamel-basis-and-dimension|basis]].

**Examples:**
- The standard unit vectors $e_1,\dots,e_n$ in $\mathbb{R}^n$ are linearly independent.
- The set $\{(1,0),(2,0)\}\subset\mathbb{R}^2$ is linearly dependent since $2(1,0)-(2,0)=0$.
- Any set containing the zero vector is linearly dependent: if $0\in M$, then $1\cdot 0=0$ is a nontrivial dependence.
- The empty set is linearly independent (there is no finite nonempty subset to witness dependence).
