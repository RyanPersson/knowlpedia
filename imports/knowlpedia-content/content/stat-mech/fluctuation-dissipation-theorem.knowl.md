+++
id = "stat-mech/fluctuation-dissipation-theorem"
title = "Fluctuation–dissipation theorem (FDT)"
kind = "knowl"
summary = "Identifies linear response (dissipation) with equilibrium fluctuations via time-correlation functions; classical and quantum forms."
aliases = ["fluctuation-dissipation-theorem", "Fluctuation–dissipation theorem (FDT)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/fluctuation-dissipation-theorem.md"
+++

## Setup (linear response)

Consider an equilibrium system perturbed by a weak time-dependent field $h(t)$ coupled to an observable $B$:
$$
H \;\mapsto\; H - h(t)\,B.
$$

For another observable $A$, the linear response is written
$$
\delta\langle A(t)\rangle = \int_{-\infty}^{t} R_{AB}(t-s)\,h(s)\,ds,
$$

where $R_{AB}(t)$ is the (causal) response kernel and $\langle\cdot\rangle$ denotes an equilibrium [[stat-mech/ensemble-average|ensemble average]].

## Classical FDT (common time-domain form)

Under standard assumptions of equilibrium and time-translation invariance (often in the [[stat-mech/canonical-ensemble|canonical ensemble]]), one form of the FDT relates the response to an equilibrium correlation:
$$
R_{AB}(t) = \beta\,\theta(t)\,\langle \dot{B}(0)\,A(t)\rangle_{\mathrm{eq}},
$$

where $\beta = 1/(k_B T)$, $\theta(t)$ is the Heaviside step function (causality), and the correlation is a [[stat-mech/correlation-function-two-point|two-point function]].

Equivalent variants differ by integration by parts or by the precise choice of conjugate variables (e.g., $R_{AB}(t)= -\beta\,\theta(t)\,\frac{d}{dt}\langle B(0)A(t)\rangle_{\mathrm{eq}}$ when boundary terms vanish).

## Quantum FDT (frequency-domain form)

In quantum equilibrium (a [[stat-mech-quantum/gibbs-state-quantum|Gibbs state]] satisfying the [[stat-mech-quantum/kms-condition-finite|KMS condition]]), let $\chi_{AB}(\omega)$ be the susceptibility (Fourier transform of the causal response) and let $S_{AB}(\omega)$ be the Fourier transform of an equilibrium correlation (appropriately symmetrized, depending on convention). A standard statement is that
$$
S_{AB}(\omega)\quad\text{is proportional to}\quad \frac{1}{1-e^{-\beta\hbar\omega}}\,\Im \chi_{AB}(\omega),
$$
so the imaginary part of the response (dissipation) is fixed by equilibrium fluctuations.

## Consequences

- **Green–Kubo:** Time-integrated equilibrium current correlations yield transport coefficients; see [[stat-mech/green-kubo-relations|Green–Kubo relations]].
- **Equilibrium input:** The FDT expresses a nonequilibrium *response* purely using equilibrium objects: temperature ([[thermodynamics/temperature-thermo|temperature]]), correlations, and the unperturbed dynamics.
- **Microscopic reversibility:** In stochastic settings, [[stat-mech/detailed-balance|detailed balance]] is a common sufficient condition behind the equilibrium structure used by FDT.

## Link to Kubo’s formula

A systematic derivation of $R_{AB}$ in both classical and quantum settings is given by the [[stat-mech/kubo-formula|Kubo formula]].
