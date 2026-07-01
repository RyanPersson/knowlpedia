+++
id = "stat-mech/prop-maxwell-from-mixed-partials"
title = "Maxwell relations from equality of mixed partial derivatives"
kind = "knowl"
summary = "For twice differentiable thermodynamic potentials, symmetry of mixed second derivatives yields Maxwell relations among conjugate variables."
aliases = ["prop-maxwell-from-mixed-partials", "Maxwell relations from equality of mixed partial derivatives"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/prop-maxwell-from-mixed-partials.md"
+++

## Statement

Let $\Phi(x_1,\dots,x_n)$ be a thermodynamic potential expressed in its natural variables (e.g. $\Phi=F(T,V,N)$, $G(T,P,N)$, or $\Omega(T,V,\mu)$). Assume $\Phi$ is $C^2$ (twice continuously differentiable) in those variables.

If the differential has the form
$$
d\Phi = \sum_{i=1}^n a_i(x)\,dx_i,
$$

then each coefficient is a partial derivative $a_i = \left(\frac{\partial \Phi}{\partial x_i}\right)_{x_{j\neq i}}$, and symmetry of the Hessian implies the identities
$$
\left(\frac{\partial a_i}{\partial x_j}\right)_{x_{k\neq i,j}}
={}
\left(\frac{\partial a_j}{\partial x_i}\right)_{x_{k\neq i,j}}
\quad\text{for all } i\neq j.
$$

These are Maxwell relations (see [[thermodynamics/maxwell-relation|Maxwell relations]]) once the $a_i$ are identified with conjugate variables via the standard thermodynamic definitions.

### Canonical examples

- For the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)$,
  $$
  dF = -S\,dT - P\,dV + \mu\,dN,
  $$

  so $S= -(\partial F/\partial T)_{V,N}$ and $P= -(\partial F/\partial V)_{T,N}$, hence
  $$
  \left(\frac{\partial S}{\partial V}\right)_{T,N}
  ={}
  \left(\frac{\partial P}{\partial T}\right)_{V,N}.
  $$

- For the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,P,N)$,
  $$
  dG = -S\,dT + V\,dP + \mu\,dN,
  $$
  giving
  $$
  \left(\frac{\partial S}{\partial P}\right)_{T,N}
  ={}
  -\left(\frac{\partial V}{\partial T}\right)_{P,N}.
  $$

- For the [[thermodynamics/grand-potential|grand potential]] $\Omega(T,V,\mu)$,
  $$
  d\Omega = -S\,dT - P\,dV - N\,d\mu,
  $$
  giving, for instance,
  $$
  \left(\frac{\partial S}{\partial V}\right)_{T,\mu}
  ={}
  \left(\frac{\partial P}{\partial T}\right)_{V,\mu}.
  $$

## Key hypotheses

- The system is described by a state function $\Phi$ in equilibrium (see [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]]).
- $\Phi$ is $C^2$ in its natural variables, so mixed partial derivatives commute.
- Conjugate variables are defined by partial derivatives of the potential (e.g. [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]]).

## Key conclusions

- Each Maxwell relation is an instance of $\partial^2\Phi/\partial x_i\partial x_j = \partial^2\Phi/\partial x_j\partial x_i$ after substituting the derivative definitions of the conjugate variables.
- Practically, these relations convert difficult-to-measure derivatives (e.g. derivatives of entropy) into derivatives of more accessible quantities (e.g. pressure–temperature slopes).

## Cross-links to definitions

- [[thermodynamics/maxwell-relation|Maxwell relation]]
- [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], [[thermodynamics/gibbs-free-energy|Gibbs free energy]], [[thermodynamics/grand-potential|grand potential]]
- [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], [[thermodynamics/chemical-potential-thermo|chemical potential]]
- [[stat-mech/exact-differential-criterion|exact differential criterion]]
