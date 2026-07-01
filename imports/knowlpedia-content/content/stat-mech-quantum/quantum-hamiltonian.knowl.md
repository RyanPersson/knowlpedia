+++
id = "stat-mech-quantum/quantum-hamiltonian"
title = "Quantum Hamiltonian"
kind = "knowl"
summary = "A self-adjoint operator representing energy and generating unitary time evolution; it also defines the Gibbs state and quantum partition function."
aliases = ["quantum-hamiltonian", "Quantum Hamiltonian"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/quantum-hamiltonian.md"
+++

A **quantum Hamiltonian** is a [[quantum-foundations/self-adjoint-operator-observable|self-adjoint operator]] $H$ acting on the system Hilbert space $\mathcal{H}$ (or, more generally, a self-adjoint element of the [[stat-mech-quantum/observable-algebra|observable algebra]]).

In finite dimension, self-adjointness means $H=H^\dagger$, so $H$ admits a spectral decomposition
$$
H = \sum_{n} E_n P_n,
$$

where $E_n \in \mathbb{R}$ are eigenvalues (energies) and $P_n$ are the corresponding orthogonal projections. See [[quantum-foundations/spectrum-self-adjoint-finite|spectrum of a self-adjoint operator]] for details in finite dimension.

The Hamiltonian generates unitary time evolution:
$$
U_t = e^{- \frac{i}{\hbar} t H},
\qquad
\rho(t) = U_t\,\rho(0)\,U_t^\dagger,
\qquad
A(t)=U_t^\dagger A(0) U_t,
$$

for states $\rho$ and observables $A$.

In equilibrium statistical mechanics, for inverse temperature $\beta$ (see [[thermodynamics/inverse-temperature-beta|inverse temperature beta]]), one defines the [[stat-mech-quantum/quantum-partition-function|quantum partition function]]
$$
Z(\beta) = \operatorname{Tr}\!\left(e^{-\beta H}\right),
$$
and the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]]
$$
\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)}.
$$

## Physical interpretation
- $H$ is the **energy observable**: measuring energy yields an eigenvalue $E_n$ with Born-rule probabilities determined by the state.
- $H$ sets the system’s **dynamics** (closed system evolution is unitary and energy-conserving when $H$ is time-independent).
- Through $e^{-\beta H}$ it governs **thermal weighting**: low-energy states are favored when $\beta>0$.

## Key properties
- **Real spectrum:** Self-adjointness implies energies $E_n$ are real and eigenprojections resolve the identity.
- **Energy zero-point irrelevance:** Replacing $H$ by $H+c\,I$ shifts all energies by $c$ but leaves $\rho_\beta$ unchanged, since $e^{-\beta(H+cI)} = e^{-\beta c} e^{-\beta H}$ and the scalar cancels in normalization.
- **Degeneracy and symmetry:** If distinct microstates share the same $E_n$, the corresponding eigenspace is degenerate; symmetries often explain degeneracies.
- **Conservation laws:** If an observable $A$ satisfies $[A,H]=0$, then $A$ is conserved under the Heisenberg evolution $A(t)$.
