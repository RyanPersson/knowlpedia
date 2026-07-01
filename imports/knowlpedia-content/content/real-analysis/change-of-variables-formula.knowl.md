+++
id = "real-analysis/change-of-variables-formula"
title = "Change of variables formula"
kind = "knowl"
summary = "A multivariable substitution rule involving the Jacobian determinant."
aliases = ["change-of-variables-formula", "Change of variables formula"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/change-of-variables-formula.md"
+++

**Change of variables formula:** Let $U,V\subseteq\mathbb{R}^n$ be [[topology/open-set|open sets]] and let $\Phi:U\to V$ be a $C^1$ [[fiber-bundles/diffeomorphism|diffeomorphism]]. If $f:V\to\mathbb{R}$ is such that the multiple Riemann integrals below exist (for example, if $f$ is continuous with compact support in $V$), then
$$
\int_V f(x)\,dx = \int_U f(\Phi(u))\,\bigl|\det D\Phi(u)\bigr|\,du,
$$

where $\det D\Phi(u)$ is the [[real-analysis/jacobian-determinant|Jacobian determinant]] of $\Phi$ at $u$.

This is the multivariable generalization of the one-dimensional [[real-analysis/substitution-rule|substitution rule]], and it is fundamental for computing [[real-analysis/multiple-riemann-integral|multiple Riemann integrals]] under smooth coordinate changes.
