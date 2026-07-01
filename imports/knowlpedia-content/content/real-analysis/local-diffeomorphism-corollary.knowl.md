+++
id = "real-analysis/local-diffeomorphism-corollary"
title = "Local diffeomorphism corollary"
kind = "knowl"
summary = "Nonvanishing Jacobian determinant implies a map is a diffeomorphism in a neighborhood of each point."
aliases = ["local-diffeomorphism-corollary", "Local diffeomorphism corollary"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/local-diffeomorphism-corollary.md"
+++

**Local diffeomorphism corollary:** Let $U\subseteq\mathbb R^k$ be an [[topology/open-set|open set]] and let $f:U\to\mathbb R^k$ be continuously differentiable. If $\det Df(x)\ne 0$ for every $x\in U$, then for each $x_0\in U$ there exist neighborhoods $A$ of $x_0$ and $B$ of $f(x_0)$ such that the restriction $f:A\to B$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]].

This is an immediate consequence of the [[real-analysis/inverse-function-theorem-rk|inverse function theorem]] applied at each point, and it is the standard meaning of saying that $f$ is a “local diffeomorphism.”
