---
title: "Translation-invariant interaction"
description: "An interaction potential on a lattice whose local energy functions are unchanged under lattice translations."
---

Let $\Phi=\{\Phi_A\}_{A \Subset \mathbb{Z}^d}$ be an interaction (see {{< knowl id="interaction-potential-phi" text="interaction potential $\Phi$" >}}). For a lattice translation by $x\in\mathbb{Z}^d$, define $A+x=\{a+x:a\in A\}$. The interaction is **translation-invariant** if for every finite $A$ and every $x$,
$$
\Phi_{A+x}(\sigma_{A+x})=\Phi_A(\tau_x\sigma_A),
$$

where $(\tau_x\sigma)_y=\sigma_{y-x}$ denotes the translated configuration restricted to the appropriate set (see {{< knowl id="spin-configuration" text="spin configuration" >}}).

Informally: the rule assigning interaction energies depends only on relative positions, not on absolute location in $\mathbb{Z}^d$.

## Cross-links
- Often imposed together with {{< knowl id="finite-range-interaction-lattice" text="finite-range interactions" >}}.
- Under translation invariance, one typically studies translation-invariant states among {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} and their {{< knowl id="extremal-gibbs-measure" text="extremal components" >}}.
- Translation-invariant interactions are central to defining the lattice {{< knowl id="pressure-lattice" text="pressure" >}} and its {{< knowl id="thermodynamic-limit-pressure-lattice" text="thermodynamic limit" >}}.

## Key properties
1. **Homogeneity.** Local energetics are the same everywhere; bulk observables (e.g. average energy density) are spatially uniform in translation-invariant Gibbs states.
2. **Simplified parameterization.** Many models are specified by finitely many coupling constants (e.g. nearest-neighbor coupling $J$), because all translated copies share the same functional form.
3. **Shift-covariant specifications.** The associated {{< knowl id="gibbs-specification" text="Gibbs specification" >}} commutes with lattice shifts in the sense that translating both the region and the boundary condition translates the conditional distribution.
4. **Connection to phases.** Even when the interaction is translation-invariant, multiple translation-invariant infinite-volume Gibbs measures may exist; this is a hallmark of {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}.

## Physical interpretation
Translation invariance encodes a uniform medium: there are no impurities, boundaries, or spatially varying couplings in the bulk. When translation symmetry is present in the microscopic interaction but absent in a macroscopic state, that indicates {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} (for instance, coexistence of distinct ordered states).
