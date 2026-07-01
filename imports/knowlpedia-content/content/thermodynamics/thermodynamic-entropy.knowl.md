+++
id = "thermodynamics/thermodynamic-entropy"
title = "Thermodynamic entropy"
kind = "knowl"
summary = "A state function S defined so that dS = δQ_rev/T for reversible processes; it quantifies irreversibility and constrains spontaneous change."
aliases = ["thermodynamic-entropy", "Thermodynamic entropy"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-entropy.md"
+++

*Thermodynamic entropy* $S$ is a [[thermodynamics/state-function|state function]] defined on equilibrium [[thermodynamics/thermodynamic-state|states]]. It is introduced by the Clausius definition: for any [[thermodynamics/reversible-process|reversible process]],
$$
dS = \frac{\delta Q_{\mathrm{rev}}}{T},
$$

where $\delta Q_{\mathrm{rev}}$ is the [[thermodynamics/heat-inexact-differential|heat increment]] along the reversible path and $T$ is [[thermodynamics/temperature-thermo|thermodynamic temperature]].

A key fact (often called the Clausius theorem) is that for reversible cycles,
$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T} = 0,
$$

so the integral between two equilibrium states is path-independent when taken over reversible paths. This path-independence is what makes $S$ a state function even though $\delta Q$ itself is an inexact differential.

## Physical interpretation
Entropy measures the *directionality* of macroscopic change: it increases when constraints are relaxed and when processes are irreversible. In many contexts, it is useful to think of entropy as quantifying “energy dispersal” among microscopic degrees of freedom, and of *entropy production* as a measure of irreversibility.

## Key properties and relations
- **Second law and isolated systems:** for an [[thermodynamics/isolated-system|isolated system]] (no heat or work exchange), the [[thermodynamics/second-law-thermodynamics|second law]] implies
  $$
  \Delta S \ge 0,
  $$
  with equality for an idealized reversible evolution.

- **Clausius inequality:** for any cycle (not necessarily reversible),
  $$
  \oint \frac{\delta Q}{T} \le 0,
  $$
  with equality iff the cycle is reversible. This is the content of the [[thermodynamics/clausius-inequality|Clausius inequality]] in a compact form.

- **Entropy and temperature (definition of T):** if equilibrium states are described by a [[thermodynamics/fundamental-relation-entropy|fundamental relation in the entropy representation]] $S(U,V,N)$, then temperature is defined by
  $$
  \frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N},
  $$
  using the notion of [[real-analysis/partial-derivative|partial derivative]]. The reciprocal temperature is often written as [[thermodynamics/inverse-temperature-beta|β (inverse temperature)]] after introducing [[thermodynamics/boltzmann-constant|Boltzmann’s constant]].

- **Additivity and extensivity:** for weakly interacting subsystems, entropy is additive, aligning with the [[thermodynamics/additivity-postulate|additivity postulate]]. In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], entropy typically scales with system size, making it an [[thermodynamics/extensive-variable|extensive variable]] (see the [[thermodynamics/extensivity-postulate|extensivity postulate]]).

- **Stability (concavity):** for stable equilibrium, $S(U,V,N)$ is concave in its extensive arguments; this is one formulation of [[thermodynamics/entropy-concavity-stability|entropy concavity and stability]] and is part of [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

- **Statistical-mechanical connection:** in equilibrium statistical mechanics, entropy can be related to microstate multiplicity (e.g., $S = k_B \ln \Omega$ in the microcanonical setting) and, more generally, to the information-theoretic [[probability/shannon-entropy|Shannon entropy]] of a probability distribution over microstates, with $k_B$ setting the physical units.

- **Third law (reference point):** the [[thermodynamics/third-law-thermodynamics|third law]] constrains the behavior of $S$ as $T\to 0$ (often implying $S$ approaches a constant), fixing the otherwise arbitrary additive constant in practical conventions (see [[thermodynamics/entropy-normalization-convention|entropy normalization conventions]]).
