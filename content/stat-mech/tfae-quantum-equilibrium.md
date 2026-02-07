---
title: "TFAE: quantum equilibrium at inverse temperature β"
description: "Equivalent characterizations of thermal equilibrium for a finite quantum system: Gibbs form, KMS condition, and variational (entropy/free-energy) principles."
---

Fix a finite quantum system with Hamiltonian $H$ and states given by a {{< knowl id="density-operator" section="quantum-foundations" text="density operator" >}} $\rho$ (positive, trace $1$). Let $\beta = 1/(k_B T)$ where $T$ is the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.

Then the following are equivalent (TFAE):

1. **Gibbs form (canonical state).**  
   $\rho$ equals the {{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="Gibbs state" >}}
   $$\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)}, \qquad Z(\beta)=\mathrm{Tr}\,e^{-\beta H},$$

   where $Z(\beta)$ is the {{< knowl id="quantum-partition-function" section="stat-mech-quantum" text="quantum partition function" >}}.

2. **Finite-system KMS condition.**  
   With Heisenberg dynamics $\tau_t(A)=e^{itH}Ae^{-itH}$, the state $\omega(A)=\mathrm{Tr}(\rho A)$ satisfies the {{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition (finite)" >}} at inverse temperature $\beta$: for all observables $A,B$, the function
   $$F_{A,B}(t)=\omega\!\big(A\,\tau_t(B)\big)$$

   extends to a function analytic in the strip $0<\mathrm{Im}\,z<\beta$ with boundary values
   $$F_{A,B}(t+i\beta)=\omega\!\big(\tau_t(B)\,A\big).$$

3. **Free-energy minimizer (variational principle).**  
   $\rho$ minimizes the (Helmholtz) free-energy functional
   $$\mathcal F_\beta(\rho)=\mathrm{Tr}(\rho H)-\beta^{-1}S(\rho),$$

   where $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ is the {{< knowl id="von-neumann-entropy" section="quantum-foundations" text="von Neumann entropy" >}}. Equivalently,
   $$\mathcal F_\beta(\rho)\ge \mathcal F_\beta(\rho_\beta) \quad\text{for all density operators }\rho.$$
   (Compare with {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}} in the classical setting.)

4. **Maximum entropy subject to mean energy (Lagrange multiplier form).**  
   For fixed mean energy $U=\mathrm{Tr}(\rho H)$, the state $\rho$ maximizes $S(\rho)$ among all density operators with that same $U$; the maximizer is of Gibbs form with some $\beta$.

5. **Relative-entropy gap identity.**  
   For all density operators $\rho$,
   $$\mathcal F_\beta(\rho)-\mathcal F_\beta(\rho_\beta)=\beta^{-1}D(\rho\|\rho_\beta)\ge 0,$$

   where $D(\rho\|\sigma)=\mathrm{Tr}(\rho(\log\rho-\log\sigma))$ is the quantum analogue of {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}.

Prerequisites: {{< knowl id="density-operator" section="quantum-foundations" text="density operators" >}}, {{< knowl id="gibbs-state-quantum" section="stat-mech-quantum" text="quantum Gibbs states" >}}, {{< knowl id="kms-condition-finite" section="stat-mech-quantum" text="KMS condition" >}}, and {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
