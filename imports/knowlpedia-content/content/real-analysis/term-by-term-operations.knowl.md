+++
id = "real-analysis/term-by-term-operations"
title = "Term-by-term operations for power series"
kind = "knowl"
summary = "Within the common disk of convergence, power series can be added, scaled, and multiplied by operating on coefficients."
aliases = ["term-by-term-operations", "Term-by-term operations for power series"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/term-by-term-operations.md"
+++

**Term-by-term operations for power series:** Let
\[
\sum_{n=0}^\infty a_n (x-x_0)^n
\quad\text{and}\quad
\sum_{n=0}^\infty b_n (x-x_0)^n
\]
be [[real-analysis/power-series|power series]] with radii of convergence $R_a$ and $R_b$. Set $R=\min(R_a,R_b)$. Then for every $|x-x_0|<R$:

- (Addition and scalar multiplication) The series $\sum_{n=0}^\infty (a_n+b_n)(x-x_0)^n$ and $\sum_{n=0}^\infty (\lambda a_n)(x-x_0)^n$ converge, and
  $$
  \sum_{n=0}^\infty (a_n+b_n)(x-x_0)^n = \sum_{n=0}^\infty a_n(x-x_0)^n + \sum_{n=0}^\infty b_n(x-x_0)^n.
  $$

- (Multiplication) If $c_n=\sum_{k=0}^n a_k b_{n-k}$ (the coefficient [[real-analysis/cauchy-product|Cauchy product]]), then $\sum_{n=0}^\infty c_n (x-x_0)^n$ converges and equals the product of the two sums:
  $$
  \left(\sum_{n=0}^\infty a_n(x-x_0)^n\right)\left(\sum_{n=0}^\infty b_n(x-x_0)^n\right) = \sum_{n=0}^\infty c_n(x-x_0)^n.
  $$

These operations justify treating power series like “infinite polynomials” on their common disk of convergence and connect directly to results on [[real-analysis/term-by-term-differentiation|term-by-term differentiation]] and [[real-analysis/term-by-term-integration|term-by-term integration]].
