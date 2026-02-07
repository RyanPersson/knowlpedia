---
title: "Thermal state from entropy maximization"
description: "Maximum-entropy derivation of the canonical (and generalized Gibbs) distribution from macroscopic constraints."
---

A central construction of equilibrium statistical mechanics is: **given only partial macroscopic information, choose the least biased microscopic distribution consistent with that information**. This principle is implemented by maximizing the {{< knowl id="gibbs-entropy-shannon" text="Gibbs/Shannon entropy" >}}.

## Problem (choose a distribution from constraints)

Let $x$ denote a {{< knowl id="microstate-classical" text="microstate" >}} in {{< knowl id="phase-space-classical" text="classical phase space" >}}, and let $H(x)$ be the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian function" >}}. A statistical state is a probability density $\rho(x)\ge 0$ normalized with respect to the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} $d\Gamma$:
$$
\int \rho(x)\,d\Gamma(x) \;=\; 1.
$$

The (dimensionless) entropy functional is
$$
s[\rho] \;=\; -\int \rho(x)\,\log\rho(x)\,d\Gamma(x),
$$

and the physical entropy is $S[\rho]=k_B\,s[\rho]$ with $k_B$ the {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann constant" >}}.

Assume we only know the mean energy (a macroscopic constraint)
$$
\int \rho(x)\,H(x)\,d\Gamma(x) \;=\; U.
$$

## Solution (canonical Gibbs distribution)

Maximizing $s[\rho]$ subject to normalization and fixed mean energy gives, via Lagrange multipliers, a unique maximizer of the form
$$
\rho_\beta(x)
\;=\;
\frac{e^{-\beta H(x)}}{Z(\beta)},
\qquad
Z(\beta)
\;=\;
\int e^{-\beta H(x)}\,d\Gamma(x).
$$

The normalizing factor $Z(\beta)$ is the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}, and the resulting state is exactly the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}. The multiplier $\beta$ is identified with the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}.

This provides a variational (information-theoretic) characterization of thermal equilibrium: among all distributions with the same mean energy, $\rho_\beta$ has maximal entropy.

## Generalization (multiple constraints)

If, in addition to the mean energy, one constrains the mean values of other quantities $Q_i(x)$ (often conserved charges),
$$
\int \rho(x)\,Q_i(x)\,d\Gamma(x) \;=\; q_i,
$$
the same entropy-maximization procedure yields
$$
\rho(x) \propto \exp\!\Big(-\lambda_0 - \sum_i \lambda_i Q_i(x)\Big),
$$
which is the basis of the {{< knowl id="generalized-gibbs-ensemble" text="generalized Gibbs ensemble" >}}.

## Interpretation via relative entropy

Entropy maximization can also be phrased as an optimization over information distance: the maximizer is the distribution that is “closest” to a chosen reference measure while satisfying the constraints, using the {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Kullback–Leibler divergence" >}}. The uniqueness/optimality is underwritten by the {{< knowl id="gibbs-inequality-kl" section="probability" text="Gibbs inequality" >}}.

## Physical meaning

- The constraints encode what is known macroscopically (here, the mean energy).
- The maximizer is the least structured microscopic state compatible with those constraints.
- When a small system is weakly coupled to a large heat bath, this construction matches the canonical state obtained from {{< knowl id="construction-canonical-from-microcanonical" text="deriving the canonical ensemble from the microcanonical picture" >}}.
