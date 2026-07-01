+++
id = "stat-mech-lattice/ferromagnetic-ising"
title = "Ferromagnetic Ising model"
kind = "knowl"
summary = "The Ising model with nonnegative couplings favoring alignment, featuring monotonicity and correlation inequalities and (in d≥2) an ordered low-temperature phase."
aliases = ["ferromagnetic-ising", "Ferromagnetic Ising model"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/ferromagnetic-ising.md"
+++

The **ferromagnetic Ising model** is the [[stat-mech-lattice/ising-model|Ising model]] with coupling $J>0$ (more generally, nonnegative couplings on edges), so that aligned neighboring spins lower the energy. In the nearest-neighbor translation-invariant case on $\mathbb{Z}^d$, the Hamiltonian in a finite region $\Lambda$ has the form
$$
H_{\Lambda}^{\eta}(\sigma)\;=\;-J\sum_{\substack{\{x,y\}\\ x\sim y\\ \{x,y\}\cap \Lambda\neq \emptyset}}\sigma_x\sigma_y\;-\;h\sum_{x\in\Lambda}\sigma_x,
$$

with $J>0$ and field $h$ (see [[stat-mech-lattice/external-field-coupling|external field coupling]]).

## Key properties
- **Attractiveness/monotonicity:** For ferromagnetic couplings, expectations of increasing observables are monotone in boundary conditions and in the field $h$ (compare $+$ and $-$ [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]]).
- **Extremal plus/minus states:** At $h=0$, the thermodynamic limits with $+$ and $-$ boundary conditions yield distinguished [[stat-mech-lattice/extremal-gibbs-measure|extremal Gibbs measures]] $\mu_{\beta,0}^+$ and $\mu_{\beta,0}^-$ (when non-uniqueness occurs), and any other translation-invariant Gibbs state is often a [[stat-mech-lattice/mixture-gibbs-measures|mixture]] of these two.
- **Spontaneous symmetry breaking:** In dimensions $d\ge 2$, sufficiently large $\beta$ yields [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]] at $h=0$, witnessed by nonzero [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]].
- **Correlation inequalities:** Ferromagnetism implies strong positivity properties for correlations (e.g. nonnegative connected correlations for increasing observables), which underpin existence/uniqueness results and bounds on critical behavior.
- **No frustration:** Because couplings favor simultaneous satisfaction of local alignment constraints, the model lacks the geometric frustration typical of competing-sign interactions.

## Physical interpretation
The ferromagnetic interaction encourages large domains of aligned spins. At high temperature (small $\beta$), thermal fluctuations break up domains and magnetization averages to zero. At low temperature (large $\beta$), the alignment tendency dominates, producing macroscopic ordering: the system settles into one of two symmetry-related magnetized phases, and an infinitesimal field can select which one.
