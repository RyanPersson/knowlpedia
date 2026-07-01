+++
id = "stat-mech/exact-differential-criterion"
title = "Criterion for an exact differential"
kind = "knowl"
summary = "Mixed-partial equality criterion for when a differential form is the differential of a state function; used to justify Maxwell relations and identify thermodynamic potentials."
aliases = ["exact-differential-criterion", "Criterion for an exact differential"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/exact-differential-criterion.md"
+++

## Statement
Let $D\subset\mathbb R^2$ be an open, simply connected domain and let $M,N\in C^1(D)$. Consider the $1$-form
$$
\omega = M(x,y)\,dx + N(x,y)\,dy.
$$
Then the following are equivalent:
1. $\omega$ is **exact**: there exists a scalar potential $F\in C^2(D)$ such that $dF=\omega$ (i.e. $\partial_x F=M$ and $\partial_y F=N$).
2. The mixed partials satisfy
   $$
   \frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}\qquad\text{everywhere on }D.
   $$

Equivalently, line integrals of $\omega$ are path-independent on $D$.

### Multivariable version (thermodynamic coordinates)
For $\omega=\sum_{i=1}^n M_i(x)\,dx_i$ with $M_i\in C^1(D)\subset\mathbb R^n$ on a simply connected domain, $\omega$ is exact iff
$$
\frac{\partial M_i}{\partial x_j}=\frac{\partial M_j}{\partial x_i}\qquad\text{for all }i,j.
$$

## Key hypotheses
- Coefficients $M,N$ are continuously differentiable (at least $C^1$).
- The domain $D$ is simply connected (no “holes”), ensuring that closedness implies exactness in this setting.

## Key conclusions
- A differential expression is the differential of a single-valued state function precisely when the corresponding cross-derivative compatibility holds.
- In thermodynamics, this criterion underlies:
  - identification of state functions like [[thermodynamics/internal-energy-thermo|internal energy]] and [[thermodynamics/thermodynamic-entropy|entropy]];
  - derivations of [[thermodynamics/maxwell-relation|Maxwell relations]] (see [[thermodynamics/maxwell-relations-theorem|Maxwell relations theorem]] and [[stat-mech/prop-maxwell-from-mixed-partials|Maxwell from mixed partials]]).
