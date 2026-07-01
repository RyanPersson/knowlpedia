+++
id = "stat-mech-quantum/quantum-microstate"
title = "Quantum microstate"
kind = "knowl"
summary = "A maximally specific state of a quantum system, represented by a pure state (ray) or equivalently a rank-one projector."
aliases = ["quantum-microstate", "Quantum microstate"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/quantum-microstate.md"
+++

In quantum statistical mechanics, a **quantum microstate** is typically identified with a **pure state** of the system (see [[quantum-foundations/pure-state-quantum|pure state]]).

Concretely, in finite dimensions a microstate can be represented by either of the equivalent data:

1. A normalized vector $|\psi\rangle \in \mathcal{H}$ with $\langle\psi|\psi\rangle = 1$, where vectors differing by a global phase represent the same physical state: $|\psi\rangle \sim e^{i\theta}|\psi\rangle$.
2. A rank-one projection (density operator)
$$
\rho_\psi = |\psi\rangle\langle\psi|.
$$

Given an observable $A$ in the [[stat-mech-quantum/observable-algebra|observable algebra]], the expected outcome in the microstate $|\psi\rangle$ is
$$
\langle A\rangle_\psi = \langle \psi|A|\psi\rangle
= \operatorname{Tr}(\rho_\psi A).
$$
This matches the general [[stat-mech-quantum/density-operator-state|density-operator]] formula for expectations.

A particularly important class of microstates in statistical mechanics are **energy eigenstates**: if $H$ is the [[stat-mech-quantum/quantum-hamiltonian|Hamiltonian]] and $H|\phi_n\rangle = E_n|\phi_n\rangle$, then $|\phi_n\rangle$ is a microstate with definite energy $E_n$ (see [[linear-algebra/eigenvector|eigenvector]]).

## Physical interpretation
- A microstate is the most refined description allowed by quantum theory for an isolated system: it specifies all measurement statistics but generally not sharp values for all observables.
- Superpositions of energy eigenstates are also microstates; “being in a microstate” does not mean having definite classical phase-space coordinates.

## Key properties
- **Extremality:** Microstates are extreme points of the convex set of [[stat-mech-quantum/density-operator-state|density-operator states]]; they cannot be expressed as nontrivial convex mixtures of other states.
- **Zero von Neumann entropy:** For $\rho_\psi = |\psi\rangle\langle\psi|$, the [[quantum-foundations/von-neumann-entropy|von Neumann entropy]] satisfies $S(\rho_\psi)=0$.
- **Projector condition:** $\rho_\psi$ is pure iff $\rho_\psi^2=\rho_\psi$ (equivalently, $\operatorname{Tr}(\rho_\psi^2)=1$).
- **Basis dependence of “definite values”:** A microstate has definite value for an observable only when it lies in an eigenstate of that observable.
