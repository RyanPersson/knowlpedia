+++
id = "stat-mech-lattice/ising-model"
title = "Ising model"
kind = "knowl"
summary = "A lattice spin model with binary spins (±1) and nearest-neighbor pair interactions, used as a paradigmatic model for phase transitions and symmetry breaking."
aliases = ["ising-model", "Ising model"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/ising-model.md"
+++

The (nearest-neighbor) **Ising model** on $\mathbb{Z}^d$ has:
- [[stat-mech-lattice/spin-space|spin space]] $\{-1,+1\}$,
- [[stat-mech-lattice/spin-configuration|configurations]] $\sigma=(\sigma_x)_{x\in\mathbb{Z}^d}$ with $\sigma_x\in\{-1,+1\}$,
- nearest-neighbor edges given by [[discrete-structures/nearest-neighbor-zd|nearest neighbors]].

For a finite region $\Lambda$ (see [[discrete-structures/finite-box-lattice|finite boxes]]) and boundary condition $\eta$, the standard finite-volume [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]] is
$$
H_{\Lambda}^{\eta}(\sigma)\;=\;-J\sum_{\substack{\{x,y\}\\ x\sim y\\ \{x,y\}\cap \Lambda\neq \emptyset}}\sigma_x\sigma_y\;-\;h\sum_{x\in\Lambda}\sigma_x,
$$

where $J\in\mathbb{R}$ is the coupling and $h\in\mathbb{R}$ is the [[stat-mech-lattice/external-field-coupling|external field]]. The sum over edges crossing the boundary is interpreted using $\eta$ for spins outside $\Lambda$ (see [[stat-mech-lattice/boundary-condition-lattice|boundary conditions]]).

The associated [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] at inverse temperature [[thermodynamics/inverse-temperature-beta|$\\beta$]] is
$$
\mu_{\Lambda,\beta,h}^{\eta}(\sigma)\;=\;\frac{1}{Z_{\Lambda}(\beta,h,\eta)}\exp\!\big(-\beta H_{\Lambda}^{\eta}(\sigma)\big),
$$

with [[stat-mech-lattice/partition-function-lattice|partition function]] $Z_{\Lambda}(\beta,h,\eta)$.

## Key properties
- **Spin-flip symmetry:** At $h=0$ the Hamiltonian is invariant under $\sigma\mapsto -\sigma$, leading to a $\mathbb{Z}_2$ symmetry that may be broken via [[stat-mech-lattice/spontaneous-symmetry-breaking|SSB]].
- **Interactions viewpoint:** The model is specified by a finite-range, translation-invariant [[stat-mech-lattice/interaction-potential-phi|interaction potential]] (pair interaction on nearest-neighbor edges), fitting the framework of [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]] and [[stat-mech-lattice/translation-invariant-interaction|translation invariance]].
- **Thermodynamics:** The infinite-volume free energy density is encoded by the [[stat-mech-lattice/pressure-lattice|pressure]] as a [[stat-mech-lattice/thermodynamic-limit-pressure-lattice|thermodynamic limit]] of finite-volume pressures.
- **Correlations:** Spatial dependence of order is studied via [[stat-mech/correlation-function-two-point|two-point correlations]] and the [[stat-mech/correlation-length|correlation length]].
- **Phase transition behavior:** For $d\ge 2$ and ferromagnetic coupling ($J>0$), the model exhibits a low-temperature ordered regime with nonzero [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] (details depend on $d$). For $d=1$ with finite-range interactions, there is no finite-temperature phase transition.

## Physical interpretation
Each spin represents a two-state degree of freedom (e.g. up/down magnetic moment). The pair term favors alignment if $J>0$ (ferromagnetism) or anti-alignment if $J<0$ (antiferromagnetism). Competition between energetic preference and thermal fluctuations produces sharp changes in macroscopic behavior, making the Ising model a central testbed for critical phenomena.
