+++
id = "convex-analysis/codimension"
title = "Codimension"
kind = "knowl"
summary = "The dimension of the quotient space X/L for a subspace L⊂X."
aliases = ["codimension"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/codimension.md"
+++

Let $X$ be a [[linear-algebra/vector-space|vector space]] and let $L\subset X$ be a [[convex-analysis/linear-subspace|linear subspace]]. The **codimension** of $L$ in $X$ is
$$
\operatorname{codim}(L):=\dim(X/L),
$$

where $X/L$ is the [[convex-analysis/quotient-vector-space-codimension|quotient space]] of $X$ by $L$.

Codimension measures "how many independent linear constraints" define $L$. Codimension one subspaces play a special role in the geometry of [[convex-analysis/hyperplane|hyperplanes]].

**Examples:**
- In $\mathbb{R}^n$, a hyperplane through the origin has codimension $1$.
- If $L=\{0\}$ and $\dim X=n<\infty$, then $\operatorname{codim}(L)=n$.
