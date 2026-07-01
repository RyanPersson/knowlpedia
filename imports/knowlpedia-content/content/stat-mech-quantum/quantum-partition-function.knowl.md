+++
id = "stat-mech-quantum/quantum-partition-function"
title = "Quantum partition function"
kind = "knowl"
summary = "Canonical partition function of a finite quantum system: Z(β)=Tr(e^{-βH})."
aliases = ["quantum-partition-function", "Quantum partition function"]
domains = ["stat-mech-quantum"]
legacy_source_path = "stat-mech-quantum/quantum-partition-function.md"
+++

Let $\mathcal H$ be a finite-dimensional Hilbert space and let $H$ be the Hamiltonian ([[stat-mech-quantum/quantum-hamiltonian|quantum Hamiltonian]]), a self-adjoint operator on $\mathcal H$.

For inverse temperature $\beta>0$ ([[thermodynamics/inverse-temperature-beta|inverse temperature β]]), the **quantum (canonical) partition function** is
$$
Z(\beta)\;=\;\operatorname{Tr}\!\big(e^{-\beta H}\big),
$$

where $\operatorname{Tr}$ is the operator trace ([[quantum-foundations/trace-operator|trace]]).

If $H$ has eigenvalues $\{E_n\}$ (counting multiplicity), then
$$
Z(\beta)\;=\;\sum_n e^{-\beta E_n}.
$$

The partition function normalizes the [[stat-mech-quantum/gibbs-state-quantum|quantum Gibbs state]] via $\rho_\beta = e^{-\beta H}/Z(\beta)$.

## Physical interpretation

$Z(\beta)$ is the **normalization constant** that makes thermal probabilities sum to one, and it is the generator of equilibrium thermodynamics for the canonical ensemble. It is the quantum analog of the classical [[stat-mech/partition-function-canonical|canonical partition function]].

Through $Z(\beta)$ one obtains the equilibrium Helmholtz free energy ([[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]), internal energy, entropy, and response coefficients.

## Key properties

1. **Positivity and finiteness (finite systems).**
   In finite dimension, $e^{-\beta H}$ is positive and trace-class automatically, so $Z(\beta)\in(0,\infty)$ for every $\beta>0$.

2. **Energy-shift covariance.**
   If $H' = H + cI$ for a scalar $c$, then
   $$
   Z_{H'}(\beta)\;=\;e^{-\beta c} Z_H(\beta).
   $$

   Consequently, the Gibbs state itself is invariant under adding a constant to energy (since the factor cancels in $\rho_\beta$).

3. **Free energy from $\log Z$.**
   The equilibrium free energy is
   $$
   F(\beta)\;=\;-\beta^{-1}\log Z(\beta),
   $$
   matching [[stat-mech/free-energy-statistical|statistical free energy]].

4. **Thermodynamic derivatives (finite-dimensional identities).**
   Define the equilibrium mean energy
   $$
   U(\beta)\;=\;\operatorname{Tr}(\rho_\beta H),
   \qquad \rho_\beta=\frac{e^{-\beta H}}{Z(\beta)}.
   $$
   Then
   $$
   U(\beta)\;=\;-\frac{d}{d\beta}\log Z(\beta).
   $$

   More generally, if $H(\lambda)=H_0+\lambda V$, then
   $$
   \frac{\partial}{\partial\lambda}\log Z(\beta,\lambda)\;=\;-\beta\,\langle V\rangle_{\beta,\lambda},
   $$

   where the expectation is the [[stat-mech-quantum/quantum-expectation-value|quantum expectation value]] in the Gibbs state for $H(\lambda)$.

5. **Factorization for independent subsystems.**
   If $\mathcal H=\mathcal H_A\otimes\mathcal H_B$ and
   $$
   H \;=\; H_A\otimes I_B \;+\; I_A\otimes H_B,
   $$
   then
   $$
   Z(\beta)\;=\;Z_A(\beta)\,Z_B(\beta).
   $$
   This is the canonical statement that noninteracting systems have additive free energy.

6. **Convexity and stability.**
   The map $\beta\mapsto \log Z(\beta)$ is convex. Equivalently, $U(\beta)$ is decreasing in $\beta$ and the heat capacity is nonnegative in the canonical ensemble (in finite dimension).

7. **Noncommuting Hamiltonian bounds.**
   When splitting a Hamiltonian into noncommuting parts, trace inequalities such as the [[quantum-foundations/golden-thompson-inequality|Golden–Thompson inequality]] yield useful estimates of $Z(\beta)$ and hence of $F(\beta)$.
