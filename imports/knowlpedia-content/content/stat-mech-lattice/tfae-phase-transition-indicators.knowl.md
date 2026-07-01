+++
id = "stat-mech-lattice/tfae-phase-transition-indicators"
title = "TFAE: Indicators of a Phase Transition"
kind = "knowl"
summary = "Equivalent criteria for phase coexistence and symmetry breaking: non-uniqueness of Gibbs measures, boundary-condition dependence, non-differentiability of pressure, and order parameters."
aliases = ["tfae-phase-transition-indicators", "TFAE: Indicators of a Phase Transition"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/tfae-phase-transition-indicators.md"
+++

Fix a lattice spin system with a symmetry-breaking order parameter (e.g. the [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising model]]) on $\mathbb{Z}^d$. Consider parameters such as inverse temperature $\beta$ and external field $h$, and focus on the symmetry point $h=0$. The following are equivalent ways to say that **a phase transition (symmetry breaking / phase coexistence) occurs at $(\beta,0)$**.

1. **Non-uniqueness of infinite-volume Gibbs measures.**
   There exist at least two distinct [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] at the same parameters $(\beta,0)$.

2. **Boundary-condition dependence of local expectations.**
   There exist two boundary conditions (e.g. plus and minus) and a local observable $f$ (for instance $f(\sigma)=\sigma_0$) such that the thermodynamic limits of finite-volume Gibbs states give different expectations:
   $$
   \lim_{\Lambda\uparrow\mathbb{Z}^d} \mathbb{E}_{\mu_\Lambda^{+}}[f]
   \ne
   \lim_{\Lambda\uparrow\mathbb{Z}^d} \mathbb{E}_{\mu_\Lambda^{-}}[f].
   $$
   This is a concrete operational form of item 1 using [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]].

3. **Nonzero spontaneous order parameter.**
   The [[stat-mech-lattice/order-parameter|order parameter]] (e.g. magnetization) is nonzero in an extremal phase:
   $$
   m^+(\beta) = \mathbb{E}_{\mu^{+}}[\sigma_0] > 0,
   $$

   with the symmetric counterpart $m^-(\beta)=-m^+(\beta)$.
   This is exactly [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] in the Ising setting.

4. **Non-differentiability of the pressure in the conjugate field.**
   Let $p(\beta,h)$ be the infinite-volume pressure (log-partition density; see [[stat-mech/pressure-log-partition-density|pressure (log-partition) density]]). Then the left and right derivatives in $h$ at $h=0$ differ:
   $$
   \frac{\partial p}{\partial h}(\beta,0^+) \ne \frac{\partial p}{\partial h}(\beta,0^-).
   $$

   Since $\partial p/\partial h$ equals the magnetization, this is equivalent to the existence of two phases with different order parameter values.

5. **Long-range order in two-point correlations (symmetry-broken phase).**
   The two-point function (see [[stat-mech/correlation-function-two-point|two-point correlation function]]) fails to decay to zero:
   $$
   \lim_{|x|\to\infty} \mathbb{E}_{\mu^{+}}[\sigma_0 \sigma_x] > 0.
   $$
   In ferromagnetic Ising systems this is equivalent to item 3 via standard correlation inequalities, and hence to item 1.

Notes on scope:
- Items 1–4 are the most robust equivalences for lattice systems: “phase transition” as non-uniqueness/coexistence of Gibbs states and the associated non-smoothness of thermodynamic potentials in conjugate variables.
- Divergence of a [[stat-mech/correlation-length|correlation length]] or power-law decay typically signals a *critical point* (continuous transition), but is not equivalent to coexistence in general (first-order transitions can have finite correlation length).

Prerequisites and context: [[stat-mech-lattice/phase-transition-gibbs|phase transitions via Gibbs measures]], [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]], [[stat-mech-lattice/order-parameter|order parameters]], [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]], [[stat-mech/pressure-log-partition-density|pressure (log-partition) density]].
