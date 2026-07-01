+++
id = "quantum-foundations/density-operator"
title = "Density Operator"
kind = "knowl"
summary = "A positive semidefinite trace-one operator representing the state of a quantum system, allowing both pure and statistical mixtures."
aliases = ["density-operator", "Density Operator"]
domains = ["quantum-foundations"]
legacy_source_path = "quantum-foundations/density-operator.md"
+++

Let \(H\) be a complex Hilbert space (typically finite-dimensional in basic quantum theory). A **density operator** (also called a **density matrix**) is an operator \(\rho:H\to H\) such that:

1. **Positivity:** \(\rho \ge 0\), meaning \(\langle \psi,\rho\psi\rangle \ge 0\) for all \(\psi\in H\).
2. **Unit trace:** \(\operatorname{Tr}(\rho)=1\), where \(\operatorname{Tr}\) is the operator trace ([[quantum-foundations/trace-operator|Trace Operator]]).

In finite dimension, these conditions are equivalent to \(\rho\) being a positive semidefinite matrix with trace \(1\).

## Basic structural facts (finite dimension)
- \(\rho\) is automatically self-adjoint: \(\rho=\rho^\ast\).
- All eigenvalues of \(\rho\) are real and lie in \([0,1]\).
- The eigenvalues sum to \(1\): if \(\rho\) has eigenvalues \((p_i)\), then \(\sum_i p_i=1\).

Thus \(\rho\) admits a spectral decomposition
\[
\rho = \sum_i p_i\,|\phi_i\rangle\langle \phi_i|,
\]
with \((\phi_i)\) orthonormal and \(p_i\ge 0\), \(\sum_i p_i=1\).

## Pure vs mixed
- \(\rho\) is a **pure state** iff it has rank \(1\), equivalently iff \(\rho^2=\rho\), equivalently iff \(\operatorname{Tr}(\rho^2)=1\). (See [[quantum-foundations/pure-state-quantum|Pure State Quantum]].)
- Otherwise \(\rho\) is **mixed** and can be written as a convex combination \(\rho=\sum_k q_k |\psi_k\rangle\langle\psi_k|\) with \(q_k\ge 0\), \(\sum_k q_k=1\). (See [[quantum-foundations/mixed-state-quantum|Mixed State Quantum]].)

## Expectation values (Born rule in operator form)
If \(A\) is an observable (a self-adjoint operator, see [[quantum-foundations/self-adjoint-operator-observable|Self Adjoint Operator Observable]]), then the expectation value in state \(\rho\) is
\[
\mathbb{E}_\rho[A] = \operatorname{Tr}(\rho A).
\]
This formula unifies pure and mixed states.

## Dynamics and transformations (finite dimension)
- **Unitary evolution:** if \(U\) is unitary, then \(\rho\) evolves as \(\rho \mapsto U\rho U^\ast\).
- **Projective measurement:** spectral projectors \(P_i\) (as in [[quantum-foundations/spectrum-self-adjoint-finite|Spectrum Self Adjoint Finite]]) define outcome probabilities \(\Pr(i)=\operatorname{Tr}(\rho P_i)\).

## Information-theoretic quantities
Two common functionals of \(\rho\) are:

- Von Neumann entropy: \(S(\rho) = -\operatorname{Tr}(\rho\log\rho)\) (see [[quantum-foundations/von-neumann-entropy|Von Neumann Entropy]]).
- Relative entropy: \(D(\rho\|\sigma)=\operatorname{Tr}(\rho(\log\rho-\log\sigma))\) under suitable support conditions (see [[quantum-foundations/quantum-relative-entropy|Quantum Relative Entropy]]).
