+++
id = "stat-mech/corollary-high-temp-exponential-decay"
title = "High-temperature exponential decay of correlations"
kind = "knowl"
summary = "In a uniqueness/high-temperature regime for finite-range lattice systems, connected correlations of local observables decay exponentially with distance."
aliases = ["corollary-high-temp-exponential-decay", "High-temperature exponential decay of correlations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/corollary-high-temp-exponential-decay.md"
+++

## Statement (exponential clustering in the uniqueness region)
Let $\mu$ be the unique [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]] of a finite-range lattice system in a high-temperature/uniqueness regime (e.g. satisfying the [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness condition]]).

Then there exist constants $C<\infty$ and $m>0$ such that for any two bounded local observables $F,G$ with finite supports $\mathrm{supp}(F)$ and $\mathrm{supp}(G)$,
$$
\bigl|\operatorname{Cov}_\mu(F,G)\bigr|
\;\le\;
C\, e^{-m\,\mathrm{dist}(\mathrm{supp}(F),\mathrm{supp}(G))}\,\|F\|_\infty\,\|G\|_\infty,
$$

where $\operatorname{Cov}_\mu(F,G)=\mu(FG)-\mu(F)\mu(G)$.

In particular, the [[stat-mech/correlation-function-two-point|two-point function]] (and connected two-point function) decays exponentially with separation.

## Key hypotheses
- Finite-range (or sufficiently fast decaying) interaction on $\mathbb{Z}^d$.
- A parameter regime ensuring uniqueness and contractivity/mixing, e.g. [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness]] or [[stat-mech/cluster-expansion-convergence|cluster expansion convergence]].
- Observables are local (depend on finitely many sites).

## Conclusions
- The system has a finite correlation length $\xi = 1/m$ (up to constants).
- No long-range order compatible with persistent connected correlations can occur within this regime.
- Together with uniqueness, this supports analyticity of thermodynamic functions (see [[stat-mech/corollary-uniqueness-analyticity|uniqueness implies analyticity]]).

## Cross-links (definitions and supporting results)
- [[stat-mech/correlation-function-two-point|two-point correlation function]]
- [[stat-mech/prop-connected-correlations-derivatives|connected correlations as derivatives]]
- [[stat-mech/exponential-decay-correlations-uniqueness|exponential decay from uniqueness theorem]]
- [[stat-mech/dobrushin-uniqueness-theorem|Dobrushin uniqueness theorem]]
