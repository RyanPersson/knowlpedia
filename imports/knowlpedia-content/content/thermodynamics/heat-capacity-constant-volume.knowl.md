+++
id = "thermodynamics/heat-capacity-constant-volume"
title = "Heat capacity at constant volume"
kind = "knowl"
summary = "A response function measuring how internal energy changes with temperature when volume (and composition) are held fixed."
aliases = ["heat-capacity-constant-volume", "Heat capacity at constant volume"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/heat-capacity-constant-volume.md"
+++

For a closed, simple [[thermodynamics/thermodynamic-system|thermodynamic system]] in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]], the **heat capacity at constant volume** is the [[thermodynamics/response-function-thermo|response function]]
that quantifies how the [[thermodynamics/internal-energy-thermo|internal energy]] changes with the [[thermodynamics/temperature-thermo|temperature]] when the [[thermodynamics/volume-thermo|volume]] is fixed (and the composition is fixed, e.g. fixed [[thermodynamics/particle-number|particle number]] $N$ for a single-component system).

The heat capacity at constant volume is
$$
C_V \equiv \left(\frac{\partial U}{\partial T}\right)_{V,N}.
$$

Because $U$ and $T$ are [[thermodynamics/state-function|state functions]] (for equilibrium states), $C_V$ is a property of the equilibrium [[thermodynamics/thermodynamic-state|state]].

A useful equivalent form follows from the [[thermodynamics/fundamental-relation-energy|fundamental energy differential]] for a simple compressible system,
which implies that at fixed $V$ and $N$ one has $dU = T\,dS$. Hence
$$
C_V
= T\left(\frac{\partial S}{\partial T}\right)_{V,N},
$$

where $S$ is the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]].

## Physical interpretation
Along a [[thermodynamics/quasistatic-process|quasistatic]], [[thermodynamics/reversible-process|reversible]] process in which $V$ and $N$ are held fixed, the heat increment satisfies
$$
\delta Q_{\rm rev} = C_V\,dT.
$$

This is why $C_V$ is often described as “the heat required per unit temperature rise at constant volume”: the container is effectively rigid, so there is no $p\,dV$ expansion and the energy input shows up entirely as a change in internal energy.

## Key relations and properties
- **Extensivity:** $C_V$ is typically an [[thermodynamics/extensive-variable|extensive]] quantity. One often uses a [[thermodynamics/specific-quantity|specific]] or per-particle form such as $c_V = C_V/N$ (or per unit mass).

- **Free-energy curvature:** In terms of the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)$, one has
  $$
  C_V = -\,T\left(\frac{\partial^2 F}{\partial T^2}\right)_{V,N}.
  $$

- **Stability (typical sign):** For stable single-phase equilibrium states, one expects $C_V \ge 0$; this is tied to [[thermodynamics/thermodynamic-stability|thermodynamic stability]] and can be viewed as a consequence of [[thermodynamics/entropy-concavity-stability|entropy concavity]] (or equivalently [[thermodynamics/energy-convexity-stability|energy convexity]] in appropriate variables).

- **Difference from constant-pressure heat capacity:** The difference between $C_V$ and the [[thermodynamics/heat-capacity-constant-pressure|constant-pressure heat capacity]] is
  $$
  C_P - C_V = \frac{T\,V\,\alpha^2}{\kappa_T},
  $$

  where $\alpha$ is the [[thermodynamics/thermal-expansion-coefficient|thermal expansion coefficient]] and $\kappa_T$ is the [[thermodynamics/isothermal-compressibility|isothermal compressibility]].

- **Fluctuation formula (statistical mechanics):** In the canonical description at fixed $T$, $V$, and $N$, $C_V$ can be written in terms of the [[probability/variance|variance]] of the energy as a random variable:
  $$
  C_V = \frac{1}{k_B T^2}\left(\langle E^2\rangle - \langle E\rangle^2\right),
  $$

  where $k_B$ is the [[thermodynamics/boltzmann-constant|Boltzmann constant]] and $\langle\cdot\rangle$ denotes the ensemble [[probability/expectation|expectation]].
