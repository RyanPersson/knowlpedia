---
title: "Mixtures of Gibbs measures"
description: "Convex combinations (or integrals) of infinite-volume Gibbs measures; these remain Gibbs and encode phase coexistence or random phase selection."
---


Let $\gamma$ be a {{< knowl id="gibbs-specification" text="Gibbs specification" >}} and let $\mu_1,\mu_2 \in \mathcal{G}(\gamma)$ be {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}}.

A **mixture** of Gibbs measures is any convex combination
$$
\mu = a\,\mu_1 + (1-a)\,\mu_2,
\qquad 0\le a \le 1,
$$
or more generally an integral (barycenter) over Gibbs measures:
$$
\mu = \int \nu \,\rho(d\nu),
$$

where $\rho$ is a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} on the space of Gibbs measures.

Because the {{< knowl id="dlr-equation" text="DLR consistency" >}} is linear in $\mu$, any such mixture is again a Gibbs measure in $\mathcal{G}(\gamma)$.

## Key properties

- **Convexity of the Gibbs set:** The set $\mathcal{G}(\gamma)$ is convex, so mixing preserves the Gibbs property.

- **Extremal decomposition:** Any Gibbs measure can be decomposed into {{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}} (the extreme points of $\mathcal{G}(\gamma)$). In this sense, mixtures are the generic non-extremal equilibrium states.

- **Nontrivial tail behavior:** Mixtures typically have a nontrivial tail σ-algebra: there can be tail events with probabilities strictly between $0$ and $1$, reflecting the random choice among phases “at infinity.”

- **Symmetry-invariant but non-extremal states:** In symmetric models, there are translation-invariant Gibbs measures that are mixtures of symmetry-broken pure states (see {{< knowl id="pure-phase" text="pure phase" >}}). These measures can be invariant under a symmetry even when no extremal Gibbs measure has that symmetry.

## Physical interpretation

A mixture Gibbs measure describes an ensemble that *randomly selects* among competing equilibrium phases. For example, in a low-temperature ferromagnet, a symmetry-preserving infinite-volume state can arise as a 50–50 mixture of the two magnetized phases. Such a mixture is a valid equilibrium state mathematically, but it represents phase coexistence (or uncertainty about which pure phase is realized) rather than a single homogeneous macroscopic phase in a typical large sample.
