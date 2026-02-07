---
title: "Ferromagnetic Ising model"
description: "The Ising model with nonnegative couplings favoring alignment, featuring monotonicity and correlation inequalities and (in d≥2) an ordered low-temperature phase."
---

The **ferromagnetic Ising model** is the {{< knowl id="ising-model" text="Ising model" >}} with coupling $J>0$ (more generally, nonnegative couplings on edges), so that aligned neighboring spins lower the energy. In the nearest-neighbor translation-invariant case on $\mathbb{Z}^d$, the Hamiltonian in a finite region $\Lambda$ has the form
$$
H_{\Lambda}^{\eta}(\sigma)\;=\;-J\sum_{\substack{\{x,y\}\\ x\sim y\\ \{x,y\}\cap \Lambda\neq \emptyset}}\sigma_x\sigma_y\;-\;h\sum_{x\in\Lambda}\sigma_x,
$$

with $J>0$ and field $h$ (see {{< knowl id="external-field-coupling" text="external field coupling" >}}).

## Key properties
- **Attractiveness/monotonicity:** For ferromagnetic couplings, expectations of increasing observables are monotone in boundary conditions and in the field $h$ (compare $+$ and $-$ {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}}).
- **Extremal plus/minus states:** At $h=0$, the thermodynamic limits with $+$ and $-$ boundary conditions yield distinguished {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}} $\mu_{\beta,0}^+$ and $\mu_{\beta,0}^-$ (when non-uniqueness occurs), and any other translation-invariant Gibbs state is often a {{< knowl id="mixture-gibbs-measures" text="mixture" >}} of these two.
- **Spontaneous symmetry breaking:** In dimensions $d\ge 2$, sufficiently large $\beta$ yields {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} at $h=0$, witnessed by nonzero {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}}.
- **Correlation inequalities:** Ferromagnetism implies strong positivity properties for correlations (e.g. nonnegative connected correlations for increasing observables), which underpin existence/uniqueness results and bounds on critical behavior.
- **No frustration:** Because couplings favor simultaneous satisfaction of local alignment constraints, the model lacks the geometric frustration typical of competing-sign interactions.

## Physical interpretation
The ferromagnetic interaction encourages large domains of aligned spins. At high temperature (small $\beta$), thermal fluctuations break up domains and magnetization averages to zero. At low temperature (large $\beta$), the alignment tendency dominates, producing macroscopic ordering: the system settles into one of two symmetry-related magnetized phases, and an infinitesimal field can select which one.
