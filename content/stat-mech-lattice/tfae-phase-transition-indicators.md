---
title: "TFAE: Indicators of a Phase Transition"
description: "Equivalent criteria for phase coexistence and symmetry breaking: non-uniqueness of Gibbs measures, boundary-condition dependence, non-differentiability of pressure, and order parameters."
---

Fix a lattice spin system with a symmetry-breaking order parameter (e.g. the {{< knowl id="ferromagnetic-ising" section="stat-mech-lattice" text="ferromagnetic Ising model" >}}) on $\mathbb{Z}^d$. Consider parameters such as inverse temperature $\beta$ and external field $h$, and focus on the symmetry point $h=0$. The following are equivalent ways to say that **a phase transition (symmetry breaking / phase coexistence) occurs at $(\beta,0)$**.

1. **Non-uniqueness of infinite-volume Gibbs measures.**  
   There exist at least two distinct {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} at the same parameters $(\beta,0)$.

2. **Boundary-condition dependence of local expectations.**  
   There exist two boundary conditions (e.g. plus and minus) and a local observable $f$ (for instance $f(\sigma)=\sigma_0$) such that the thermodynamic limits of finite-volume Gibbs states give different expectations:
   $$
   \lim_{\Lambda\uparrow\mathbb{Z}^d} \mathbb{E}_{\mu_\Lambda^{+}}[f]
   \ne
   \lim_{\Lambda\uparrow\mathbb{Z}^d} \mathbb{E}_{\mu_\Lambda^{-}}[f].
   $$
   This is a concrete operational form of item 1 using {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}.

3. **Nonzero spontaneous order parameter.**  
   The {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}} (e.g. magnetization) is nonzero in an extremal phase:
   $$
   m^+(\beta) = \mathbb{E}_{\mu^{+}}[\sigma_0] > 0,
   $$

   with the symmetric counterpart $m^-(\beta)=-m^+(\beta)$.  
   This is exactly {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} in the Ising setting.

4. **Non-differentiability of the pressure in the conjugate field.**  
   Let $p(\beta,h)$ be the infinite-volume pressure (log-partition density; see {{< knowl id="pressure-log-partition-density" section="stat-mech" text="pressure (log-partition) density" >}}). Then the left and right derivatives in $h$ at $h=0$ differ:
   $$
   \frac{\partial p}{\partial h}(\beta,0^+) \ne \frac{\partial p}{\partial h}(\beta,0^-).
   $$

   Since $\partial p/\partial h$ equals the magnetization, this is equivalent to the existence of two phases with different order parameter values.

5. **Long-range order in two-point correlations (symmetry-broken phase).**  
   The two-point function (see {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}) fails to decay to zero:
   $$
   \lim_{|x|\to\infty} \mathbb{E}_{\mu^{+}}[\sigma_0 \sigma_x] > 0.
   $$
   In ferromagnetic Ising systems this is equivalent to item 3 via standard correlation inequalities, and hence to item 1.

Notes on scope:
- Items 1–4 are the most robust equivalences for lattice systems: “phase transition” as non-uniqueness/coexistence of Gibbs states and the associated non-smoothness of thermodynamic potentials in conjugate variables.
- Divergence of a {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} or power-law decay typically signals a *critical point* (continuous transition), but is not equivalent to coexistence in general (first-order transitions can have finite correlation length).

Prerequisites and context: {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions via Gibbs measures" >}}, {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}, {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameters" >}}, {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}}, {{< knowl id="pressure-log-partition-density" section="stat-mech" text="pressure (log-partition) density" >}}.
