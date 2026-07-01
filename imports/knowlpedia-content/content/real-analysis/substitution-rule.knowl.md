+++
id = "real-analysis/substitution-rule"
title = "Substitution rule"
kind = "knowl"
summary = "A change of variables formula for one-dimensional Riemann integrals."
aliases = ["substitution-rule", "Substitution rule"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/substitution-rule.md"
+++

**Substitution rule:** Let $\alpha<\beta$, let $\varphi:[\alpha,\beta]\to\mathbb{R}$ be continuously differentiable and strictly increasing, and set $a=\varphi(\alpha)$ and $b=\varphi(\beta)$. If $f:[a,b]\to\mathbb{R}$ is continuous, then
$$
\int_a^b f(x)\,dx = \int_\alpha^\beta f(\varphi(t))\,\varphi'(t)\,dt.
$$

This is the one-dimensional instance of the general [[real-analysis/change-of-variables-formula|change of variables formula]], and it is closely tied to the [[real-analysis/chain-rule|chain rule]] and [[real-analysis/fundamental-theorem-of-calculus-ii|fundamental theorem of calculus II]].
