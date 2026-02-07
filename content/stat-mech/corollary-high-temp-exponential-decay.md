---
title: "High-temperature exponential decay of correlations"
description: "In a uniqueness/high-temperature regime for finite-range lattice systems, connected correlations of local observables decay exponentially with distance."
---

## Statement (exponential clustering in the uniqueness region)
Let $\mu$ be the unique {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}} of a finite-range lattice system in a high-temperature/uniqueness regime (e.g. satisfying the {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness condition" >}}).

Then there exist constants $C<\infty$ and $m>0$ such that for any two bounded local observables $F,G$ with finite supports $\mathrm{supp}(F)$ and $\mathrm{supp}(G)$,
$$
\bigl|\operatorname{Cov}_\mu(F,G)\bigr|
\;\le\;
C\, e^{-m\,\mathrm{dist}(\mathrm{supp}(F),\mathrm{supp}(G))}\,\|F\|_\infty\,\|G\|_\infty,
$$

where $\operatorname{Cov}_\mu(F,G)=\mu(FG)-\mu(F)\mu(G)$.

In particular, the {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point function" >}} (and connected two-point function) decays exponentially with separation.

## Key hypotheses
- Finite-range (or sufficiently fast decaying) interaction on $\mathbb{Z}^d$.
- A parameter regime ensuring uniqueness and contractivity/mixing, e.g. {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness" >}} or {{< knowl id="cluster-expansion-convergence" text="cluster expansion convergence" >}}.
- Observables are local (depend on finitely many sites).

## Conclusions
- The system has a finite correlation length $\xi = 1/m$ (up to constants).
- No long-range order compatible with persistent connected correlations can occur within this regime.
- Together with uniqueness, this supports analyticity of thermodynamic functions (see {{< knowl id="corollary-uniqueness-analyticity" text="uniqueness implies analyticity" >}}).

## Cross-links (definitions and supporting results)
- {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}
- {{< knowl id="prop-connected-correlations-derivatives" text="connected correlations as derivatives" >}}
- {{< knowl id="exponential-decay-correlations-uniqueness" text="exponential decay from uniqueness theorem" >}}
- {{< knowl id="dobrushin-uniqueness-theorem" text="Dobrushin uniqueness theorem" >}}

