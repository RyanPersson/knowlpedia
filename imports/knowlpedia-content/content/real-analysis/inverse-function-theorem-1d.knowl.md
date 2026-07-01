+++
id = "real-analysis/inverse-function-theorem-1d"
title = "Inverse function theorem in one dimension"
kind = "knowl"
summary = "A differentiable function with nonzero derivative has a differentiable local inverse."
aliases = ["inverse-function-theorem-1d", "Inverse function theorem in one dimension"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/inverse-function-theorem-1d.md"
+++

**Inverse function theorem (1D):** Let $I\subseteq\mathbb{R}$ be an open interval and let $f:I\to\mathbb{R}$ be continuously differentiable. Fix $x_0\in I$ with $f'(x_0)\neq 0$. Then there exist open intervals $J\subseteq I$ and $K\subseteq\mathbb{R}$ with $x_0\in J$ and $f(x_0)\in K$ such that:

1. The restriction $f|_J:J\to K$ is bijective, so it has an [[shared-foundations/inverse-function|inverse function]] $g:K\to J$.
2. The inverse $g$ is continuously differentiable on $K$, and for all $y\in K$,
   $$
   g'(y)=\frac{1}{f'(g(y))}.
   $$

   In particular, $g'(f(x_0))=1/f'(x_0)$.

This result combines [[real-analysis/derivative-sign-implies-monotonicity|local monotonicity from the derivative]] with the [[real-analysis/chain-rule|chain rule]] applied to $f\circ g=\mathrm{id}$. It is the one-dimensional case of the [[real-analysis/inverse-function-theorem-rk|inverse function theorem in higher dimensions]].
