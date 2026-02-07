---
title: "Jensen's inequality for integrals"
description: "A convexity inequality comparing a convex function of an average with the average of a convex function."
---

**Jensen's inequality (integral form):** Let $(X,\Sigma,\mu)$ be a measure space with $\mu(X)=1$. Let $I\subseteq\mathbb R$ be an interval, let $f:X\to I$ be measurable and integrable, and let $\varphi:I\to\mathbb R$ be convex. If $\varphi\circ f$ is integrable, then
\[
\varphi\Big(\int_X f\,d\mu\Big)\le \int_X \varphi(f)\,d\mu.
\]

This is a fundamental inequality for {{< knowl id="convex-function-via-epigraph" section="convex-analysis" text="convex functions" >}} applied to the {{< knowl id="lebesgue-integral" text="Lebesgue integral" >}}, often used with $f$ in {{< knowl id="l1-function" text="L1" >}} and $\varphi\circ f$ integrable. It can be viewed as a measure-theoretic extension of finite-dimensional convexity to averages taken with respect to a {{< knowl id="measure" text="measure" >}} on a {{< knowl id="measure-space" text="measure space" >}}.
