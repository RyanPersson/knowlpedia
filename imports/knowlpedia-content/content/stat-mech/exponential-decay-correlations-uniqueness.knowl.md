+++
id = "stat-mech/exponential-decay-correlations-uniqueness"
title = "Exponential decay of correlations in the uniqueness regime"
kind = "knowl"
summary = "Under a Dobrushin-type contraction condition, the unique Gibbs state has exponentially decaying covariances for local observables."
aliases = ["exponential-decay-correlations-uniqueness", "Exponential decay of correlations in the uniqueness regime"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/exponential-decay-correlations-uniqueness.md"
+++

## Statement

Assume the hypotheses of the [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness theorem]] for a [[stat-mech-lattice/gibbs-specification|Gibbs specification]] $\gamma$ on $\Omega=S^{\mathbb{Z}^d}$, and let $\mu$ be the (unique) [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] satisfying the [[stat-mech-lattice/dlr-equation|DLR equation]].

Then there exist constants $C<\infty$ and $c>0$ (depending on the Dobrushin matrix $(C_{ij})$) such that for any bounded local functions $f,g:\Omega\to\mathbb{R}$ with supports contained in finite sets $A,B\Subset\mathbb{Z}^d$,
$$
\big|\mathrm{Cov}_\mu(f,g)\big|
\le
C\,\|f\|_\infty\,\|g\|_\infty\,
e^{-c\,\mathrm{dist}(A,B)}.
$$

In particular, for single-site observables (e.g. spins), the [[stat-mech/correlation-function-two-point|two-point correlation function]] decays exponentially in the distance between the sites.

## Key hypotheses

- **Uniqueness criterion:** the Dobrushin constant $\alpha<1$ as in [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness]].
- **Local observables:** $f$ and $g$ depend only on finitely many coordinates.
- **Covariance:** $\mathrm{Cov}_\mu(f,g)=\mathbb{E}_\mu[fg]-\mathbb{E}_\mu[f]\mathbb{E}_\mu[g]$, with expectations taken in the sense of [[probability/expectation|expectation]].

## Key conclusions

- **Exponential mixing:** correlations between spatially separated regions decay exponentially with separation.
- **Stability under boundary conditions:** local expectations are exponentially insensitive to far-away boundary perturbations (a strong form of uniqueness).
- **No phase coexistence in this regime:** exponential decay is incompatible with symmetry-breaking coexistence typical of [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].

## significance

Dobrushin’s comparison method bounds how changing a boundary condition at site $j$ influences the conditional distribution at site $i$, and then propagates this bound along paths in the lattice via the interdependence matrix $(C_{ij})$. When $\alpha<1$, influences contract and admit an expansion whose coefficients decay exponentially in graph distance. Converting “influence decay” into a covariance estimate yields the stated exponential bound.

This result formalizes the heuristic that in the high-temperature (unique-phase) regime, distant regions are nearly independent.
