---
title: "Variational principle for lattice pressure"
description: "The lattice pressure equals a supremum of specific entropy minus energy density over translation-invariant states, and the maximizers are Gibbs measures."
---

## Statement

Let $\Phi$ be a translation-invariant, uniformly absolutely summable interaction on $\mathbb{Z}^d$ with finite spin space $S$, and let
$p(\Phi)$ denote the {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="lattice pressure" >}}, defined via the thermodynamic limit of the {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="lattice partition function" >}} (e.g. along a van Hove sequence).

Then the pressure satisfies the variational formula
$$
p(\Phi)
={}
\sup_{\mu\in\mathcal{P}_{\mathrm{t.i.}}(\Omega)}
\Big\{\, s(\mu) - e_\Phi(\mu)\,\Big\},
$$
where:

- $\mathcal{P}_{\mathrm{t.i.}}(\Omega)$ is the set of translation-invariant {{< knowl id="probability-measure" section="probability" text="probability measures" >}} on $\Omega=S^{\mathbb{Z}^d}$,
- $s(\mu)$ is the **specific entropy** (entropy per site; a mean version of {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}),
- $e_\Phi(\mu)$ is the **specific energy** (energy per site) computed from the {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="interaction energy" >}}.

Furthermore, $\mu$ achieves the supremum if and only if $\mu$ is a translation-invariant {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}} for $\Phi$ (equivalently, $\mu$ satisfies the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}} and is translation-invariant).

This is the lattice analogue of the {{< knowl id="gibbs-variational-principle" section="stat-mech" text="Gibbs variational principle" >}}.

## Key hypotheses

- **Interaction:** $\Phi$ is translation-invariant and uniformly absolutely summable (finite range is enough).
- **Spin space:** $S$ is finite (extensions exist under compactness/regularity assumptions).
- **Thermodynamic limit:** the pressure $p(\Phi)$ exists as the van Hove limit of $(1/|\Lambda|)\log Z_\Lambda$.

## Key conclusions

- **Pressure as an optimization problem:** $p(\Phi)$ is the supremum of (entropy density) minus (energy density) over translation-invariant states.
- **Characterization of equilibrium states:** the maximizers are precisely the translation-invariant Gibbs (DLR) states.
- **Convex-analytic viewpoint:** $p(\Phi)$ functions as a “log-partition” density; the variational formula is a Fenchel–Legendre-type duality with entropy (compare {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} and {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}}).

