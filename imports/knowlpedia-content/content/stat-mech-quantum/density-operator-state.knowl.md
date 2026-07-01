+++
id = "stat-mech-quantum/density-operator-state"
title = "Density-operator state"
kind = "knowl"
summary = "A quantum state represented by a positive operator of unit trace; it encodes statistical mixtures and computes expectations via the trace."
aliases = ["density-operator-state", "Density-operator state"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/density-operator-state.md"
+++

Let $\mathcal{H}$ be a finite-dimensional Hilbert space. A **density-operator state** (often just “density matrix”) is an operator $\rho$ on $\mathcal{H}$ such that:

1. **Positivity:** $\rho \ge 0$, meaning $\langle\psi|\rho|\psi\rangle \ge 0$ for all $|\psi\rangle \in \mathcal{H}$.
2. **Normalization:** $\operatorname{Tr}(\rho)=1$, where $\operatorname{Tr}$ is the [[quantum-foundations/trace-operator|trace]].

This is the concrete operator version of a quantum [[quantum-foundations/density-operator|density operator]].

Given an observable $A$ (a self-adjoint element of the [[stat-mech-quantum/observable-algebra|observable algebra]]), the expectation value in the state $\rho$ is
$$
\langle A\rangle_\rho = \operatorname{Tr}(\rho A),
$$
which defines the [[stat-mech-quantum/quantum-expectation-value|quantum expectation value]].

### Pure vs mixed
- $\rho$ is **pure** (a [[stat-mech-quantum/quantum-microstate|microstate]]) iff $\rho = |\psi\rangle\langle\psi|$ for some normalized $|\psi\rangle$; see [[quantum-foundations/pure-state-quantum|pure state]].
- $\rho$ is **mixed** iff it is not pure; see [[quantum-foundations/mixed-state-quantum|mixed state]].

A useful algebraic purity test in finite dimension is:
$$
\rho \text{ is pure } \Longleftrightarrow \operatorname{Tr}(\rho^2)=1,
\qquad
\rho \text{ mixed } \Longleftrightarrow \operatorname{Tr}(\rho^2)<1.
$$

## Physical interpretation
- $\rho$ encodes **all measurement statistics** for the system.
- Mixed states represent **classical uncertainty** about which microstate was prepared and/or **entanglement with an environment**.
- For a subsystem of a larger system, the appropriate state is the reduced density operator obtained by the [[quantum-foundations/partial-trace|partial trace]].

## Key properties
- **Convexity:** If $\rho_1,\rho_2$ are density operators and $0\le \lambda\le 1$, then $\rho=\lambda\rho_1+(1-\lambda)\rho_2$ is also a density operator. This formalizes “statistical mixing.”
- **Spectral form:** Since $\rho$ is positive and trace one, it diagonalizes as
  $$
  \rho = \sum_i p_i |i\rangle\langle i|,
  \qquad
  p_i \ge 0,\ \sum_i p_i = 1,
  $$
  so its eigenvalues act like a probability distribution over orthonormal eigenvectors.
- **Entropy:** The thermodynamic-like uncertainty in $\rho$ is quantified by the [[quantum-foundations/von-neumann-entropy|von Neumann entropy]]
  $$
  S(\rho) = -\operatorname{Tr}(\rho\log\rho).
  $$

- **Thermal equilibrium:** Given a [[stat-mech-quantum/quantum-hamiltonian|Hamiltonian]] $H$ and inverse temperature $\beta$, the canonical equilibrium state is the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]]
  $$
  \rho_\beta = \frac{e^{-\beta H}}{\operatorname{Tr}(e^{-\beta H})},
  $$
  where the denominator is the [[stat-mech-quantum/quantum-partition-function|quantum partition function]].
