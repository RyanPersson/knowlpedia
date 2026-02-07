---
title: "Correlation length"
description: "Characteristic length scale controlling how fast connected correlations decay with distance."
---

Consider an equilibrium state (for instance the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}) on a $d$-dimensional system such as a {{< knowl id="lattice-zd" section="discrete-structures" text="$\mathbb{Z}^d$ lattice" >}} or a continuum. For two (typically local) observables $A_x$ and $B_0$, the {{< knowl id="correlation-function-two-point" text="two-point correlation function" >}} is
$$
G(x) \;=\; \langle A_x B_0\rangle,
$$

where $\langle\cdot\rangle$ denotes an {{< knowl id="ensemble-average" text="ensemble average" >}}. The physically meaningful quantity for “independent fluctuations at long distance” is the {{< knowl id="connected-correlation-function" text="connected correlation function" >}}
$$
G_c(x) \;=\; \langle A_x B_0\rangle \;-\; \langle A_x\rangle\,\langle B_0\rangle.
$$

## Exponential correlation length

If the state is translation invariant and correlations *cluster*, one often observes an exponential envelope
$$
|G_c(x)| \sim e^{-|x|/\xi}\qquad (|x|\to\infty),
$$

in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}. When the limit exists, the (exponential) **correlation length** $\xi\in(0,\infty]$ can be defined by
$$
\xi^{-1}
\;=\;
-\lim_{|x|\to\infty}\frac{1}{|x|}\,\log |G_c(x)|.
$$
Equivalently, one may define an upper correlation length via a bound of the form
$$
|G_c(x)| \le C\,e^{-|x|/\xi}\quad \text{for all sufficiently large }|x|.
$$

- $\xi<\infty$ indicates *short-ranged* correlations (typical of disordered/gapped phases).
- $\xi=\infty$ indicates *long-ranged* or *critical* correlations (e.g. algebraic decay at a critical point).

## Second-moment correlation length

A widely used alternative is the **second-moment correlation length**, which is well-defined when $G_c$ is nonnegative and summable (common in ferromagnets above criticality):
$$
\xi_{\mathrm{2nd}}^{\,2}
\;=\;
\frac{1}{2d}\,
\frac{\sum_{x\in\mathbb{Z}^d} |x|^2\,G_c(x)}{\sum_{x\in\mathbb{Z}^d} G_c(x)}.
$$
This version is especially convenient numerically and in finite systems.

## Link to susceptibility and integrated correlations

For many order parameters, the {{< knowl id="susceptibility-stat-mech" text="susceptibility" >}} is an *integral/sum* of connected correlations, so a growing $\xi$ typically produces a growing response. Concretely, when an extensive observable is a spatial sum of local fields, the integrated $G_c$ controls the linear response and becomes large when the decay length $\xi$ becomes large.

## Transfer-matrix interpretation in 1D

In one-dimensional models constructed via the {{< knowl id="construction-transfer-matrix-1d" text="transfer matrix" >}}, connected correlations often behave like a ratio of eigenvalues:
$$
G_c(r)\propto \left(\frac{\lambda_1}{\lambda_0}\right)^r,
\qquad r\in\mathbb{N},
$$
so the exponential correlation length is
$$
\xi \;=\; \frac{1}{\log(\lambda_0/|\lambda_1|)}.
$$

Here $\lambda_0$ is the leading eigenvalue and $\lambda_1$ the subleading eigenvalue controlling the slowest decay mode.
