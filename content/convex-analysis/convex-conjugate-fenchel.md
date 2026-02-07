---
title: "Fenchel conjugate"
description: "The convex conjugate of an extended-real-valued function, defined by a supremum of affine functionals."
---

A **Fenchel conjugate** of an extended-real-valued {{< knowl id="function" section="shared-foundations" text="function" >}} $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function $f^*:\mathbb{R}^n\to(-\infty,+\infty]$ defined by
$$
f^*(y) \;=\; \sup_{x\in\mathbb{R}^n}\big(\langle y,x\rangle - f(x)\big),
\qquad y\in\mathbb{R}^n,
$$

where $\langle y,x\rangle$ denotes the Euclidean pairing.

This operation (also called the {{< knowl id="legendre-fenchel-transform" text="Legendre–Fenchel transform" >}}) turns $f$ into a (possibly extended-real) {{< knowl id="convex-function-via-epigraph" text="convex function" >}}, and it is the basic object behind {{< knowl id="fenchel-young-inequality" text="Fenchel–Young inequality" >}} and {{< knowl id="convex-duality-primal-dual" text="convex duality" >}}. The definition uses the {{< knowl id="supremum" section="real-analysis" text="supremum" >}} over all affine functionals $x\mapsto \langle y,x\rangle - f(x)$.

**Examples:**
- If $f(x)=\tfrac12\|x\|_2^2$ on $\mathbb{R}^n$, then $f^*(y)=\tfrac12\|y\|_2^2$.
- If $f=\delta_C$ is the indicator of a nonempty set $C$ (i.e. $\delta_C(x)=0$ for $x\in C$ and $+\infty$ otherwise), then $f^*(y)=\sup_{x\in C}\langle y,x\rangle$, the support function of $C$.
