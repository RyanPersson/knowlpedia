+++
id = "stat-mech/corollary-maxwell-standard-identities"
title = "Standard derivative identities from Maxwell relations"
kind = "knowl"
summary = "Differentials of thermodynamic potentials express , , as partial derivatives and yield the usual Maxwell relations."
aliases = ["corollary-maxwell-standard-identities", "Standard derivative identities from Maxwell relations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-maxwell-standard-identities.md"
+++

Let
- $U$ be [[thermodynamics/internal-energy-thermo|internal energy]],
- $F$ be [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]],
- $G$ be [[thermodynamics/gibbs-free-energy|Gibbs free energy]],
- $\Omega$ be the [[thermodynamics/grand-potential|grand potential]].

Let $S$, $T$, $P$, and $\mu$ denote [[thermodynamics/thermodynamic-entropy|entropy]], [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], and [[thermodynamics/chemical-potential-thermo|chemical potential]], respectively.

Assume equilibrium and sufficient smoothness so that mixed partial derivatives commute, as in [[thermodynamics/maxwell-relations-theorem|Maxwell's relations theorem]].

## Statement
For a simple compressible system with particle number $N$, the potentials in their natural variables satisfy
$$
dU = T\,dS - P\,dV + \mu\, dN,
$$
$$
dF = -S\,dT - P\,dV + \mu\, dN,
$$
$$
dG = -S\,dT + V\,dP + \mu\, dN,
$$
$$
d\Omega = -S\,dT - P\,dV - N\,d\mu.
$$

Therefore the conjugate variables are recovered by partial differentiation, for example:
- from $F(T,V,N)$,
  $$
  S = -\left(\frac{\partial F}{\partial T}\right)_{V,N},\qquad
  P = -\left(\frac{\partial F}{\partial V}\right)_{T,N},\qquad
  \mu = \left(\frac{\partial F}{\partial N}\right)_{T,V};
  $$

- from $G(T,P,N)$,
  $$
  S = -\left(\frac{\partial G}{\partial T}\right)_{P,N},\qquad
  V = \left(\frac{\partial G}{\partial P}\right)_{T,N},\qquad
  \mu = \left(\frac{\partial G}{\partial N}\right)_{T,P};
  $$

- from $\Omega(T,V,\mu)$,
  $$
  S = -\left(\frac{\partial \Omega}{\partial T}\right)_{V,\mu},\qquad
  P = -\left(\frac{\partial \Omega}{\partial V}\right)_{T,\mu},\qquad
  N = -\left(\frac{\partial \Omega}{\partial \mu}\right)_{T,V}.
  $$

Commuting mixed partials yields the standard Maxwell relations, e.g. from $F(T,V,N)$,
$$
\left(\frac{\partial S}{\partial V}\right)_{T,N}
={}
\left(\frac{\partial P}{\partial T}\right)_{V,N},
\qquad
\left(\frac{\partial S}{\partial N}\right)_{T,V}
={}
-\left(\frac{\partial \mu}{\partial T}\right)_{V,N},
\qquad
\left(\frac{\partial P}{\partial N}\right)_{T,V}
={}
-\left(\frac{\partial \mu}{\partial V}\right)_{T,N}.
$$

## Key hypotheses
- The equilibrium [[thermodynamics/thermodynamic-state|state]] admits differentiable thermodynamic potentials.
- Each potential is expressed in its natural independent variables (obtained via a [[convex-analysis/legendre-transform|Legendre transform]] from $U$).
- The relevant second derivatives exist and mixed partial derivatives commute.

## Key conclusions
- $S$, $P$, $V$, $N$, and $\mu$ are partial derivatives of a single potential in natural variables.
- Maxwell relations provide measurable identities between derivatives (often turning difficult entropy derivatives into accessible pressure/volume derivatives).

## significance
Differentiate the fundamental identity for $U(S,V,N)$ and apply the defining Legendre transforms to obtain $F$, $G$, and $\Omega$. The displayed differential forms follow by direct differentiation. Maxwell relations then come from commuting mixed partial derivatives (see [[stat-mech/prop-maxwell-from-mixed-partials|Maxwell relations from mixed partials]]). These identities are the primary computational bridge between different experimentally accessible response functions.
