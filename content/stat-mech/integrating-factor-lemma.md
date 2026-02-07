---
title: "Integrating factor lemma"
description: "Sufficient conditions for a non-exact 1-form M dx + N dy to become exact after multiplication by a scalar integrating factor; used for entropy/temperature as an integrating factor for heat."
---

## Statement
Let $D\subset\mathbb R^2$ be an open domain and let $M,N\in C^1(D)$. Consider the $1$-form
$$
\omega = M(x,y)\,dx + N(x,y)\,dy.
$$

A nonvanishing function $\mu$ on $D$ is an **integrating factor** for $\omega$ if the rescaled form $\mu\,\omega$ is exact (equivalently, $\mu\,\omega=dF$ for some potential $F$).

### A common sufficient criterion (two-variable, one-function dependence)
Assume $N\neq 0$ on $D$ and define
$$
\Phi(x,y)=\frac{1}{N(x,y)}\left(\frac{\partial M}{\partial y}-\frac{\partial N}{\partial x}\right).
$$

If $\Phi(x,y)$ depends only on $x$, i.e. $\Phi(x,y)=f(x)$, then
$$
\mu(x)=\exp\!\left(\int^x f(s)\,ds\right)
$$

is an integrating factor on $D$.

Similarly, if $M\neq 0$ on $D$ and
$$
\Psi(x,y)=\frac{1}{M(x,y)}\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right)
$$

depends only on $y$, i.e. $\Psi(x,y)=g(y)$, then
$$
\mu(y)=\exp\!\left(\int^y g(t)\,dt\right)
$$
is an integrating factor.

## Key hypotheses
- $M,N$ are $C^1$ on $D$.
- $\mu$ is nonzero on $D$ (so multiplication does not change the set of admissible directions).
- For the explicit formulas above, the indicated dependence restriction holds (e.g. $\Phi(x,y)=f(x)$).

## Key conclusions
- Under the criterion, $\mu\,\omega$ satisfies the {{< knowl id="exact-differential-criterion" text="exact differential criterion" >}}, hence $\mu\,\omega=dF$ for some state function $F$.
- The integrating factor is determined (up to an overall multiplicative constant) by a one-dimensional integral.

