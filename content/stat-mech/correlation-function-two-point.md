---
title: "Two-Point Correlation Function"
description: "The ensemble expectation ⟨A(x)B(y)⟩ of observables at two points, encoding spatial (or temporal) correlations."
---

Many statistical-mechanical models are built from *local* degrees of freedom (spins, densities, fields) living on a {{< knowl id="lattice-zd" section="discrete-structures" text="lattice" >}} or in continuous space. For local observables $A_x$ and $B_y$ (e.g. “spin at site $x$”), the **two-point correlation function** measures how values at two locations co-vary under a chosen ensemble such as the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} or a more general {{< knowl id="generalized-gibbs-ensemble" text="generalized Gibbs ensemble" >}}.

The (possibly uncentered) **two-point correlation function** is
$$
G_{AB}(x,y) \;:=\; \langle A_x\,B_y\rangle.
$$

If the system is translation invariant in equilibrium, then $G_{AB}(x,y)$ depends only on the separation $r=x-y$, and one often writes
$$
G_{AB}(r) := \langle A_0\,B_r\rangle.
$$

This object is distinct from, but closely related to, the {{< knowl id="connected-correlation-function" text="connected correlation function" >}}, which removes the part coming from the separate one-point means.

## Connected vs. unconnected
Writing fluctuations $\delta A_x = A_x-\langle A_x\rangle$ (see {{< knowl id="fluctuation-observable" text="fluctuation of an observable" >}}), the connected two-point function is
$$
G^{(c)}_{AB}(x,y)
\;:=\;
\langle \delta A_x\,\delta B_y\rangle
\;=\;
\langle A_x B_y\rangle - \langle A_x\rangle\langle B_y\rangle.
$$

Thus $G^{(c)}_{AB}(x,y)$ is a spatial version of {{< knowl id="covariance-observables-ensemble" text="covariance" >}}.

## Key formulas and interpretations
- **Independence test:** If the degrees of freedom at $x$ and $y$ are effectively independent under the ensemble, then $G^{(c)}_{AB}(x,y)\approx 0$ (no genuine correlation between fluctuations).

- **Correlation length:** In phases with short-range correlations, the connected function often decays with distance and defines a {{< knowl id="correlation-length" text="correlation length" >}} $\xi$, heuristically via behavior like $G^{(c)}_{AB}(r)\sim e^{-|r|/\xi}$ at large $|r|$.

- **Susceptibility as an integrated correlation:** For many models, the linear response (a {{< knowl id="susceptibility-stat-mech" text="susceptibility" >}}) can be expressed as a sum/integral of connected two-point correlations, reflecting that macroscopic response is the accumulation of microscopic correlated fluctuations.
