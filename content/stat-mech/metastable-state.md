---
title: "Metastable state"
description: "A long-lived, locally stable state (often corresponding to a local minimum of a thermodynamic potential) that eventually decays to the globally stable equilibrium via rare fluctuations."
---

A **metastable state** is a state that is *locally stable* under small perturbations but is not the globally stable equilibrium at the same control parameters. In statistical mechanics, metastability typically appears near **first-order phase coexistence** and is tied to **free-energy barriers** and **nucleation**.

## Static characterization

Fix control parameters (e.g., inverse temperature $\beta$ and field $h$) and consider an order parameter (e.g., magnetization) $m$ as in {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}.

A metastable state is commonly modeled by a **local minimum** of an effective thermodynamic function of $m$, such as:
- a constrained free-energy density (canonical viewpoint; see {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}), or
- a large-deviation rate function for $m$ (see {{< knowl id="ldp-rate-function-magnetization" text="rate function for magnetization" >}}).

In a Landau description (see {{< knowl id="landau-free-energy-functional" text="Landau free-energy functional" >}}), metastability corresponds to **multiple local minima** of the Landau free energy; the globally stable phase is the *global* minimizer, while the metastable phase is a *local* minimizer separated by a barrier.

## Dynamical viewpoint and lifetime scale

When a microscopic dynamics is specified (e.g., Glauber-type dynamics for spins), a metastable state manifests as:
- rapid relaxation to a quasi-equilibrium within a basin of attraction, followed by
- a long waiting time before a rare transition to the stable phase.

Heuristically, the mean exit time from the metastable basin often has an Arrhenius-type form
$$
\mathbb{E}[\tau] \sim \exp(\beta \,\Delta F^\ddagger),
$$

where $\Delta F^\ddagger$ is an effective **free-energy barrier**.

## Nucleation barrier (classical droplet heuristic)

At a first-order transition, decay is often driven by nucleation of a droplet of the stable phase inside the metastable background. A standard heuristic for a droplet of linear size $R$ in $d$ dimensions is
$$
\Delta F(R) \approx \sigma\, S_d\, R^{d-1} \;-\; \Delta f\, V_d\, R^d,
$$
where:
- $\sigma$ is the **surface tension** (see {{< knowl id="surface-tension-interface" text="surface tension and interfaces" >}}),
- $\Delta f$ is the bulk free-energy density difference between the phases,
- $S_d$ and $V_d$ are geometric constants (surface area and volume of the unit ball).

The competition between the positive surface term and negative bulk term yields a critical droplet size $R_\star$ and a barrier height $\Delta F(R_\star)$ controlling the metastable lifetime.

## Where metastability lives in equilibrium theory

Metastable behavior is naturally discussed using finite- and infinite-volume Gibbs measures:
- In finite volume, the Gibbs measure (see {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}) may exhibit multiple “preferred” macrostates separated by exponentially small probabilities.
- In infinite volume (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}), the globally stable phases correspond to equilibrium Gibbs states; metastability is often encoded in how boundary conditions or fields select among competing phases (see {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions via Gibbs measures" >}}).

Metastability is closely tied to **thermodynamic stability** (local convexity/positivity conditions) but differs in that a metastable state can satisfy local stability conditions while failing global optimality; compare {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}.
