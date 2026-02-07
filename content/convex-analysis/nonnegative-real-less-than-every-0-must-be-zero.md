---
title: "A nonnegative real below every epsilon is zero"
description: "If ℓ≥0 and ℓ<ε for all ε>0, then ℓ=0"
---

**Lemma.**
Let $\ell\ge 0$ be a real number. If
$$
\ell<\varepsilon \quad\text{for every }\varepsilon>0,
$$

then $\ell=0$.

**Proof.** If $\ell>0$, choose $\varepsilon:=\ell/2>0$. Then $\varepsilon<\ell$, contradicting the assumption that $\ell<\varepsilon$ for every $\varepsilon>0$. Hence $\ell=0$.

This lemma is commonly used to conclude equality from estimates that hold for all $\varepsilon>0$, e.g. in {{< knowl id="uniqueness-of-limits-in-metric-spaces" text="uniqueness of limits" >}}.
