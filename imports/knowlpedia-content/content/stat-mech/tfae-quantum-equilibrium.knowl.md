+++
id = "stat-mech/tfae-quantum-equilibrium"
title = "TFAE: quantum equilibrium at inverse temperature β"
kind = "knowl"
summary = "Equivalent characterizations of thermal equilibrium for a finite quantum system: Gibbs form, KMS condition, and variational (entropy/free-energy) principles."
aliases = ["tfae-quantum-equilibrium", "TFAE: quantum equilibrium at inverse temperature β"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/tfae-quantum-equilibrium.md"
+++

Fix a finite quantum system with Hamiltonian $H$ and states given by a [[quantum-foundations/density-operator|density operator]] $\rho$ (positive, trace $1$). Let $\beta = 1/(k_B T)$ where $T$ is the [[thermodynamics/temperature-thermo|temperature]].

Then the following are equivalent (TFAE):

1. **Gibbs form (canonical state).**
   $\rho$ equals the [[stat-mech-quantum/gibbs-state-quantum|Gibbs state]]
   $$\rho_\beta = \frac{e^{-\beta H}}{Z(\beta)}, \qquad Z(\beta)=\mathrm{Tr}\,e^{-\beta H},$$

   where $Z(\beta)$ is the [[stat-mech-quantum/quantum-partition-function|quantum partition function]].

2. **Finite-system KMS condition.**
   With Heisenberg dynamics $\tau_t(A)=e^{itH}Ae^{-itH}$, the state $\omega(A)=\mathrm{Tr}(\rho A)$ satisfies the [[stat-mech-quantum/kms-condition-finite|KMS condition (finite)]] at inverse temperature $\beta$: for all observables $A,B$, the function
   $$F_{A,B}(t)=\omega\!\big(A\,\tau_t(B)\big)$$

   extends to a function analytic in the strip $0<\mathrm{Im}\,z<\beta$ with boundary values
   $$F_{A,B}(t+i\beta)=\omega\!\big(\tau_t(B)\,A\big).$$

3. **Free-energy minimizer (variational principle).**
   $\rho$ minimizes the (Helmholtz) free-energy functional
   $$\mathcal F_\beta(\rho)=\mathrm{Tr}(\rho H)-\beta^{-1}S(\rho),$$

   where $S(\rho)=-\mathrm{Tr}(\rho\log\rho)$ is the [[quantum-foundations/von-neumann-entropy|von Neumann entropy]]. Equivalently,
   $$\mathcal F_\beta(\rho)\ge \mathcal F_\beta(\rho_\beta) \quad\text{for all density operators }\rho.$$
   (Compare with [[stat-mech/free-energy-statistical|statistical free energy]] in the classical setting.)

4. **Maximum entropy subject to mean energy (Lagrange multiplier form).**
   For fixed mean energy $U=\mathrm{Tr}(\rho H)$, the state $\rho$ maximizes $S(\rho)$ among all density operators with that same $U$; the maximizer is of Gibbs form with some $\beta$.

5. **Relative-entropy gap identity.**
   For all density operators $\rho$,
   $$\mathcal F_\beta(\rho)-\mathcal F_\beta(\rho_\beta)=\beta^{-1}D(\rho\|\rho_\beta)\ge 0,$$

   where $D(\rho\|\sigma)=\mathrm{Tr}(\rho(\log\rho-\log\sigma))$ is the quantum analogue of [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]].

Prerequisites: [[quantum-foundations/density-operator|density operators]], [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs states]], [[stat-mech-quantum/kms-condition-finite|KMS condition]], and [[thermodynamics/temperature-thermo|temperature]].
