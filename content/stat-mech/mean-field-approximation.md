---
title: "Mean-field approximation"
description: "A variational/product-measure approximation that replaces interactions by an effective field determined self-consistently, yielding tractable equations for order parameters and approximate free energies."
---

The **mean-field approximation** replaces an interacting many-body system by an effective single-site (or single-particle) problem coupled to a self-consistent average field. It is widely used to obtain qualitative phase diagrams and critical behavior.

## Variational formulation (canonical ensemble)

In the canonical ensemble (see {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}), the equilibrium Gibbs measure minimizes a free-energy functional. A convenient formulation uses the Shannon/Gibbs entropy (see {{< knowl id="gibbs-entropy-shannon" section="stat-mech" text="Gibbs (Shannon) entropy" >}} and {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}).

For a Hamiltonian $H(\sigma)$ on a finite configuration space and a trial probability measure $q$ (see {{< knowl id="probability-measure" section="probability" text="probability measure" >}}), define
$$
\mathcal{F}_\beta[q] \;=\; \mathbb{E}_q[H] \;-\; \beta^{-1} S(q),
\qquad
S(q)=-\sum_\sigma q(\sigma)\log q(\sigma).
$$
Then the equilibrium free energy (see {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}) satisfies
$$
-\beta^{-1}\log Z(\beta)=\inf_q \mathcal{F}_\beta[q].
$$

**Mean-field** restricts the variational class to *product measures* (or low-complexity factorizations), e.g.
$$
q(\sigma)=\prod_{i\in\Lambda} q_i(\sigma_i),
$$
thereby neglecting correlations (compare {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}}).

## Mean-field equation for the Ising model

Consider the nearest-neighbor Ising Hamiltonian on a regular lattice with coordination number $z$:
$$
H(\sigma)=-J\sum_{\langle i,j\rangle}\sigma_i\sigma_j - h\sum_i \sigma_i.
$$

Mean-field replaces neighbors by their average magnetization $m=\mathbb{E}[\sigma_i]$, giving an effective single-site energy
$$
H_i^{\text{MF}}(\sigma_i) = -\sigma_i\,(J z\, m + h).
$$

The single-site distribution is proportional to $\exp(\beta \sigma_i(J z m+h))$, so the self-consistency condition is
$$
m=\tanh\!\big(\beta(J z\, m+h)\big).
$$

Nontrivial solutions at $h=0$ correspond to spontaneous magnetization (see {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}}).

## Mean-field free-energy density (and stability)

A standard mean-field free-energy density as a function of $m$ is
$$
f_{\beta,h}^{\text{MF}}(m)
={}
-\frac{J z}{2}\,m^2 - h m
+\beta^{-1}\left[
\frac{1+m}{2}\log\frac{1+m}{2}
+\frac{1-m}{2}\log\frac{1-m}{2}
\right].
$$

Equilibrium magnetizations are minimizers of $f_{\beta,h}^{\text{MF}}(m)$; multiple local minima correspond to metastability (see {{< knowl id="metastable-state" text="metastable states" >}}).

This $m$-dependent free energy is the simplest instance of a Landau theory (see {{< knowl id="landau-free-energy-functional" text="Landau free-energy functional" >}}).

## When mean-field works (and when it fails)

Mean-field becomes accurate when fluctuations are suppressed, for example:
- in genuine long-range/fully-connected models (it is exact for {{< knowl id="curie-weiss-model" text="Curie–Weiss" >}}),
- in high dimension, or when correlation lengths are short (see {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}).

It typically fails quantitatively near critical points in low dimensions because it neglects long-wavelength fluctuations that dominate critical behavior.
