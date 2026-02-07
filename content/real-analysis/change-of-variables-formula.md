---
title: "Change of variables formula"
description: "A multivariable substitution rule involving the Jacobian determinant."
---

**Change of variables formula:** Let $U,V\subseteq\mathbb{R}^n$ be {{< knowl id="open-set" section="topology" text="open sets" >}} and let $\Phi:U\to V$ be a $C^1$ {{< knowl id="diffeomorphism" text="diffeomorphism" section="fiber-bundles">}}. If $f:V\to\mathbb{R}$ is such that the multiple Riemann integrals below exist (for example, if $f$ is continuous with compact support in $V$), then
$$
\int_V f(x)\,dx = \int_U f(\Phi(u))\,\bigl|\det D\Phi(u)\bigr|\,du,
$$

where $\det D\Phi(u)$ is the {{< knowl id="jacobian-determinant" text="Jacobian determinant" >}} of $\Phi$ at $u$.

This is the multivariable generalization of the one-dimensional {{< knowl id="substitution-rule" text="substitution rule" >}}, and it is fundamental for computing {{< knowl id="multiple-riemann-integral" text="multiple Riemann integrals" >}} under smooth coordinate changes.
