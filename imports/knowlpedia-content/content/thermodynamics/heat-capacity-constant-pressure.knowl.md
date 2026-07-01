+++
id = "thermodynamics/heat-capacity-constant-pressure"
title = "Heat capacity at constant pressure"
kind = "knowl"
summary = "A response function measuring how enthalpy changes with temperature when pressure (and composition) are held fixed."
aliases = ["heat-capacity-constant-pressure", "Heat capacity at constant pressure"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/heat-capacity-constant-pressure.md"
+++

For a simple [[thermodynamics/thermodynamic-system|thermodynamic system]] in [[thermodynamics/thermodynamic-equilibrium|equilibrium]], the **heat capacity at constant pressure** is a [[thermodynamics/response-function-thermo|response function]]
that quantifies how much the system’s energy-like content must change to raise the [[thermodynamics/temperature-thermo|temperature]] while keeping the [[thermodynamics/pressure-thermo|pressure]] fixed (and keeping composition fixed, e.g. fixed [[thermodynamics/particle-number|particle number]] $N$).

It is defined by the partial derivative
$$
C_P \equiv \left(\frac{\partial H}{\partial T}\right)_{p,N},
$$

where $H$ is the [[thermodynamics/enthalpy|enthalpy]],
$$
H \equiv U + pV,
$$

with $U$ the [[thermodynamics/internal-energy-thermo|internal energy]] and $V$ the [[thermodynamics/volume-thermo|volume]].

Using the standard differential for $H$ for a simple compressible system, at fixed $p$ and $N$ one has $dH = T\,dS$, so an equivalent form is
$$
C_P
= T\left(\frac{\partial S}{\partial T}\right)_{p,N},
$$
in terms of the [[thermodynamics/thermodynamic-entropy|entropy]].

## Physical interpretation
Along a [[thermodynamics/quasistatic-process|quasistatic]], [[thermodynamics/reversible-process|reversible]] process at fixed pressure,
$$
\delta Q_{\rm rev} = C_P\,dT.
$$

Compared with heating at fixed volume (see [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]]), maintaining constant pressure generally allows the system to expand as it warms. Part of the supplied heat is then “spent” on the $p\,dV$ expansion, which is why $C_P$ is typically larger than $C_V$ in stable single-phase regions.

## Key relations and properties
- **Extensivity:** $C_P$ is typically [[thermodynamics/extensive-variable|extensive]]; one often uses a [[thermodynamics/specific-quantity|specific]] form such as $c_P = C_P/N$ (or per unit mass).

- **Gibbs free-energy curvature:** In terms of the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,p,N)$, one has
  $$
  C_P = -\,T\left(\frac{\partial^2 G}{\partial T^2}\right)_{p,N}.
  $$

- **Difference from $C_V$:** For a simple compressible system,
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  involving the [[thermodynamics/thermal-expansion-coefficient|thermal expansion coefficient]] $\alpha$ and the [[thermodynamics/isothermal-compressibility|isothermal compressibility]] $\kappa_T$.

- **Inequality (typical):** In stable single-phase regions with $\kappa_T>0$, one usually has $C_P \ge C_V$, consistent with [[thermodynamics/thermodynamic-stability|stability]].

- **Fluctuation formula (statistical mechanics):** In the isothermal–isobaric description (fixed $T$, $p$, $N$), $C_P$ is proportional to the [[probability/variance|variance]] of the enthalpy as a random variable:
  $$
  C_P = \frac{1}{k_B T^2}\left(\langle H^2\rangle - \langle H\rangle^2\right),
  $$

  where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]] and $\langle\cdot\rangle$ is an ensemble [[probability/expectation|expectation]].
