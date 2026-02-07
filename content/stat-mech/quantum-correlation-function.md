---
title: "Quantum correlation function"
description: "Thermal two-point function GAB(t)=Tr(ρβ A(t)B) and its KMS/imaginary-time properties in finite quantum systems."
---


Let $H$ be the Hamiltonian ({{< knowl id="quantum-hamiltonian" section="stat-mech-quantum" text="quantum Hamiltonian" >}}) on a finite-dimensional Hilbert space, and let $\tau_t$ denote the Heisenberg time evolution on observables ({{< knowl id="observable-algebra" section="stat-mech-quantum" text="observable algebra" >}}),
$$
\tau_t(A)\;=\;e^{itH}Ae^{-itH}.
$$

Let $\rho$ be a density operator state ({{< knowl id="density-operator-state" section="stat-mech-quantum" text="density-operator state" >}}). The **(real-time) two-point correlation function** of observables $A,B$ in state $\rho$ is
$$
G_{A,B}^{(\rho)}(t)\;=\;\operatorname{Tr}\!\big(\rho\,\tau_t(A)\,B\big).
$$

In thermal equilibrium at inverse temperature $\beta>0$ ({{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature β" >}}), one uses the Gibbs state ({{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="quantum Gibbs state" >}}) $\rho_\beta$ and writes
$$
G_{A,B}(t)\;=\;\operatorname{Tr}\!\big(\rho_\beta\,\tau_t(A)\,B\big).
$$

A commonly used **connected** (or “cumulant”) correlator subtracts the product of one-point functions:
$$
G^{\mathrm c}_{A,B}(t)\;=\;G_{A,B}(t)\;-\;\langle A\rangle_\beta\,\langle B\rangle_\beta,
$$

where $\langle\cdot\rangle_\beta$ is the thermal {{< knowl id="quantum-expectation-value" section="stat-mech-quantum" text="quantum expectation value" >}}.

This is the quantum analogue of the classical {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}.

## Physical interpretation

Two-point correlation functions quantify:

- **Fluctuations:** how deviations of $A$ from its mean co-vary with $B$ at later times.
- **Dynamical memory:** how quickly correlations decay (relaxation and mixing).
- **Response:** via linear response theory, commutator-based correlators determine susceptibilities and transport coefficients.

In equilibrium, correlation functions are time-translation invariant and obey characteristic “imaginary-time” relations captured by the {{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition (finite)" >}}.

## Key properties

1. **Spectral (energy-eigenbasis) representation.**  
   If $H|n\rangle=E_n|n\rangle$ and $A_{nm}=\langle n|A|m\rangle$, then for the Gibbs state,
   $$
   G_{A,B}(t)\;=\;\frac{1}{Z(\beta)}\sum_{n,m} e^{-\beta E_n}\,e^{it(E_n-E_m)}\,A_{nm}\,B_{mn},
   $$

   where $Z(\beta)$ is the {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="quantum partition function" >}}.

2. **Equilibrium (stationarity).**  
   In the Gibbs state, $G_{A,B}(t)$ depends only on the time difference because the state is invariant under $\tau_t$. In particular, $\langle \tau_t(A)\rangle_\beta=\langle A\rangle_\beta$.

3. **KMS (imaginary-time shift) relation.**  
   The Gibbs state is a $\beta$-KMS state ({{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition (finite)" >}}). One consequence is that the function
   $$
   F_{A,B}(t)\;=\;\langle A\,\tau_t(B)\rangle_\beta
   $$
   extends to complex time and satisfies the boundary identity
   $$
   \langle A\,\tau_{t+i\beta}(B)\rangle_\beta \;=\;\langle \tau_t(B)\,A\rangle_\beta.
   $$
   This is the precise statement of thermal “imaginary-time periodicity” (up to exchanging operator order).

4. **Imaginary-time (Matsubara) correlators.**  
   For $\tau\in[0,\beta]$, define the imaginary-time correlator
   $$
   G_{A,B}(\tau)\;=\;\operatorname{Tr}\!\big(\rho_\beta\,\tau_{-i\tau}(A)\,B\big).
   $$

   The KMS condition determines how $G_{A,B}(\tau)$ behaves at the endpoints $\tau=0$ and $\tau=\beta$ via the order-exchange relation above.

5. **Fourier-domain detailed-balance form (finite systems).**  
   If one defines a frequency-space correlation spectrum by Fourier transforming the real-time correlator, the KMS condition implies a thermal detailed-balance relation of the schematic form
   $$
   S_{A,B}(-\omega)\;=\;e^{-\beta\omega}\,S_{B,A}(\omega),
   $$

   encoding the asymmetry between absorption and emission at temperature $T$.

6. **Special cases and reductions.**
   - If $A$ commutes with $H$, then $\tau_t(A)=A$ and $G_{A,B}(t)$ is constant in time.
   - If $A=B$ is self-adjoint, then $G^{\mathrm c}_{A,A}(0)$ is the thermal variance of $A$, a static fluctuation measure.

7. **Connection to thermodynamics.**  
   Static (equal-time) correlations and susceptibilities often control derivatives of thermodynamic potentials such as the Helmholtz free energy ({{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}) with respect to parameters that couple to observables.
