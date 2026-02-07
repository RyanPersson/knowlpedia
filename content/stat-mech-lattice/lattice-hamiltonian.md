---
title: "Lattice Hamiltonian"
description: "The finite-volume energy function on lattice spin configurations induced by an interaction potential (and possibly an external field and boundary condition)."
---

Fix a {{< knowl id="spin-space" text="spin space" >}} $S$ and a finite region $\Lambda$ of the lattice (see {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite box" >}} in {{< knowl id="lattice-zd" section="discrete-structures" text="the integer lattice" >}}). A **lattice Hamiltonian in volume** $\Lambda$ is an energy function that assigns a real number (or $+\infty$ in hard-constraint models) to each {{< knowl id="spin-configuration" text="spin configuration" >}} $\sigma_\Lambda \in S^\Lambda$, typically depending also on an exterior configuration (a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}}) $\eta_{\Lambda^c}$.

Given an {{< knowl id="interaction-potential-phi" text="interaction potential" >}} $\Phi = (\Phi_X)$, the standard finite-volume Hamiltonian with boundary condition $\eta$ is
$$
H_\Lambda^\Phi(\sigma_\Lambda \mid \eta)
:= \sum_{\substack{X \subset \mathbb{Z}^d \\ X \cap \Lambda \neq \emptyset}} \Phi_X(\sigma_\Lambda \eta_{\Lambda^c}),
$$

where each $\Phi_X$ depends only on the spins in $X$.

An **external field** is usually incorporated via single-site terms (see {{< knowl id="external-field-coupling" text="external field coupling" >}}), e.g. by including appropriate $\Phi_{\{i\}}$.

## Key properties
- **Locality:** If $\Phi$ has finite range (see {{< knowl id="finite-range-interaction-lattice" text="finite-range interaction" >}}), then changing $\sigma$ far from $\Lambda$ (in the boundary condition) does not affect $H_\Lambda^\Phi$ except near the boundary.
- **Additivity over interaction sets:** The Hamiltonian is a sum of local contributions. For nearest-neighbor models (see {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor structure" >}}), the sum reduces to edges and sites.
- **Translation invariance:** If $\Phi$ is translation invariant (see {{< knowl id="translation-invariant-interaction" text="translation-invariant interaction" >}}), then $H_\Lambda^\Phi$ is covariant under lattice shifts (up to boundary effects).
- **Boundary dependence:** Different boundary conditions $\eta$ encode different ways the exterior influences $\Lambda$. This dependence is essential in the study of {{< knowl id="phase-transition-gibbs" text="phase transitions" >}} and in defining {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} via the {{< knowl id="dlr-equation" text="DLR equation" >}}.
- **Connection to Gibbs weights:** The Hamiltonian generates Boltzmann weights $\exp(-\beta H_\Lambda^\Phi)$, where $\beta$ is the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}. These weights define the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} and the {{< knowl id="partition-function-lattice" text="lattice partition function" >}}.

## Physical interpretation
The lattice Hamiltonian encodes the **microscopic energetics**: which local patterns are energetically favored (low energy) or suppressed (high energy). Competing terms in $H_\Lambda$ (e.g. interaction vs field, ferro- vs antiferromagnetic couplings) determine typical configurations, the presence of order parameters (see {{< knowl id="order-parameter" text="order parameter" >}}), and whether multiple equilibrium phases can coexist (see {{< knowl id="pure-phase" text="pure phases" >}} and {{< knowl id="mixture-gibbs-measures" text="mixtures of Gibbs measures" >}}).
