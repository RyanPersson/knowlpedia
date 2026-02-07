---
title: "Thermodynamic limit of pressure (lattice)"
description: "The existence and properties of the pressure in the infinite-volume limit for lattice systems."
---

For a lattice system on a finite region $\Lambda \subset \mathbb{Z}^d$ at inverse temperature $\beta$, the **pressure** (or log-partition density) is
$$
p_\Lambda(\beta) = \frac{1}{|\Lambda|} \log Z_\Lambda(\beta),
$$

where $Z_\Lambda$ is the {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}}.

## Thermodynamic limit

Under standard conditions (translation-invariant interactions with suitable decay), the limit
$$
p(\beta) = \lim_{\Lambda \nearrow \mathbb{Z}^d} p_\Lambda(\beta)
$$

exists and is independent of the sequence of regions $\Lambda$ and of {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}}.

## Properties

- $p(\beta)$ is a convex function of $\beta^{-1}$.
- Derivatives of $p$ with respect to parameters yield thermodynamic densities (energy, magnetization, etc.).
- Non-analyticity of $p(\beta)$ signals a {{< knowl id="phase-transition-gibbs" text="phase transition" >}}.

The pressure is closely connected to the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} and its {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume limit" >}}; see also the general notion of {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}.
