+++
id = "thermodynamics/third-law-thermodynamics"
title = "Third law of thermodynamics"
kind = "knowl"
summary = "As temperature approaches absolute zero, equilibrium entropy approaches a constant, fixing the absolute entropy scale and implying unattainability of ."
aliases = ["third-law-thermodynamics", "Third law of thermodynamics"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/third-law-thermodynamics.md"
+++

One common formulation (Nernst heat theorem) is:

- For any reversible isothermal change between equilibrium states, the entropy change tends to zero as the [[thermodynamics/temperature-thermo|temperature]] tends to absolute zero (on the [[thermodynamics/absolute-temperature-scale|absolute temperature scale]]).

A closely related and widely used consequence is that, for a system in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] with fixed composition and fixed internal constraints,
$$
\lim_{T\to 0^+} S(T, X) = S_0,
$$

where $S$ is the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] and $S_0$ is a constant independent of the *continuous* thermodynamic coordinates $X$ (such as volume or pressure). For a “perfect crystal” with a unique ground state, one often takes $S_0=0$, which is an [[thermodynamics/entropy-normalization-convention|entropy normalization convention]] compatible with the third law.

A complementary formulation is the **unattainability principle**: no finite sequence of [[thermodynamics/thermodynamic-process|thermodynamic processes]] can reach $T=0$.

## Physical interpretation

At very low temperatures, accessible microscopic configurations collapse toward the ground-state set, so there is (typically) no extensive configurational disorder left to contribute to entropy. When the ground state has a degeneracy $g$, the third-law limit allows a “residual entropy”
$$
S_0 = k_B \ln g,
$$
linking macroscopic entropy to microscopic state counting via the [[thermodynamics/boltzmann-constant|Boltzmann constant]].

## Key relations

- **Computing absolute entropies from heat capacities.** If the third law fixes $S_0$, then along a path at fixed volume,
  $$
  S(T) = S_0 + \int_{0}^{T} \frac{C_V(T')}{T'}\,dT' \;+\; \sum_{\text{transitions}} \Delta S,
  $$

  where $C_V$ is the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]] and the sum accounts for entropy jumps at phase transitions. An analogous formula uses the [[thermodynamics/heat-capacity-constant-pressure|heat capacity at constant pressure]] along a constant-pressure path.

- **Low-temperature constraint.** For equilibrium systems that obey the third law, $C_V$ and $C_P$ cannot remain finite and nonzero all the way to $T=0^+$ without making the integral of $C/T$ diverge; in many familiar systems they vanish as $T\to 0^+$, strongly constraining admissible [[thermodynamics/equation-of-state|equations of state]] near absolute zero.

- **Statistical-mechanical parameter.** In ensemble language, $T\to 0^+$ corresponds to the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta\to +\infty$, emphasizing that the third law concerns the extreme low-energy limit.
