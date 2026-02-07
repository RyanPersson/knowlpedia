---
title: "Curvature of a vector bundle connection"
description: "The obstruction to commuting covariant derivatives, yielding an endomorphism-valued 2-form."
---

Let $E\to M$ be a vector bundle with a {{< knowl id="connection-on-a-vector-bundle" text="connection on a vector bundle" >}} $\nabla$. Let $X,Y$ be smooth vector fields on $M$, and let $s$ be a smooth section of $E$.

**Definition.** The curvature of $\nabla$ is the map $R^\nabla$ defined by
\[
R^\nabla(X,Y)s \;:=\; \nabla_X\nabla_Y s \;-\; \nabla_Y\nabla_X s \;-\; \nabla_{[X,Y]} s,
\]
where $[X,Y]$ is the {{< knowl id="lie-bracket" text="Lie bracket" >}} of vector fields.

For each $X,Y$, the operator $R^\nabla(X,Y):\Gamma(E)\to\Gamma(E)$ is $C^\infty(M)$-linear in $s$, hence defines a bundle endomorphism of $E$. Moreover, $R^\nabla$ is $C^\infty(M)$-linear in $X$ and $Y$ and skew-symmetric, so it can be viewed as an $\mathrm{End}(E)$-valued {{< knowl id="differential-k-form" text="differential 2-form" >}} on $M$. In a local frame, it is represented by the {{< knowl id="curvature-2-form-in-a-frame" text="curvature 2-form" >}} matrix.

## Examples
1. **Trivial connection is flat.** For the trivial connection on $M\times\mathbb R^r$, mixed derivatives commute and $R^\nabla=0$.
2. **Levi-Civita curvature.** For the Levi-Civita connection on $TM$, $R^\nabla$ is the Riemann curvature tensor (in $(1,3)$ form), encoding sectional curvature and holonomy phenomena.
3. **Constant matrix connection on a trivial bundle.** On $U\subset\mathbb R^n$, take $\nabla = d + \sum_k A_k\,dx^k$ with constant matrices $A_k$. Then $R^\nabla$ corresponds to the commutators $[A_k,A_\ell]$; it vanishes exactly when the matrices $A_k$ pairwise commute.
