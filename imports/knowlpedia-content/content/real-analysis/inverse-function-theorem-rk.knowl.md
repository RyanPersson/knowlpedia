+++
id = "real-analysis/inverse-function-theorem-rk"
title = "Inverse function theorem in R^k"
kind = "knowl"
summary = "A map with invertible derivative at a point has a differentiable local inverse."
aliases = ["inverse-function-theorem-rk", "Inverse function theorem in R^k"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/inverse-function-theorem-rk.md"
+++

**Inverse function theorem in $\mathbb R^k$:** Let $U\subseteq\mathbb R^k$ be an [[topology/open-set|open set]] and let $f:U\to\mathbb R^k$ be continuously differentiable. If the [[real-analysis/jacobian-determinant|Jacobian determinant]] $\det Df(a)$ is nonzero at some $a\in U$, then there exist neighborhoods $A$ of $a$ and $B$ of $f(a)$ such that $f$ restricts to a bijection $f:A\to B$ whose inverse $f^{-1}:B\to A$ is continuously differentiable. Moreover,
$$
D(f^{-1})(f(a))=(Df(a))^{-1}.
$$

Thus, near $a$, the map $f$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]] onto its image; in particular it is a local [[topology/homeomorphism|homeomorphism]].
