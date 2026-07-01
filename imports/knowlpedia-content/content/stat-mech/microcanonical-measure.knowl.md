+++
id = "stat-mech/microcanonical-measure"
title = "Microcanonical measure"
kind = "knowl"
summary = "Uniform probability measure on the microcanonical energy shell, expressing equal a priori probability for accessible microstates."
aliases = ["microcanonical-measure", "Microcanonical measure"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/microcanonical-measure.md"
+++

Fix a classical [[stat-mech/phase-space-classical|phase space]] $\Gamma$ with Liouville [[stat-mech/phase-space-volume-element|volume element]] $d\Gamma$, and a [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H(x)$. For energy $E$ and window $\Delta E>0$, let $\Sigma_{E,\Delta E}$ be the [[stat-mech/microcanonical-shell|microcanonical shell]].

## Definition (finite-thickness shell)
The **microcanonical measure** is the normalized restriction of Liouville measure to the shell:
$$
\mu_{E,\Delta E}(A)
\;=\;
\frac{1}{\Omega(E,\Delta E)}\int_{\Gamma}\mathbf{1}_A(x)\,\mathbf{1}_{\Sigma_{E,\Delta E}}(x)\, d\Gamma,
$$
where
$$
\Omega(E,\Delta E)
\;=\;
\int_{\Gamma}\mathbf{1}_{\Sigma_{E,\Delta E}}(x)\, d\Gamma
$$

is the shell volume. This makes $\mu_{E,\Delta E}$ a [[probability/probability-measure|probability measure]] on $\Gamma$.

Equivalently, the microcanonical density with respect to $d\Gamma$ is
$$
\rho_{E,\Delta E}(x)
\;=\;
\frac{\mathbf{1}_{\Sigma_{E,\Delta E}}(x)}{\Omega(E,\Delta E)}.
$$

## Definition (delta-function energy surface)
Formally, one can write a “surface” version concentrated on $H(x)=E$:
$$
\mu_E(dx)
\;=\;
\frac{\delta\!\big(E-H(x)\big)}{g(E)}\, d\Gamma,
$$

where $g(E)$ is the [[stat-mech/density-of-states|density of states]] ensuring normalization.

## Ensemble averages
Given an observable $A:\Gamma\to\mathbb{R}$ (a function of the [[stat-mech/microstate-classical|microstate]]), its microcanonical [[stat-mech/ensemble-average|ensemble average]] is
$$
\langle A\rangle_{\mathrm{mc}}
\;=\;
\int_{\Gamma} A(x)\, \mu_{E,\Delta E}(dx).
$$

This is the same object as the [[probability/expectation|expectation]] of $A$ under the probability distribution $\mu_{E,\Delta E}$.

## Invariance and equilibrium meaning
Because Hamiltonian time evolution preserves Liouville volume (Liouville’s theorem) and conserves energy, the microcanonical measure is stationary under the dynamics restricted to the shell. In the equilibrium picture, it encodes “equal a priori probability” among accessible microstates at fixed energy.

## Entropy connection
The associated microcanonical [[thermodynamics/thermodynamic-entropy|entropy]] is captured by the [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann entropy]]
$$
S(E,\Delta E) \;=\; k_B \ln \Omega(E,\Delta E),
$$

with [[thermodynamics/boltzmann-constant|Boltzmann's constant]] $k_B$.
