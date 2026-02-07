---
title: "Thermodynamic entropy"
description: "A state function S defined so that dS = δQ_rev/T for reversible processes; it quantifies irreversibility and constrains spontaneous change."
---

*Thermodynamic entropy* $S$ is a {{< knowl id="state-function" text="state function" >}} defined on equilibrium {{< knowl id="thermodynamic-state" text="states" >}}. It is introduced by the Clausius definition: for any {{< knowl id="reversible-process" text="reversible process" >}},
$$
dS = \frac{\delta Q_{\mathrm{rev}}}{T},
$$

where $\delta Q_{\mathrm{rev}}$ is the {{< knowl id="heat-inexact-differential" text="heat increment" >}} along the reversible path and $T$ is {{< knowl id="temperature-thermo" text="thermodynamic temperature" >}}.

A key fact (often called the Clausius theorem) is that for reversible cycles,
$$
\oint \frac{\delta Q_{\mathrm{rev}}}{T} = 0,
$$

so the integral between two equilibrium states is path-independent when taken over reversible paths. This path-independence is what makes $S$ a state function even though $\delta Q$ itself is an inexact differential.

## Physical interpretation
Entropy measures the *directionality* of macroscopic change: it increases when constraints are relaxed and when processes are irreversible. In many contexts, it is useful to think of entropy as quantifying “energy dispersal” among microscopic degrees of freedom, and of *entropy production* as a measure of irreversibility.

## Key properties and relations
- **Second law and isolated systems:** for an {{< knowl id="isolated-system" text="isolated system" >}} (no heat or work exchange), the {{< knowl id="second-law-thermodynamics" text="second law" >}} implies
  $$
  \Delta S \ge 0,
  $$
  with equality for an idealized reversible evolution.

- **Clausius inequality:** for any cycle (not necessarily reversible),
  $$
  \oint \frac{\delta Q}{T} \le 0,
  $$
  with equality iff the cycle is reversible. This is the content of the {{< knowl id="clausius-inequality" text="Clausius inequality" >}} in a compact form.

- **Entropy and temperature (definition of T):** if equilibrium states are described by a {{< knowl id="fundamental-relation-entropy" text="fundamental relation in the entropy representation" >}} $S(U,V,N)$, then temperature is defined by
  $$
  \frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V,N},
  $$
  using the notion of {{< knowl id="partial-derivative" section="real-analysis" text="partial derivative" >}}. The reciprocal temperature is often written as {{< knowl id="inverse-temperature-beta" text="β (inverse temperature)" >}} after introducing {{< knowl id="boltzmann-constant" text="Boltzmann’s constant" >}}.

- **Additivity and extensivity:** for weakly interacting subsystems, entropy is additive, aligning with the {{< knowl id="additivity-postulate" text="additivity postulate" >}}. In the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}}, entropy typically scales with system size, making it an {{< knowl id="extensive-variable" text="extensive variable" >}} (see the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}}).

- **Stability (concavity):** for stable equilibrium, $S(U,V,N)$ is concave in its extensive arguments; this is one formulation of {{< knowl id="entropy-concavity-stability" text="entropy concavity and stability" >}} and is part of {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}.

- **Statistical-mechanical connection:** in equilibrium statistical mechanics, entropy can be related to microstate multiplicity (e.g., $S = k_B \ln \Omega$ in the microcanonical setting) and, more generally, to the information-theoretic {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}} of a probability distribution over microstates, with $k_B$ setting the physical units.

- **Third law (reference point):** the {{< knowl id="third-law-thermodynamics" text="third law" >}} constrains the behavior of $S$ as $T\to 0$ (often implying $S$ approaches a constant), fixing the otherwise arbitrary additive constant in practical conventions (see {{< knowl id="entropy-normalization-convention" text="entropy normalization conventions" >}}).
