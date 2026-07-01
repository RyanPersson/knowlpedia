+++
id = "stat-mech-lattice/variational-principle-pressure-lattice"
title = "Variational principle for lattice pressure"
kind = "knowl"
summary = "The lattice pressure equals a supremum of specific entropy minus energy density over translation-invariant states, and the maximizers are Gibbs measures."
aliases = ["variational-principle-pressure-lattice", "Variational principle for lattice pressure"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/variational-principle-pressure-lattice.md"
+++

## Statement

Let $\Phi$ be a translation-invariant, uniformly absolutely summable interaction on $\mathbb{Z}^d$ with finite spin space $S$, and let
$p(\Phi)$ denote the [[stat-mech-lattice/pressure-lattice|lattice pressure]], defined via the thermodynamic limit of the [[stat-mech-lattice/partition-function-lattice|lattice partition function]] (e.g. along a van Hove sequence).

Then the pressure satisfies the variational formula
$$
p(\Phi)
={}
\sup_{\mu\in\mathcal{P}_{\mathrm{t.i.}}(\Omega)}
\Big\{\, s(\mu) - e_\Phi(\mu)\,\Big\},
$$
where:

- $\mathcal{P}_{\mathrm{t.i.}}(\Omega)$ is the set of translation-invariant [[probability/probability-measure|probability measures]] on $\Omega=S^{\mathbb{Z}^d}$,
- $s(\mu)$ is the **specific entropy** (entropy per site; a mean version of [[probability/shannon-entropy|Shannon entropy]]),
- $e_\Phi(\mu)$ is the **specific energy** (energy per site) computed from the [[stat-mech-lattice/lattice-hamiltonian|interaction energy]].

Furthermore, $\mu$ achieves the supremum if and only if $\mu$ is a translation-invariant [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] for $\Phi$ (equivalently, $\mu$ satisfies the [[stat-mech-lattice/dlr-equation|DLR equation]] and is translation-invariant).

This is the lattice analogue of the [[stat-mech/gibbs-variational-principle|Gibbs variational principle]].

## Key hypotheses

- **Interaction:** $\Phi$ is translation-invariant and uniformly absolutely summable (finite range is enough).
- **Spin space:** $S$ is finite (extensions exist under compactness/regularity assumptions).
- **Thermodynamic limit:** the pressure $p(\Phi)$ exists as the van Hove limit of $(1/|\Lambda|)\log Z_\Lambda$.

## Key conclusions

- **Pressure as an optimization problem:** $p(\Phi)$ is the supremum of (entropy density) minus (energy density) over translation-invariant states.
- **Characterization of equilibrium states:** the maximizers are precisely the translation-invariant Gibbs (DLR) states.
- **Convex-analytic viewpoint:** $p(\Phi)$ functions as a “log-partition” density; the variational formula is a Fenchel–Legendre-type duality with entropy (compare [[convex-analysis/legendre-transform|Legendre transform]] and [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]]).
