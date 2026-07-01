+++
id = "stat-mech-lattice/infinite-volume-gibbs-measure"
title = "Infinite-volume Gibbs measure"
kind = "knowl"
summary = "A probability measure on lattice spin configurations whose finite-volume conditional distributions are given by a Gibbs specification (DLR consistency)."
aliases = ["infinite-volume-gibbs-measure", "Infinite-volume Gibbs measure"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/infinite-volume-gibbs-measure.md"
+++

Fix a lattice spin system with single-spin space given by the [[stat-mech-lattice/spin-space|spin space]] and configuration space $\Omega$ given by the [[stat-mech-lattice/configuration-space-lattice|lattice configuration space]] (elements are [[stat-mech-lattice/spin-configuration|spin configurations]]). Let $\gamma = (\gamma_\Lambda)_{\Lambda \Subset \mathbb{Z}^d}$ be the [[stat-mech-lattice/gibbs-specification|Gibbs specification]] associated with a chosen [[stat-mech-lattice/interaction-potential-phi|interaction potential]], [[stat-mech-lattice/lattice-hamiltonian|finite-volume Hamiltonians]], and (possibly) an [[stat-mech-lattice/external-field-coupling|external field]] at [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$.

An **infinite-volume Gibbs measure** for $\gamma$ is a [[probability/probability-measure|probability measure]] $\mu$ on $\Omega$ such that for every finite region $\Lambda$ and every bounded measurable function $f$ depending only on spins in $\Lambda$ (a *local observable*),
$$
\int f(\sigma)\,\mu(d\sigma)
={}
\int \left[\int f(\sigma_\Lambda \eta_{\Lambda^c})\,\gamma_\Lambda(d\sigma_\Lambda \mid \eta_{\Lambda^c})\right]\mu(d\eta).
$$

Equivalently, $\mu$ satisfies the [[stat-mech-lattice/dlr-equation|DLR equation]]: for each finite $\Lambda$, the conditional law of $\sigma_\Lambda$ given the outside configuration $\sigma_{\Lambda^c}$ is $\gamma_\Lambda(\cdot \mid \sigma_{\Lambda^c})$, where $\gamma_\Lambda$ is the same kernel that defines the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] with [[stat-mech-lattice/boundary-condition-lattice|boundary condition]] $\sigma_{\Lambda^c}$.

## Key properties

- **Local equilibrium / consistency:** The defining feature is *local*: every finite window sees the outside world only through the specification kernel. This is the infinite-system analogue of sampling from a finite-volume Gibbs law with an induced boundary condition.

- **Thermodynamic-limit realization:** For standard interactions (e.g. [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]]), infinite-volume Gibbs measures arise as subsequential limits of finite-volume Gibbs measures as the region grows (a form of [[thermodynamics/thermodynamic-limit|thermodynamic limit]]).

- **Convexity:** The set of all infinite-volume Gibbs measures for a fixed specification is convex: mixtures of solutions are still solutions (see [[stat-mech-lattice/mixture-gibbs-measures|mixtures of Gibbs measures]]).

- **Uniqueness vs multiplicity:** If there is exactly one infinite-volume Gibbs measure at given parameters, boundary conditions do not affect infinite-volume local statistics. Multiple distinct Gibbs measures indicate a [[stat-mech-lattice/phase-transition-gibbs|Gibbs phase transition]].

- **Symmetries:** If the interaction is [[stat-mech-lattice/translation-invariant-interaction|translation-invariant]] (and similarly for other symmetries), then there exist Gibbs measures that inherit these symmetries, though symmetry-invariant measures need not be [[stat-mech-lattice/extremal-gibbs-measure|extremal]].

## Physical interpretation

An infinite-volume Gibbs measure represents an equilibrium state of an *infinite* lattice system: any finite subsystem is in thermal equilibrium with the remainder of the lattice acting as a “heat bath,” encoded by the specification. Measurable predictions (magnetization, energy density, etc.) are computed as [[stat-mech/ensemble-average|ensemble averages]] under $\mu$, and the presence of multiple such measures corresponds to the coexistence of distinct macroscopic phases.
