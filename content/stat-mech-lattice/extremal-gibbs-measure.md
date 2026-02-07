---
title: "Extremal Gibbs measure"
description: "An infinite-volume Gibbs measure that is an extreme point of the convex set of Gibbs measures (equivalently, tail-trivial)."
---


Fix a {{< knowl id="gibbs-specification" text="Gibbs specification" >}} $\gamma$ and let $\mathcal{G}(\gamma)$ denote the set of {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} consistent with $\gamma$.

A Gibbs measure $\mu \in \mathcal{G}(\gamma)$ is **extremal** if it cannot be written as a nontrivial convex combination of other Gibbs measures: whenever
$$
\mu = t\,\mu_1 + (1-t)\,\mu_2,
\qquad 0<t<1,
\qquad \mu_1,\mu_2 \in \mathcal{G}(\gamma),
$$

it follows that $\mu_1=\mu_2=\mu$.

A standard equivalent characterization is **tail triviality**: if $\mathcal{T}$ is the tail {{< knowl id="sigma-algebra" section="measure-theory" text="σ-algebra" >}} (events depending only on spins arbitrarily far away),
$$
\mathcal{T} = \bigcap_{\Lambda \Subset \mathbb{Z}^d} \mathcal{F}_{\Lambda^c},
$$

then $\mu(A)\in\{0,1\}$ for every $A\in\mathcal{T}$.

## Key properties

- **Pure-state building blocks:** Extremal Gibbs measures are the “indecomposable” equilibrium states. Every Gibbs measure can be represented as a {{< knowl id="mixture-gibbs-measures" text="mixture" >}} of extremal ones.

- **No hidden randomization at infinity:** Tail triviality means there is no residual macroscopic randomness left after conditioning on arbitrarily large scales. Intuitively, an extremal state does not randomly select among competing phases.

- **Ergodic behavior under symmetries (when applicable):** For {{< knowl id="translation-invariant-interaction" text="translation-invariant interactions" >}}, many physically relevant extremal Gibbs measures are translation-ergodic (though extremality is defined relative to the Gibbs set, not relative to translations).

- **Characterization of coexistence:** When multiple distinct extremal Gibbs measures exist at the same parameters, they correspond to distinct macroscopic phases (see {{< knowl id="phase-transition-gibbs" text="phase transition" >}} and {{< knowl id="pure-phase" text="pure phase" >}}).

## Physical interpretation

An extremal Gibbs measure corresponds to a single homogeneous equilibrium phase of an infinite system, with no macroscopic phase coexistence encoded by random mixing. In models with symmetry breaking (e.g. the {{< knowl id="ising-model" text="Ising model" >}} at low temperature), the “plus” and “minus” magnetized states are paradigmatic examples of distinct extremal Gibbs measures, while a symmetry-invariant state may be their non-extremal mixture.
