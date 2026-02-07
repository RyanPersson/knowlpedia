---
title: "Reduced density matrix (construction)"
description: "Subsystem state obtained by tracing out degrees of freedom; it encodes all local expectations and correlations of a quantum state."
---

A **reduced density matrix** is the quantum analogue of a marginal distribution: it describes the state of a subsystem when the rest of the degrees of freedom are ignored. In quantum statistical mechanics, it is the object that turns a global thermal state into a locally testable state on a finite region.

## Definition via partial trace

Let the system Hilbert space factorize as
$\mathcal H=\mathcal H_A\otimes \mathcal H_B$,
where $A$ is the subsystem of interest and $B$ is its complement (environment).

A (mixed) quantum state is represented by a density operator $\rho$ on $\mathcal H$, which in finite dimensions is a positive semidefinite {{< knowl id="matrix" section="linear-algebra" text="matrix" >}} with {{< knowl id="trace" section="linear-algebra" text="trace" >}} equal to $1$:
$$
\rho \ge 0,
\qquad
\operatorname{Tr}_{\mathcal H}(\rho)=1.
$$

The **reduced density matrix on $A$** is defined by the partial trace over $B$:
$$
\rho_A := \operatorname{Tr}_B(\rho).
$$

It is characterized by the universal property: for every observable $O_A$ acting only on $A$,
$$
\operatorname{Tr}_{\mathcal H_A}(\rho_A\, O_A)
={}
\operatorname{Tr}_{\mathcal H}\big(\rho\, (O_A\otimes I_B)\big).
$$

Equivalently, choosing any orthonormal basis $\{|b\rangle\}$ of $\mathcal H_B$ (compatible with the {{< knowl id="inner-product" section="linear-algebra" text="inner product" >}}), one has the concrete formula
$$
\rho_A = \sum_b \langle b|\rho|b\rangle,
$$

where each $\langle b|\rho|b\rangle$ is an operator on $\mathcal H_A$.

This definition guarantees that local expectations computed using the reduced state agree with the global {{< knowl id="ensemble-average" text="ensemble average" >}}.

## Reduced thermal state in the canonical ensemble

For a quantum Hamiltonian $H$ at inverse temperature $\beta$, the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} uses the thermal density matrix
$$
\rho_\beta=\frac{e^{-\beta H}}{Z(\beta)},
\qquad
Z(\beta)=\operatorname{Tr}\big(e^{-\beta H}\big),
$$

where $Z(\beta)$ is the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}.

Given a region $A$ (e.g. a finite subset of a lattice), the **reduced thermal density matrix** is
$$
\rho_{A,\beta}
={}
\operatorname{Tr}_{A^c}\!\left(\rho_\beta\right)
={}
\frac{\operatorname{Tr}_{A^c}\!\left(e^{-\beta H}\right)}{\operatorname{Tr}\!\left(e^{-\beta H}\right)}.
$$

All local thermodynamic quantities and local correlation functions supported in $A$ can be computed from $\rho_{A,\beta}$.

## Consistency across regions and infinite-volume viewpoint

For nested finite regions $A\subset B$, reduced states satisfy a consistency (marginalization) property:
$$
\rho_A = \operatorname{Tr}_{B\setminus A}(\rho_B).
$$
This mirrors the way finite-volume marginals are consistent in classical Gibbs measures; compare the role played by a {{< knowl id="construction-dlr-specification" text="DLR specification" >}} in the classical setting. In many constructions of infinite systems, one proves existence of an infinite-volume state by controlling these finite-region reduced density matrices and then taking a suitable {{< knowl id="construction-infinite-volume-gibbs-weak-limit" text="weak limit" >}}.

## Physical interpretation

- **Local physics:** $\rho_A$ is the complete description of outcomes of measurements confined to $A$.
- **Open systems viewpoint:** tracing out $B$ represents ignorance of (or intentional coarse-graining over) the environment.
- **Entropy:** the von Neumann entropy
  $$
  S(\rho_A) = -\operatorname{Tr}(\rho_A \log \rho_A)
  $$
  is the quantum analogue of the entropy concepts discussed in {{< knowl id="gibbs-entropy-shannon" text="Gibbs/Shannon entropy" >}} and {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} (with important quantum-specific features due to entanglement).

Reduced density matrices are also the natural inputs for defining {{< knowl id="construction-quantum-thermal-correlation" text="quantum thermal correlation functions" >}} restricted to a subsystem.
