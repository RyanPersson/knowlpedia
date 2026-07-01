+++
id = "stat-mech-lattice/translation-invariant-interaction"
title = "Translation-invariant interaction"
kind = "knowl"
summary = "An interaction potential on a lattice whose local energy functions are unchanged under lattice translations."
aliases = ["translation-invariant-interaction", "Translation-invariant interaction"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/translation-invariant-interaction.md"
+++

Let $\Phi=\{\Phi_A\}_{A \Subset \mathbb{Z}^d}$ be an interaction (see [[stat-mech-lattice/interaction-potential-phi|interaction potential $\Phi$]]). For a lattice translation by $x\in\mathbb{Z}^d$, define $A+x=\{a+x:a\in A\}$. The interaction is **translation-invariant** if for every finite $A$ and every $x$,
$$
\Phi_{A+x}(\sigma_{A+x})=\Phi_A(\tau_x\sigma_A),
$$

where $(\tau_x\sigma)_y=\sigma_{y-x}$ denotes the translated configuration restricted to the appropriate set (see [[stat-mech-lattice/spin-configuration|spin configuration]]).

Informally: the rule assigning interaction energies depends only on relative positions, not on absolute location in $\mathbb{Z}^d$.

## Cross-links
- Often imposed together with [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]].
- Under translation invariance, one typically studies translation-invariant states among [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] and their [[stat-mech-lattice/extremal-gibbs-measure|extremal components]].
- Translation-invariant interactions are central to defining the lattice [[stat-mech-lattice/pressure-lattice|pressure]] and its [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]].

## Key properties
1. **Homogeneity.** Local energetics are the same everywhere; bulk observables (e.g. average energy density) are spatially uniform in translation-invariant Gibbs states.
2. **Simplified parameterization.** Many models are specified by finitely many coupling constants (e.g. nearest-neighbor coupling $J$), because all translated copies share the same functional form.
3. **Shift-covariant specifications.** The associated [[stat-mech-lattice/gibbs-specification|Gibbs specification]] commutes with lattice shifts in the sense that translating both the region and the boundary condition translates the conditional distribution.
4. **Connection to phases.** Even when the interaction is translation-invariant, multiple translation-invariant infinite-volume Gibbs measures may exist; this is a hallmark of [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].

## Physical interpretation
Translation invariance encodes a uniform medium: there are no impurities, boundaries, or spatially varying couplings in the bulk. When translation symmetry is present in the microscopic interaction but absent in a macroscopic state, that indicates [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]] (for instance, coexistence of distinct ordered states).
