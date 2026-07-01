+++
id = "measure-theory/jensen-inequality-integral"
title = "Jensen's inequality for integrals"
kind = "knowl"
summary = "A convexity inequality comparing a convex function of an average with the average of a convex function."
aliases = ["jensen-inequality-integral", "Jensen's inequality for integrals"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/jensen-inequality-integral.md"
+++

**Jensen's inequality (integral form):** Let $(X,\Sigma,\mu)$ be a measure space with $\mu(X)=1$. Let $I\subseteq\mathbb R$ be an interval, let $f:X\to I$ be measurable and integrable, and let $\varphi:I\to\mathbb R$ be convex. If $\varphi\circ f$ is integrable, then
\[
\varphi\Big(\int_X f\,d\mu\Big)\le \int_X \varphi(f)\,d\mu.
\]

This is a fundamental inequality for [[convex-analysis/convex-function-via-epigraph|convex functions]] applied to the [[measure-theory/lebesgue-integral|Lebesgue integral]], often used with $f$ in [[measure-theory/l1-function|L1]] and $\varphi\circ f$ integrable. It can be viewed as a measure-theoretic extension of finite-dimensional convexity to averages taken with respect to a [[measure-theory/measure|measure]] on a [[measure-theory/measure-space|measure space]].
