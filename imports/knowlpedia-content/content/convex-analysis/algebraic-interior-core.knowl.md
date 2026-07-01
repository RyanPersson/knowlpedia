+++
id = "convex-analysis/algebraic-interior-core"
title = "Algebraic Interior (Core)"
kind = "knowl"
summary = "The algebraic analogue of interior for subsets of vector spaces"
aliases = ["algebraic-interior-core", "Algebraic Interior (Core)"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/algebraic-interior-core.md"
+++

Let $X$ be a real [[linear-algebra/vector-space|vector space]] and let $\Omega\subset X$.

The **algebraic interior** (or **core**) of $\Omega$ is
$$
\operatorname{core}(\Omega):=\Big\{x\in\Omega \ \Big|\ \forall v\in X,\ \exists \delta>0\ \text{s.t.}\ x+tv\in\Omega\ \text{for all }|t|<\delta\Big\}.
$$

Equivalently, $x\in\operatorname{core}(\Omega)$ iff for every direction $v\in X$, one can move a small amount from $x$ in the direction $v$ and remain in $\Omega$.

When $X$ is a [[convex-analysis/norm-normed-vector-space|normed vector space]] and $\Omega$ is [[convex-analysis/convex-set|convex]], we have
$$
\operatorname{int}(\Omega)\subset \operatorname{core}(\Omega)\subset \Omega,
$$

where $\operatorname{int}(\Omega)$ is the usual [[convex-analysis/interior-of-a-set|interior]]. See also [[convex-analysis/linear-closure|linear closure]] for the dual notion.

**Examples:**
- If $\Omega$ is an open ball in a normed space, then $\operatorname{core}(\Omega)=\Omega$.
- If $\Omega$ is a linear subspace $L$, then $\operatorname{core}(L)=L$.
