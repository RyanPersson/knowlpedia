---
title: "Convergence of the Virial Expansion"
description: "Sufficient conditions (via cluster/Mayer expansions) guaranteeing analyticity of the pressure and a convergent virial series at low density (or small activity) for a classical gas."
---

## Prerequisites

- {{< knowl id="pressure-log-partition-density" text="pressure / log-partition density" >}}
- {{< knowl id="cluster-integrals-mayer" text="cluster integrals (Mayer expansion)" >}}
- {{< knowl id="virial-coefficients" text="virial coefficients" >}}
- {{< knowl id="cluster-expansion-theorem" text="cluster expansion theorem" >}}
- {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}

## Setting and expansions

Consider a classical continuum gas in a bounded region $\Lambda\subset\mathbb{R}^d$ at inverse temperature $\beta>0$ with a translation-invariant pair potential $\phi(x)$.
The grand-canonical partition function is
$$
\Xi_\Lambda(z,\beta)
={}
\sum_{N=0}^\infty \frac{z^N}{N!}
\int_{\Lambda^N}
\exp\!\Big(
-\beta \sum_{1\le i<j\le N}\phi(x_i-x_j)
\Big)\,dx_1\cdots dx_N,
$$

where $z$ is the activity.

The finite-volume pressure (in units of $\beta$) is
$$
\beta p_\Lambda(z)=\frac{1}{|\Lambda|}\log \Xi_\Lambda(z,\beta),
$$
and the thermodynamic pressure is the limit defining {{< knowl id="pressure-log-partition-density" text="pressure/log-partition density" >}}.

Introduce the Mayer function
$$
f(x)=e^{-\beta \phi(x)}-1.
$$
Under suitable assumptions, one has an absolutely convergent cluster (Mayer) expansion
$$
\beta p(z)=\sum_{n\ge 1} b_n(\beta)\, z^n,
\qquad
\rho(z)= z\frac{d}{dz}\big(\beta p(z)\big)=\sum_{n\ge 1} n\,b_n(\beta)\,z^n,
$$

where $\rho(z)$ is the particle density.

The **virial expansion** is the equation of state as a power series in $\rho$:
$$
\beta p(\rho)=\rho+\sum_{n\ge 2} B_n(\beta)\,\rho^n,
$$

with coefficients $B_n$ (the {{< knowl id="virial-coefficients" text="virial coefficients" >}}) determined combinatorially from the cluster integrals $b_n$ (see {{< knowl id="cluster-integrals-mayer" text="cluster integrals" >}}).

## Theorem (Convergence of Mayer and virial expansions)

Assume the pair potential $\phi$ is:

1. **Stable**: there exists $B\ge 0$ such that for every $N$ and every configuration $(x_1,\dots,x_N)$,
   $$
   \sum_{1\le i<j\le N}\phi(x_i-x_j)\ge -B\,N.
   $$
2. **Tempered / integrable Mayer function**: the quantity
   $$
   C(\beta)=\int_{\mathbb{R}^d} \big|e^{-\beta\phi(x)}-1\big|\,dx
   $$
   is finite.

Then there exists $z_0(\beta)>0$ such that:

- The series $\sum_{n\ge1} b_n z^n$ and $\sum_{n\ge1} n b_n z^n$ converge absolutely for $|z|<z_0(\beta)$.
- The functions $p(z)$ and $\rho(z)$ are analytic on $|z|<z_0(\beta)$, with $\rho(0)=0$ and $\rho'(0)=1$.
- Consequently, there exists $\rho_0(\beta)>0$ such that $z\mapsto \rho(z)$ is invertible and analytic for $|\rho|<\rho_0(\beta)$, and the virial series
  $$
  \beta p(\rho)=\rho+\sum_{n\ge2} B_n(\beta)\rho^n
  $$

  converges absolutely for $|\rho|<\rho_0(\beta)$.

One explicit sufficient small-activity condition commonly used in practice is
$$
e^{2\beta B}\,|z|\,C(\beta) < \frac{1}{e},
$$

which guarantees convergence of the cluster expansion (hence analyticity of $p$ and $\rho$) and yields a nontrivial analyticity neighborhood for the virial expansion.

## Low-order relations between $b_n$ and $B_n$

With the normalization $b_1=1$ (so that $\rho(z)=z+O(z^2)$), the first virial coefficients can be expressed in terms of the cluster coefficients as
$$
B_2 = - b_2,
\qquad
B_3 = 4 b_2^2 - 2 b_3,
$$

and higher $B_n$ are polynomials in $b_2,\dots,b_n$.

## Consequences and interpretation

- **Analytic equation of state at low density**: convergence implies $p(\rho)$ is analytic for sufficiently small $\rho$; in particular, there is no thermodynamic singularity in that regime.
- **Uniform control via {{< knowl id="cluster-expansion-theorem" text="cluster expansion" >}}**: the same estimates typically imply exponential decay of correlations and uniqueness of the Gibbs state in the corresponding parameter region (high temperature / low density).
