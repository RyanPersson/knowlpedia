---
title: "Observable algebra"
description: "The algebra of operators used to represent observables of a quantum system; in finite dimensions typically all linear operators on the Hilbert space."
---

Let $\mathcal{H}$ be the system Hilbert space (see {{< knowl id="complex-hilbert-space-finite" section="quantum-foundations" text="finite-dimensional complex Hilbert space" >}}). An **observable algebra** is a unital $*$-algebra $\mathcal{A}$ of operators acting on $\mathcal{H}$, meaning:

1. $\mathcal{A}$ is closed under addition and scalar multiplication.
2. If $A,B\in\mathcal{A}$ then $AB\in\mathcal{A}$ (closure under multiplication).
3. If $A\in\mathcal{A}$ then $A^\dagger \in \mathcal{A}$ (closure under adjoint).
4. The identity operator $I$ belongs to $\mathcal{A}$.

In the standard finite-dimensional setting one takes
$\mathcal{A} = \mathcal{B}(\mathcal{H})$,
the algebra of all {{< knowl id="bounded-operator-hilbert" section="quantum-foundations" text="bounded operators" >}} on $\mathcal{H}$ (equivalently, all complex matrices in a chosen basis; see {{< knowl id="matrix" section="linear-algebra" text="matrix" >}}).

An **observable** is a {{< knowl id="self-adjoint-operator-observable" section="quantum-foundations" text="self-adjoint" >}} element $A \in \mathcal{A}$; its spectral projections encode measurement outcomes.

A **state** on $\mathcal{A}$ can be defined abstractly as a linear map $\omega:\mathcal{A}\to\mathbb{C}$ that is positive ($\omega(A^\dagger A)\ge 0$) and normalized ($\omega(I)=1$). In finite dimensions, every such state is represented by a {{< knowl id="density-operator-state" text="density-operator state" >}} $\rho$ via
$$
\omega(A)=\operatorname{Tr}(\rho A),
$$
using the {{< knowl id="trace-operator" section="quantum-foundations" text="trace" >}}.

## Physical interpretation
- $\mathcal{A}$ is the mathematical container for “what you can measure” and “how measurements combine.”
- Noncommutativity ($AB\neq BA$) encodes **incompatible observables** and the impossibility of assigning sharp values to all observables simultaneously.
- Commutative subalgebras behave like classical algebras of random variables, describing compatible families of measurements.

## Key properties
- **$*$-structure and reality:** Self-adjoint elements correspond to real-valued measurement outcomes.
- **Positivity:** Operators of the form $A^\dagger A$ are positive; states must assign them nonnegative expectation values.
- **Expectation values:** The operational content of the algebra is summarized by the {{< knowl id="quantum-expectation-value" text="expectation functional" >}} $A\mapsto \omega(A)$.
- **Subsystem structure:** For composite systems, observables typically include tensor-product forms; reduced descriptions use the {{< knowl id="partial-trace" section="quantum-foundations" text="partial trace" >}} to produce subsystem states.
