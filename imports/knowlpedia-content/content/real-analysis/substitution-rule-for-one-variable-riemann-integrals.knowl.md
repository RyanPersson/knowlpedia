+++
id = "real-analysis/substitution-rule-for-one-variable-riemann-integrals"
title = "Substitution rule (change of variables) for Riemann integrals"
kind = "knowl"
summary = "A one-dimensional change of variables formula for definite integrals"
aliases = ["substitution-rule-for-one-variable-riemann-integrals", "Substitution rule (change of variables) for Riemann integrals"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/substitution-rule-for-one-variable-riemann-integrals.md"
+++

**Substitution rule**: Let $f:[a,b]\to\mathbb{R}$ be [[real-analysis/continuity-on-a-set|continuous]], and let $\varphi:[\alpha,\beta]\to[a,b]$ be continuously [[real-analysis/differentiability-one-variable|differentiable]] and [[real-analysis/monotone-sequence|monotone]] on $[\alpha,\beta]$. Then
$
\int_\alpha^\beta f(\varphi(t))\,\varphi'(t)\,dt=\int_{\varphi(\alpha)}^{\varphi(\beta)} f(u)\,du.
$
(If $\varphi$ is decreasing, the right-hand side automatically changes sign because $\varphi(\alpha)>\varphi(\beta)$.)

This formula is the rigorous justification for substitution in calculus and is the one-dimensional prototype for higher-dimensional [[real-analysis/change-of-variables-formula|change of variables]].
