+++
id = "stat-mech-quantum/observable-algebra"
title = "Observable algebra"
kind = "knowl"
summary = "The algebra of operators used to represent observables of a quantum system; in finite dimensions typically all linear operators on the Hilbert space."
aliases = ["observable-algebra", "Observable algebra"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/observable-algebra.md"
+++

Let $\mathcal{H}$ be the system Hilbert space (see [[quantum-foundations/complex-hilbert-space-finite|finite-dimensional complex Hilbert space]]). An **observable algebra** is a unital $*$-algebra $\mathcal{A}$ of operators acting on $\mathcal{H}$, meaning:

1. $\mathcal{A}$ is closed under addition and scalar multiplication.
2. If $A,B\in\mathcal{A}$ then $AB\in\mathcal{A}$ (closure under multiplication).
3. If $A\in\mathcal{A}$ then $A^\dagger \in \mathcal{A}$ (closure under adjoint).
4. The identity operator $I$ belongs to $\mathcal{A}$.

In the standard finite-dimensional setting one takes
$\mathcal{A} = \mathcal{B}(\mathcal{H})$,
the algebra of all [[quantum-foundations/bounded-operator-hilbert|bounded operators]] on $\mathcal{H}$ (equivalently, all complex matrices in a chosen basis; see [[linear-algebra/matrix|matrix]]).

An **observable** is a [[quantum-foundations/self-adjoint-operator-observable|self-adjoint]] element $A \in \mathcal{A}$; its spectral projections encode measurement outcomes.

A **state** on $\mathcal{A}$ can be defined abstractly as a linear map $\omega:\mathcal{A}\to\mathbb{C}$ that is positive ($\omega(A^\dagger A)\ge 0$) and normalized ($\omega(I)=1$). In finite dimensions, every such state is represented by a [[stat-mech-quantum/density-operator-state|density-operator state]] $\rho$ via
$$
\omega(A)=\operatorname{Tr}(\rho A),
$$
using the [[quantum-foundations/trace-operator|trace]].

## Physical interpretation
- $\mathcal{A}$ is the mathematical container for “what you can measure” and “how measurements combine.”
- Noncommutativity ($AB\neq BA$) encodes **incompatible observables** and the impossibility of assigning sharp values to all observables simultaneously.
- Commutative subalgebras behave like classical algebras of random variables, describing compatible families of measurements.

## Key properties
- **$*$-structure and reality:** Self-adjoint elements correspond to real-valued measurement outcomes.
- **Positivity:** Operators of the form $A^\dagger A$ are positive; states must assign them nonnegative expectation values.
- **Expectation values:** The operational content of the algebra is summarized by the [[stat-mech-quantum/quantum-expectation-value|expectation functional]] $A\mapsto \omega(A)$.
- **Subsystem structure:** For composite systems, observables typically include tensor-product forms; reduced descriptions use the [[quantum-foundations/partial-trace|partial trace]] to produce subsystem states.
