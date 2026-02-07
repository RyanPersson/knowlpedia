---
title: "Infinite-volume Gibbs measure"
description: "A probability measure on lattice spin configurations whose finite-volume conditional distributions are given by a Gibbs specification (DLR consistency)."
---


Fix a lattice spin system with single-spin space given by the {{< knowl id="spin-space" text="spin space" >}} and configuration space $\Omega$ given by the {{< knowl id="configuration-space-lattice" text="lattice configuration space" >}} (elements are {{< knowl id="spin-configuration" text="spin configurations" >}}). Let $\gamma = (\gamma_\Lambda)_{\Lambda \Subset \mathbb{Z}^d}$ be the {{< knowl id="gibbs-specification" text="Gibbs specification" >}} associated with a chosen {{< knowl id="interaction-potential-phi" text="interaction potential" >}}, {{< knowl id="lattice-hamiltonian" text="finite-volume Hamiltonians" >}}, and (possibly) an {{< knowl id="external-field-coupling" text="external field" >}} at {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta$.

An **infinite-volume Gibbs measure** for $\gamma$ is a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} $\mu$ on $\Omega$ such that for every finite region $\Lambda$ and every bounded measurable function $f$ depending only on spins in $\Lambda$ (a *local observable*),
$$
\int f(\sigma)\,\mu(d\sigma)
={}
\int \left[\int f(\sigma_\Lambda \eta_{\Lambda^c})\,\gamma_\Lambda(d\sigma_\Lambda \mid \eta_{\Lambda^c})\right]\mu(d\eta).
$$

Equivalently, $\mu$ satisfies the {{< knowl id="dlr-equation" text="DLR equation" >}}: for each finite $\Lambda$, the conditional law of $\sigma_\Lambda$ given the outside configuration $\sigma_{\Lambda^c}$ is $\gamma_\Lambda(\cdot \mid \sigma_{\Lambda^c})$, where $\gamma_\Lambda$ is the same kernel that defines the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} with {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} $\sigma_{\Lambda^c}$.

## Key properties

- **Local equilibrium / consistency:** The defining feature is *local*: every finite window sees the outside world only through the specification kernel. This is the infinite-system analogue of sampling from a finite-volume Gibbs law with an induced boundary condition.

- **Thermodynamic-limit realization:** For standard interactions (e.g. {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}}), infinite-volume Gibbs measures arise as subsequential limits of finite-volume Gibbs measures as the region grows (a form of {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}).

- **Convexity:** The set of all infinite-volume Gibbs measures for a fixed specification is convex: mixtures of solutions are still solutions (see {{< knowl id="mixture-gibbs-measures" text="mixtures of Gibbs measures" >}}).

- **Uniqueness vs multiplicity:** If there is exactly one infinite-volume Gibbs measure at given parameters, boundary conditions do not affect infinite-volume local statistics. Multiple distinct Gibbs measures indicate a {{< knowl id="phase-transition-gibbs" text="Gibbs phase transition" >}}.

- **Symmetries:** If the interaction is {{< knowl id="translation-invariant-interaction" text="translation-invariant" >}} (and similarly for other symmetries), then there exist Gibbs measures that inherit these symmetries, though symmetry-invariant measures need not be {{< knowl id="extremal-gibbs-measure" text="extremal" >}}.

## Physical interpretation

An infinite-volume Gibbs measure represents an equilibrium state of an *infinite* lattice system: any finite subsystem is in thermal equilibrium with the remainder of the lattice acting as a “heat bath,” encoded by the specification. Measurable predictions (magnetization, energy density, etc.) are computed as {{< knowl id="ensemble-average" section="stat-mech" text="ensemble averages" >}} under $\mu$, and the presence of multiple such measures corresponds to the coexistence of distinct macroscopic phases.
