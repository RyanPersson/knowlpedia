+++
id = "stat-mech/green-kubo-relations"
title = "Green–Kubo relations"
kind = "knowl"
summary = "Transport coefficients expressed as time integrals of equilibrium current autocorrelation functions (linear response)."
aliases = ["green-kubo-relations", "Green–Kubo relations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/green-kubo-relations.md"
+++

## Statement (generic form)

In equilibrium (typically with respect to a [[stat-mech/canonical-ensemble|canonical ensemble]]), many linear transport coefficients can be written as time integrals of equilibrium time-correlation functions (a special case of [[stat-mech/kubo-formula|Kubo linear response]]).

A common template is
$$
\mathcal{L}_{\alpha\beta}
= \int_0^\infty \langle J_\alpha(0)\,J_\beta(t)\rangle_{\mathrm{eq}}\,dt,
$$

up to conventional prefactors (often $1/(k_B T)$ and/or volume factors) depending on the definition of the currents and forces.

Here $\langle \cdot \rangle_{\mathrm{eq}}$ is an [[stat-mech/ensemble-average|ensemble average]] in equilibrium, and $\langle J_\alpha(0)J_\beta(t)\rangle$ is a [[stat-mech/correlation-function-two-point|two-point time correlation]].

## Standard examples (common conventions)

### Electrical conductivity
Let $J(t)$ be the total electric current in volume $V$. Then
$$
\sigma
= \frac{1}{k_B T\,V}\int_0^\infty \langle J(0)\cdot J(t)\rangle_{\mathrm{eq}}\,dt.
$$

### Shear viscosity
Let $P_{xy}(t)$ be the off-diagonal stress tensor component. Then
$$
\eta
= \frac{1}{k_B T\,V}\int_0^\infty \langle P_{xy}(0)\,P_{xy}(t)\rangle_{\mathrm{eq}}\,dt.
$$

### Diffusion constant (Einstein–Green–Kubo form)
For a tagged particle velocity $v(t)$ in $d$ dimensions,
$$
D
= \frac{1}{d}\int_0^\infty \langle v(0)\cdot v(t)\rangle_{\mathrm{eq}}\,dt.
$$

## Conditions (what is implicitly required)

- **Stationarity:** the equilibrium measure is invariant under the dynamics (e.g., Gibbs equilibrium).
- **Decay of correlations / mixing:** ensures the integral over $t\in[0,\infty)$ converges.
- **Microreversibility:** under time-reversal symmetry (or, in stochastic settings, [[stat-mech/detailed-balance|detailed balance]]), one obtains symmetry properties such as Onsager reciprocity.

## Relationship to other linear-response statements

- Green–Kubo is a concrete evaluation of linear-response coefficients and is closely tied to the [[stat-mech/fluctuation-dissipation-theorem|fluctuation–dissipation theorem]].
- In quantum systems, the equilibrium state is often a [[stat-mech-quantum/gibbs-state-quantum|Gibbs state]] and correlation/response relations are governed by the [[stat-mech-quantum/kms-condition-finite|KMS condition]].
