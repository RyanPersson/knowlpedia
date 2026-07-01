+++
id = "thermodynamics/intensive-variable"
title = "Intensive variable"
kind = "knowl"
summary = "A thermodynamic variable that does not scale with system size and typically equalizes between subsystems at equilibrium."
aliases = ["intensive-variable", "Intensive variable"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/intensive-variable.md"
+++

## Definition and physical interpretation

An **intensive variable** is a [[thermodynamics/state-variable|state variable]] whose value does **not** scale with the overall size of the [[thermodynamics/thermodynamic-system|system]]. Concretely, under a uniform rescaling of extensive quantities (e.g. doubling the amount of material so that $S$, $V$, and $N$ all double), intensive variables remain unchanged in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].

This contrasts with an [[thermodynamics/extensive-variable|extensive variable]], which scales linearly with system size (entropy $S$, volume $V$, particle number $N$, internal energy $U$, and so on).

Intensive variables act like “generalized forces” that drive exchanges between weakly interacting subsystems. At equilibrium they equalize:
- [[thermodynamics/thermal-equilibrium|thermal equilibrium]] enforces equality of [[thermodynamics/temperature-thermo|temperature]] $T$.
- [[thermodynamics/mechanical-equilibrium|mechanical equilibrium]] enforces equality of [[thermodynamics/pressure-thermo|pressure]] $p$.
- [[thermodynamics/chemical-equilibrium|chemical equilibrium]] enforces equality of [[thermodynamics/chemical-potential-thermo|chemical potential]] $\mu$.

## Conjugate derivatives from the fundamental relation

If a single-component simple compressible system admits a [[thermodynamics/fundamental-relation-energy|fundamental relation]] $U(S,V,N)$, the standard intensive variables arise as partial derivatives:
$$
T = \left(\frac{\partial U}{\partial S}\right)_{V,N},
\qquad
p = -\left(\frac{\partial U}{\partial V}\right)_{S,N},
\qquad
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

These relations explain why intensive variables appear as natural control parameters in thermodynamic potentials such as the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] (natural in $T$), the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] (natural in $T$ and $p$), the [[thermodynamics/enthalpy|enthalpy]] (natural in $p$), and the [[thermodynamics/grand-potential|grand potential]] (natural in $T$ and $\mu$).

## Homogeneity, Euler, and Gibbs–Duhem

When the system satisfies extensivity so that $U(S,V,N)$ is a [[thermodynamics/homogeneous-function-degree-one|homogeneous function of degree one]], the [[thermodynamics/euler-relation-thermodynamics|Euler relation]] takes the form
$$
U = TS - pV + \mu N,
$$

showing $U$ as a sum of intensive–extensive products.

A key consequence is that the intensive variables are not all independent: their allowed variations are constrained by the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]] (single component),
$$
S\,dT - V\,dp + N\,d\mu = 0,
$$
which encodes that changing one intensive variable generally forces changes in the others when the composition is fixed.
