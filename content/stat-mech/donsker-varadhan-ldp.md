---
title: "Donsker–Varadhan Large Deviation Principle"
description: "The Donsker–Varadhan LDP for the empirical measure of an ergodic Markov process, with the DV variational rate function and its reversible (Dirichlet form) specialization."
---

## Prerequisites

- {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle (LDP)" >}}
- {{< knowl id="rate-function" section="large-deviations" text="rate functions" >}}
- {{< knowl id="probability-measure" section="probability" text="probability measures" >}}
- {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}
- {{< knowl id="markov-chain-discrete" text="discrete-time Markov chains" >}}
- {{< knowl id="markov-semigroup-continuous" text="continuous-time Markov semigroups" >}}
- {{< knowl id="detailed-balance" text="detailed balance" >}}
- {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="convex conjugates (Fenchel duality)" >}}

## Empirical measure

Let $(X_t)_{t\ge 0}$ be an ergodic continuous-time Markov process on a state space $E$ with generator $L$ (see {{< knowl id="markov-semigroup-continuous" text="Markov semigroups" >}}) and invariant probability measure $\pi$.

The (time-averaged) empirical measure up to time $T$ is
$$
L_T = \frac{1}{T}\int_0^T \delta_{X_t}\,dt,
$$

a random element of the space of {{< knowl id="probability-measure" section="probability" text="probability measures" >}} on $E$.

(For a discrete-time chain $(X_n)_{n\ge0}$, one analogously uses $L_n=\frac1n\sum_{k=0}^{n-1}\delta_{X_k}$; see {{< knowl id="markov-chain-discrete" text="discrete Markov chains" >}}.)

## Theorem (Donsker–Varadhan LDP, empirical measure)

Under standard ergodicity and regularity assumptions ensuring a well-posed DV theory, the family $(L_T)_{T\to\infty}$ satisfies a {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}} with speed $T$ and a good {{< knowl id="rate-function" section="large-deviations" text="rate function" >}} $I(\mu)$ characterized by the variational formula
$$
I(\mu)
={}
\sup_{g>0}
\left\{
-\int_E \frac{Lg}{g}\,d\mu
\right\}
={}
-\inf_{g>0}\int_E \frac{Lg}{g}\,d\mu,
$$

where the supremum/infimum runs over strictly positive test functions $g$ in the domain of $L$.

Key structural properties:

- $I(\mu)\ge 0$ and $I(\mu)=0$ if and only if $\mu=\pi$ (the invariant law).
- $I$ is convex and lower semicontinuous, hence “good” on suitable state spaces.

## Reversible specialization (Dirichlet form representation)

If the process is reversible with respect to $\pi$ (see {{< knowl id="detailed-balance" text="detailed balance" >}}), and $\mu$ is absolutely continuous with respect to $\pi$ with density $f=\frac{d\mu}{d\pi}$, then the DV rate function can be written in terms of the Dirichlet form:
$$
I(\mu)
={}
-\left\langle \sqrt{f},\, L\sqrt{f}\right\rangle_\pi,
\qquad
\langle a,b\rangle_\pi=\int_E a\,b\,d\pi.
$$

This representation makes clear that $I(\mu)$ measures how costly it is for the process to maintain atypical occupation statistics.

## DV duality and cumulant generating functions

A central application is the asymptotic log-moment generating function of additive functionals.
For a bounded measurable “potential” $V:E\to\mathbb{R}$, define
$$
\Lambda(V)
={}
\lim_{T\to\infty}\frac{1}{T}\log
\mathbb{E}_\pi\!\left[
\exp\!\left(\int_0^T V(X_t)\,dt\right)
\right].
$$

DV theory identifies $\Lambda(V)$ as the Legendre–Fenchel dual of $I$:
$$
\Lambda(V)
={}
\sup_{\mu}
\left\{
\int_E V\,d\mu - I(\mu)
\right\},
$$
an instance of {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel duality" >}} (often combined with Varadhan-type lemmas).

## Context in statistical mechanics

- The DV functional plays the role of an “entropic cost” for sustaining a non-typical time-averaged state in nonequilibrium models (compare {{< knowl id="nonequilibrium-steady-state" text="nonequilibrium steady states" >}}).
- In interacting particle systems, DV-type LDPs underpin variational principles for dynamical free energies and connect to hydrodynamic and macroscopic fluctuation theories (see {{< knowl id="hydrodynamic-limit-theorem" text="hydrodynamic limits" >}}).
