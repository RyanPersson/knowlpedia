+++
id = "convex-analysis/nonnegative-real-less-than-every-0-must-be-zero"
title = "A nonnegative real below every epsilon is zero"
kind = "knowl"
summary = "If ℓ≥0 and ℓ<ε for all ε>0, then ℓ=0"
aliases = ["nonnegative-real-less-than-every-0-must-be-zero", "A nonnegative real below every epsilon is zero"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/nonnegative-real-less-than-every-0-must-be-zero.md"
+++

**Lemma.**
Let $\ell\ge 0$ be a real number. If
$$
\ell<\varepsilon \quad\text{for every }\varepsilon>0,
$$

then $\ell=0$.

**Proof.** If $\ell>0$, choose $\varepsilon:=\ell/2>0$. Then $\varepsilon<\ell$, contradicting the assumption that $\ell<\varepsilon$ for every $\varepsilon>0$. Hence $\ell=0$.

This lemma is commonly used to conclude equality from estimates that hold for all $\varepsilon>0$, e.g. in [[convex-analysis/uniqueness-of-limits-in-metric-spaces|uniqueness of limits]].
