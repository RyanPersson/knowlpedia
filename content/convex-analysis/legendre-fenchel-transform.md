---
title: "Legendre–Fenchel transform"
description: "The general convex-conjugation transform defined by a supremum pairing, without smoothness assumptions."
---

A **Legendre–Fenchel transform** of an extended-real-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function $f^*:\mathbb{R}^n\to(-\infty,+\infty]$ defined by
$$
f^*(y) \;=\; \sup_{x\in\mathbb{R}^n}\big(\langle y,x\rangle - f(x)\big).
$$

This is exactly the {{< knowl id="convex-conjugate-fenchel" text="Fenchel conjugate" >}}; the “Legendre” terminology is common even when $f$ is not differentiable, and it underlies {{< knowl id="fenchel-young-inequality" text="Fenchel–Young inequality" >}} and {{< knowl id="biconjugate" text="biconjugation" >}}. When $f$ is smooth and strictly convex, the transform agrees with the classical {{< knowl id="legendre-transform" text="Legendre transform" >}} on the range of $\nabla f$.

**Examples:**
- If $f(x)=|x|$ on $\mathbb{R}$, then $f^*(y)=0$ for $|y|\le 1$ and $f^*(y)=+\infty$ for $|y|>1$.
- If $f=\delta_C$ is the indicator of a set $C$, then $f^*(y)=\sup_{x\in C}\langle y,x\rangle$ (the support function of $C$).
