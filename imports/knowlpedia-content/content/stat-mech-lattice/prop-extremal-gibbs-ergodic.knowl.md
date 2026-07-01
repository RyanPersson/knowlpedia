+++
id = "stat-mech-lattice/prop-extremal-gibbs-ergodic"
title = "Extremal Gibbs measures are ergodic (pure phases)"
kind = "knowl"
summary = "Extremality in the convex set of Gibbs measures is equivalent to trivial tail σ-algebra; with translation invariance, this implies translation ergodicity."
aliases = ["prop-extremal-gibbs-ergodic", "Extremal Gibbs measures are ergodic (pure phases)"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/prop-extremal-gibbs-ergodic.md"
+++

Fix a lattice interaction/specification and let $\mathcal{G}$ denote the convex set of all [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] consistent with it.

Let $\mathcal{T}$ be the tail $\sigma$-algebra,
$$
\mathcal{T}=\bigcap_{\Lambda\Subset\mathbb{Z}^d}\mathcal{F}_{\Lambda^c},
$$
i.e. events that depend only on spins “arbitrarily far away”.

## Statement
For $\mu\in\mathcal{G}$, the following are equivalent:

1. $\mu$ is [[stat-mech-lattice/extremal-gibbs-measure|extremal]] in $\mathcal{G}$ (it cannot be written as a nontrivial convex combination of two distinct measures in $\mathcal{G}$).

2. The tail $\sigma$-algebra is $\mu$-trivial: for every $A\in\mathcal{T}$, one has $\mu(A)\in\{0,1\}$.

If, in addition, the interaction/specification is translation-covariant and $\mu$ is translation invariant, then these conditions imply (and in common settings are equivalent to) translation ergodicity: every translation-invariant event has probability $0$ or $1$ under $\mu$.

## Key hypotheses
- $\mathcal{G}$ is the convex set of all DLR-consistent [[stat-mech-lattice/infinite-volume-gibbs-measure|Gibbs measures]] for a fixed specification.
- (For the translation-ergodic refinement) translation covariance of the specification and translation invariance of $\mu$.

## Conclusions
- Extremal Gibbs measures are “pure phases”: they have no nontrivial decomposition into distinct Gibbs components.
- Tail-triviality provides a practical criterion for purity, often used in phase-transition analysis (compare [[stat-mech-lattice/phase-transition-gibbs|phase transition]] and coexistence phenomena).
