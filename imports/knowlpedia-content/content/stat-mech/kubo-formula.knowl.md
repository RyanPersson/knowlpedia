+++
id = "stat-mech/kubo-formula"
title = "Kubo formula (linear response)"
kind = "knowl"
summary = "General expression for the linear response kernel/susceptibility in terms of equilibrium correlation functions; commutator form in quantum mechanics."
aliases = ["kubo-formula", "Kubo formula (linear response)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/kubo-formula.md"
+++

## Setup

Perturb an equilibrium system by a weak field $h(t)$ coupled to an observable $B$:
$$
H \;\mapsto\; H - h(t)\,B.
$$

For an observable $A$, define the linear response kernel $R_{AB}(t)$ by
$$
\delta\langle A(t)\rangle = \int_{-\infty}^{t} R_{AB}(t-s)\,h(s)\,ds.
$$

The equilibrium expectation is taken in a [[stat-mech/canonical-ensemble|canonical ensemble]] (classical) or a [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]] (quantum).

## Quantum Kubo formula (commutator form)

For a quantum system with Heisenberg time evolution, the Kubo formula states
$$
R_{AB}(t) = \frac{i}{\hbar}\,\theta(t)\,\langle [A(t),B(0)]\rangle_{\beta},
$$

where $[A,B]=AB-BA$ and $\langle\cdot\rangle_\beta$ is the expectation in the Gibbs state (equivalently built from the [[stat-mech-quantum/quantum-partition-function|quantum partition function]]).

The causal susceptibility is the Fourier transform $\chi_{AB}(\omega)=\int_0^\infty e^{i\omega t} R_{AB}(t)\,dt$.

## Classical analogue

In classical Hamiltonian systems, a parallel statement replaces commutators by Poisson brackets (or, equivalently, relates response to suitable time derivatives of equilibrium correlations). In many common conventions one may write
$$
R_{AB}(t)=\beta\,\theta(t)\,\langle \dot{B}(0)\,A(t)\rangle_{\mathrm{eq}},
$$
which is a standard route to the [[stat-mech/fluctuation-dissipation-theorem|fluctuation–dissipation theorem]].

## Uses

- **Transport coefficients:** Applying the Kubo formula with currents as observables yields the [[stat-mech/green-kubo-relations|Green–Kubo relations]].
- **Equilibrium structure:** In quantum systems, analytic properties encoded by the [[stat-mech-quantum/kms-condition-finite|KMS condition]] control the relationship between response and correlation functions.
- **Correlation input:** The building blocks are equilibrium [[stat-mech/correlation-function-two-point|two-point correlations]] and [[stat-mech/ensemble-average|ensemble averages]].

## Interpretation

Kubo’s formula is the precise statement that, to first order in the perturbing field, the deviation from equilibrium is determined entirely by equilibrium dynamical correlations of the unperturbed system.
