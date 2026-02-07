---
title: "Concavity of the von Neumann entropy"
description: "The von Neumann entropy is concave on density operators: mixing quantum states cannot decrease entropy."
---

Let $\rho$ be a {{< knowl id="density-operator" section="quantum-foundations" text="density operator" >}} on a finite-dimensional Hilbert space. Its {{< knowl id="von-neumann-entropy" section="quantum-foundations" text="von Neumann entropy" >}} is
$S(\rho) = -\mathrm{Tr}(\rho \log \rho)$.

## Statement
For any density operators $\rho_1,\dots,\rho_n$ and any probabilities $p_1,\dots,p_n$ with $\sum_i p_i = 1$, define the mixture
$\bar\rho = \sum_{i=1}^n p_i \rho_i$.
Then
$$
S(\bar\rho) \ge \sum_{i=1}^n p_i\, S(\rho_i).
$$

## Key hypotheses
- Each $\rho_i$ is positive semidefinite and has unit trace: $\rho_i \succeq 0$ and $\mathrm{Tr}(\rho_i)=1$.
- The coefficients form a probability vector: $p_i \ge 0$ and $\sum_i p_i = 1$.

## Key conclusion
- The map $\rho \mapsto S(\rho)$ is **concave** on the convex set of density operators. In particular, classical randomization (“forgetting which state was prepared”) cannot decrease entropy.

Thermodynamically, this expresses the idea that coarse-graining or mixing increases uncertainty: entropy is increased by ignoring classical information about the preparation.
