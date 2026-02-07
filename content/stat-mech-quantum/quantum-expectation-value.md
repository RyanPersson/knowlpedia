---
title: "Quantum expectation value"
description: "Expectation of an observable A in state ρ: ⟨A⟩=Tr(ρA); in equilibrium ⟨A⟩β=Tr(ρβA)."
---


Let $\mathcal H$ be a finite-dimensional Hilbert space and let $A$ be an observable, represented as a self-adjoint element of the observable algebra ({{< knowl id="observable-algebra" text="observable algebra" >}}). Let $\rho$ be a quantum state given by a density operator ({{< knowl id="density-operator-state" text="density-operator state" >}}; compare {{< knowl id="density-operator" section="quantum-foundations" text="density operator" >}}).

The **expectation value** of $A$ in state $\rho$ is
$$
\langle A\rangle_\rho \;=\; \operatorname{Tr}(\rho A),
$$

where $\operatorname{Tr}$ is the operator trace ({{< knowl id="trace-operator" section="quantum-foundations" text="trace" >}}).

In thermal equilibrium at inverse temperature $\beta>0$ ({{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature β" >}}), one typically uses the Gibbs state ({{< knowl id="gibbs-state-quantum" text="quantum Gibbs state" >}}) $\rho_\beta$ and writes
$$
\langle A\rangle_\beta \;=\; \operatorname{Tr}(\rho_\beta A).
$$

This is the quantum analogue of the classical ensemble average ({{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}}).

## Physical interpretation

$\langle A\rangle_\rho$ is the theoretical prediction for the average outcome of many measurements of the observable $A$ on identically prepared systems in state $\rho$. In equilibrium, $\langle A\rangle_\beta$ is the thermal average at temperature $T=(k_B\beta)^{-1}$ (see {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} and {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}).

## Key properties

1. **Linearity.**  
   For scalars $a,b$ and observables $A,B$,
   $$
   \langle aA+bB\rangle_\rho \;=\; a\langle A\rangle_\rho + b\langle B\rangle_\rho.
   $$

2. **Normalization and reality.**  
   $\langle I\rangle_\rho = 1$. If $A$ is self-adjoint, then $\langle A\rangle_\rho$ is real.

3. **Positivity.**  
   If $A$ is positive semidefinite, then $\langle A\rangle_\rho \ge 0$. In particular, for a projector $P$, $\langle P\rangle_\rho$ is the probability that the corresponding yes/no measurement yields “yes”.

4. **Bounds by operator norm.**  
   In finite dimension,
   $$
   |\langle A\rangle_\rho|\;\le\;\|A\|,
   $$

   where $\|A\|$ is the operator norm (see {{< knowl id="bounded-operator-hilbert" section="quantum-foundations" text="bounded operator" >}} for context).

5. **Pure-state specialization.**  
   If $\rho=|\psi\rangle\langle\psi|$ is a pure state ({{< knowl id="pure-state-quantum" section="quantum-foundations" text="pure state" >}}), then
   $$
   \langle A\rangle_\rho \;=\;\langle\psi|A|\psi\rangle.
   $$

6. **Parameter derivatives in Gibbs equilibrium.**  
   If the Hamiltonian depends on a parameter $\lambda$ via $H(\lambda)=H_0+\lambda V$, then the quantum partition function ({{< knowl id="quantum-partition-function" text="quantum partition function" >}}) satisfies
   $$
   \frac{\partial}{\partial\lambda}\log Z(\beta,\lambda)\;=\;-\beta\,\langle V\rangle_{\beta,\lambda}.
   $$
   Equivalently, the equilibrium free energy ({{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}) obeys
   $$
   \frac{\partial}{\partial\lambda}F(\beta,\lambda)\;=\;\langle V\rangle_{\beta,\lambda}.
   $$

7. **Gateway to correlations.**  
   Expectations of products and time-evolved observables define correlation functions ({{< knowl id="quantum-correlation-function" section="stat-mech" text="quantum correlation function" >}}), which quantify fluctuations and response beyond mean values.
