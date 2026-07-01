+++
id = "convex-analysis/convex-duality-primal-dual"
title = "Convex duality: primal and dual problems"
kind = "knowl"
summary = "Primal and dual convex optimization problems and the relationship between their optimal values."
aliases = ["convex-duality-primal-dual", "Convex duality: primal and dual problems"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-duality-primal-dual.md"
+++

A **primal-dual pair** in convex optimization is a pair of problems built from convex objectives so that the dual objective gives a universal lower bound on the primal optimal value. A common (Fenchel) form starts from convex [[shared-foundations/function|functions]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ and $g:\mathbb{R}^m\to(-\infty,+\infty]$ and a linear map $A:\mathbb{R}^n\to\mathbb{R}^m$, and defines
$$
p^\star=\inf_{x\in\mathbb{R}^n}\,\bigl(f(x)+g(Ax)\bigr),\qquad
d^\star=\sup_{y\in\mathbb{R}^m}\,\bigl(-f^*(A^\top y)-g^*(-y)\bigr),
$$

where $f^*$ and $g^*$ are [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugates]] and $p^\star,d^\star$ use [[real-analysis/infimum|infimum]] and [[real-analysis/supremum|supremum]]. The inequality $d^\star\le p^\star$ (weak duality) follows from the [[convex-analysis/fenchel-young-inequality|Fenchel-Young inequality]], and under suitable regularity conditions one has strong duality $d^\star=p^\star$, often certified by [[convex-analysis/subgradient|subgradient]] conditions.

**Examples:**
- Equality constraints can be encoded by choosing $g(u)$ to be $0$ when $u=b$ and $+\infty$ otherwise, turning $p^\star=\inf\{f(x):Ax=b\}$ into a dual of the form $\sup_y\{\langle b,y\rangle-f^*(A^\top y)\}$.
- The Lasso objective $\inf_x\left(\lambda\|x\|_1+\tfrac12\|Ax-b\|_2^2\right)$ has a Fenchel dual $\sup_y\left(\langle b,y\rangle-\tfrac12\|y\|_2^2\right)$ subject to the constraint $\|A^\top y\|_\infty\le \lambda$, because the conjugate of $\lambda\|x\|_1$ is an indicator of an $\ell_\infty$-ball.
