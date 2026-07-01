+++
id = "convex-analysis/convex-conjugate-fenchel"
title = "Fenchel conjugate"
kind = "knowl"
summary = "The convex conjugate of an extended-real-valued function, defined by a supremum of affine functionals."
aliases = ["convex-conjugate-fenchel", "Fenchel conjugate"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/convex-conjugate-fenchel.md"
+++

A **Fenchel conjugate** of an extended-real-valued [[shared-foundations/function|function]] $f:\mathbb{R}^n\to(-\infty,+\infty]$ is the function $f^*:\mathbb{R}^n\to(-\infty,+\infty]$ defined by
$$
f^*(y) \;=\; \sup_{x\in\mathbb{R}^n}\big(\langle y,x\rangle - f(x)\big),
\qquad y\in\mathbb{R}^n,
$$

where $\langle y,x\rangle$ denotes the Euclidean pairing.

This operation (also called the [[convex-analysis/legendre-fenchel-transform|Legendre–Fenchel transform]]) turns $f$ into a (possibly extended-real) [[convex-analysis/convex-function-via-epigraph|convex function]], and it is the basic object behind [[convex-analysis/fenchel-young-inequality|Fenchel–Young inequality]] and [[convex-analysis/convex-duality-primal-dual|convex duality]]. The definition uses the [[real-analysis/supremum|supremum]] over all affine functionals $x\mapsto \langle y,x\rangle - f(x)$.

**Examples:**
- If $f(x)=\tfrac12\|x\|_2^2$ on $\mathbb{R}^n$, then $f^*(y)=\tfrac12\|y\|_2^2$.
- If $f=\delta_C$ is the indicator of a nonempty set $C$ (i.e. $\delta_C(x)=0$ for $x\in C$ and $+\infty$ otherwise), then $f^*(y)=\sup_{x\in C}\langle y,x\rangle$, the support function of $C$.
