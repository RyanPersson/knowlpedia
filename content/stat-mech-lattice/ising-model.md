---
title: "Ising model"
description: "A lattice spin model with binary spins (±1) and nearest-neighbor pair interactions, used as a paradigmatic model for phase transitions and symmetry breaking."
---

The (nearest-neighbor) **Ising model** on $\mathbb{Z}^d$ has:
- {{< knowl id="spin-space" text="spin space" >}} $\{-1,+1\}$,
- {{< knowl id="spin-configuration" text="configurations" >}} $\sigma=(\sigma_x)_{x\in\mathbb{Z}^d}$ with $\sigma_x\in\{-1,+1\}$,
- nearest-neighbor edges given by {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest neighbors" >}}.

For a finite region $\Lambda$ (see {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite boxes" >}}) and boundary condition $\eta$, the standard finite-volume {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}} is
$$
H_{\Lambda}^{\eta}(\sigma)\;=\;-J\sum_{\substack{\{x,y\}\\ x\sim y\\ \{x,y\}\cap \Lambda\neq \emptyset}}\sigma_x\sigma_y\;-\;h\sum_{x\in\Lambda}\sigma_x,
$$

where $J\in\mathbb{R}$ is the coupling and $h\in\mathbb{R}$ is the {{< knowl id="external-field-coupling" text="external field" >}}. The sum over edges crossing the boundary is interpreted using $\eta$ for spins outside $\Lambda$ (see {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}}).

The associated {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} at inverse temperature {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="$\\beta$" >}} is
$$
\mu_{\Lambda,\beta,h}^{\eta}(\sigma)\;=\;\frac{1}{Z_{\Lambda}(\beta,h,\eta)}\exp\!\big(-\beta H_{\Lambda}^{\eta}(\sigma)\big),
$$

with {{< knowl id="partition-function-lattice" text="partition function" >}} $Z_{\Lambda}(\beta,h,\eta)$.

## Key properties
- **Spin-flip symmetry:** At $h=0$ the Hamiltonian is invariant under $\sigma\mapsto -\sigma$, leading to a $\mathbb{Z}_2$ symmetry that may be broken via {{< knowl id="spontaneous-symmetry-breaking" text="SSB" >}}.
- **Interactions viewpoint:** The model is specified by a finite-range, translation-invariant {{< knowl id="interaction-potential-phi" text="interaction potential" >}} (pair interaction on nearest-neighbor edges), fitting the framework of {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}} and {{< knowl id="translation-invariant-interaction" text="translation invariance" >}}.
- **Thermodynamics:** The infinite-volume free energy density is encoded by the {{< knowl id="pressure-lattice" text="pressure" >}} as a {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}} of finite-volume pressures.
- **Correlations:** Spatial dependence of order is studied via {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}} and the {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}.
- **Phase transition behavior:** For $d\ge 2$ and ferromagnetic coupling ($J>0$), the model exhibits a low-temperature ordered regime with nonzero {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}} (details depend on $d$). For $d=1$ with finite-range interactions, there is no finite-temperature phase transition.

## Physical interpretation
Each spin represents a two-state degree of freedom (e.g. up/down magnetic moment). The pair term favors alignment if $J>0$ (ferromagnetism) or anti-alignment if $J<0$ (antiferromagnetism). Competition between energetic preference and thermal fluctuations produces sharp changes in macroscopic behavior, making the Ising model a central testbed for critical phenomena.
