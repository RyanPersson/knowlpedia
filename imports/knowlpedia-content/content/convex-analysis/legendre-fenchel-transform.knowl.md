+++
id = "convex-analysis/legendre-fenchel-transform"
title = "Legendre–Fenchel transform"
kind = "knowl"
summary = "The general convex-conjugation transform defined by a supremum pairing, without smoothness assumptions."
aliases = ["legendre-fenchel-transform", "Legendre–Fenchel transform"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/legendre-fenchel-transform.md"
+++

A **Legendre–Fenchel transform** of an extended-real-valued [[shared-foundations/function|function]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function $f^*:\mathbb{R}^n\to(-\infty,+\infty]$ defined by
$$
f^*(y) \;=\; \sup_{x\in\mathbb{R}^n}\big(\langle y,x\rangle - f(x)\big).
$$

This is exactly the [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]; the “Legendre” terminology is common even when $f$ is not differentiable, and it underlies [[convex-analysis/fenchel-young-inequality|Fenchel–Young inequality]] and [[convex-analysis/biconjugate|biconjugation]]. When $f$ is smooth and strictly convex, the transform agrees with the classical [[convex-analysis/legendre-transform|Legendre transform]] on the range of $\nabla f$.

**Examples:**
- If $f(x)=|x|$ on $\mathbb{R}$, then $f^*(y)=0$ for $|y|\le 1$ and $f^*(y)=+\infty$ for $|y|>1$.
- If $f=\delta_C$ is the indicator of a set $C$, then $f^*(y)=\sup_{x\in C}\langle y,x\rangle$ (the support function of $C$).
