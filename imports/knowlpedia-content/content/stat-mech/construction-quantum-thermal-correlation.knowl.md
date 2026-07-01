+++
id = "stat-mech/construction-quantum-thermal-correlation"
title = "Quantum thermal correlation function (construction)"
kind = "knowl"
summary = "Equilibrium time and imaginary-time correlation functions computed from the thermal density matrix; they satisfy the KMS condition and control response."
aliases = ["construction-quantum-thermal-correlation", "Quantum thermal correlation function (construction)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-quantum-thermal-correlation.md"
+++

A **quantum thermal correlation function** is a two-point (or multipoint) expectation value in a thermal equilibrium state, with operators evolved in time. These objects generalize the [[stat-mech/correlation-function-two-point|two-point correlation function]] of classical statistical mechanics and are central for linear response and spectroscopy.

## Thermal expectation and time evolution

In the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta$, the thermal state is
$$
\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)},
\qquad
Z(\beta)=\operatorname{Tr}\big(e^{-\beta H}\big),
$$

with $Z(\beta)$ the [[stat-mech/partition-function-canonical|canonical partition function]]. The thermal expectation of an observable $X$ is the [[stat-mech/ensemble-average|ensemble average]]
$$
\langle X\rangle_\beta := \operatorname{Tr}(\rho_\beta X).
$$

In the Heisenberg picture, the real-time evolution of an operator $A$ is
$$
A(t) := e^{iHt/\hbar}\,A\,e^{-iHt/\hbar}.
$$

## Real-time and imaginary-time two-point functions

Given two observables $A$ and $B$, the **real-time thermal correlation function** is
$$
C_{AB}(t) := \langle A(t)\,B\rangle_\beta
= \operatorname{Tr}\!\big(\rho_\beta\, A(t)\,B\big).
$$

The **imaginary-time (Matsubara) correlation function** is defined for $\tau\in[0,\beta]$ by
$$
G_{AB}(\tau) := \langle A(-i\tau)\,B\rangle_\beta
= \operatorname{Tr}\!\big(\rho_\beta\, e^{\tau H}\,A\,e^{-\tau H}\,B\big).
$$
Imaginary-time correlations are particularly natural in path-integral and transfer-matrix approaches (compare [[stat-mech/construction-transfer-matrix-1d|transfer matrix constructions]] in one dimension).

If $A$ and $B$ are supported in a finite region, the same correlations can be computed using the [[stat-mech/construction-reduced-density-matrix|reduced density matrix]] for that region instead of the full $\rho_\beta$.

## Connected thermal correlations

The **connected** (or truncated) two-point function is obtained by subtracting the product of means:
$$
\langle AB\rangle_{\beta,c} := \langle AB\rangle_\beta - \langle A\rangle_\beta\,\langle B\rangle_\beta.
$$
This is the quantum counterpart of the [[stat-mech/connected-correlation-function|connected correlation function]] and is the basic building block for cumulant expansions (see [[stat-mech/construction-connected-correlations-cumulants|connected correlations via cumulants]]).

## KMS condition (thermal analyticity)

A defining equilibrium property of thermal correlations is the **KMS condition**, which can be stated (for bosonic observables) as the analyticity/periodicity relation
$$
C_{AB}(t-i\beta) = \langle B\,A(t)\rangle_\beta,
$$
whenever the analytic continuation is well-defined. This identity encodes equilibrium and replaces time-translation invariance plus detailed balance in the quantum setting.

## Spectral (energy-eigenbasis) representation

Let $H|n\rangle=E_n|n\rangle$ and define matrix elements $A_{nm}=\langle n|A|m\rangle$. Then
$$
C_{AB}(t)
={}
\frac{1}{Z(\beta)}\sum_{n,m}
e^{-\beta E_n}\,
e^{i(E_n-E_m)t/\hbar}\,
A_{nm}\,B_{mn}.
$$
This formula shows that thermal correlations probe energy differences and selection rules through operator matrix elements.

## Physical interpretation and response

- **Fluctuations:** $C_{AA}(t)$ quantifies how fluctuations of $A$ persist over time in equilibrium, complementing static quantities like [[stat-mech/variance-observable-ensemble|variance in an ensemble]].
- **Susceptibility:** static and dynamical response coefficients (see [[stat-mech/susceptibility-stat-mech|susceptibility]]) can be expressed in terms of time-integrated *connected* thermal correlations; in many settings, imaginary-time integrals of $G_{AA}(\tau)$ control static susceptibilities.
- **Clustering:** in phases with finite [[stat-mech/correlation-length|correlation length]], connected thermal correlations decay in space (and often in imaginary time), reflecting locality and the absence of long-range order.

These correlation functions are also the natural objects that appear when differentiating $\log Z$ with respect to sources, matching the general “derivatives of $\log Z$ produce cumulants” philosophy in [[stat-mech/construction-cumulant-generating-function|cumulant generating constructions]].
