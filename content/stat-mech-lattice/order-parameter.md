---
title: "Order parameter"
description: "A quantitative diagnostic that distinguishes phases by taking different typical values in different Gibbs states, often vanishing in disordered/symmetric phases and nonzero in ordered phases."
---

An **order parameter** is a map from equilibrium states (typically {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}}) to a finite-dimensional quantity (often $\mathbb{R}$ or $\mathbb{R}^k$) that separates phases.

In lattice spin systems, a common choice is the expectation of a (quasi-)local observable $O$:
$$
\mathcal{M}(\mu)\;:=\;\mu(O),
$$

where $O$ is chosen so that $\mathcal{M}$ differs across distinct {{< knowl id="pure-phase" text="pure phases" >}} ({{< knowl id="extremal-gibbs-measure" text="extremal Gibbs measures" >}}). For the {{< knowl id="ising-model" text="Ising model" >}} at $h=0$, the canonical example is magnetization with $O=\sigma_0$, leading to {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}}.

## Key properties
- **Phase discrimination:** If $\mu_1,\mu_2$ are distinct equilibrium phases, a good order parameter satisfies $\mathcal{M}(\mu_1)\neq \mathcal{M}(\mu_2)$.
- **Symmetry behavior:** In models with a symmetry group $G$, an order parameter is often chosen to transform nontrivially under $G$ so that $\mathcal{M}(\mu)=0$ in a $G$-invariant phase but $\mathcal{M}(\mu)\neq 0$ in phases exhibiting {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}}.
- **Dependence on state selection:** When multiple Gibbs measures exist, $\mathcal{M}(\mu)$ can depend on boundary conditions and on how limits are taken (see {{< knowl id="boundary-condition-lattice" text="boundary conditions" >}} and {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measures" >}}).
- **Fluctuations and response:** The response of an order parameter to a conjugate field is captured by linear response, often tied to the {{< knowl id="susceptibility-stat-mech" section="stat-mech" text="susceptibility" >}} and to {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation functions" >}}.

## Physical interpretation
An order parameter measures “how ordered” the system is with respect to a proposed pattern (alignment, staggered alignment, rotational ordering, clustering, etc.). In disordered phases, microscopic fluctuations average out so the order parameter is typically zero (or symmetry-forced to vanish). In ordered phases, correlations persist over long distances, producing a stable macroscopic signal in the order parameter.
