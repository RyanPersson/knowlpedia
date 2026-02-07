---
title: "Canonical ensemble from the microcanonical ensemble"
description: "Derives the canonical distribution for a subsystem coupled to a large reservoir, and relates Z(β) to the Laplace transform of the density of states."
---

The canonical ensemble can be constructed from the microcanonical ensemble by considering a small subsystem weakly coupled to a large heat bath. This derivation explains why Boltzmann weights appear and clarifies the meaning of the inverse temperature $\beta$ as a derivative of microcanonical entropy.

It complements the direct definition of the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}} and connects to the microcanonical entropy built from the {{< knowl id="density-of-states" text="density of states" >}} (see {{< knowl id="construction-microcanonical-entropy-density-of-states" section="thermodynamics" text="microcanonical entropy from Ω(E)" >}}).

## Microcanonical starting point: system + bath

Consider a total isolated system composed of a subsystem $S$ and a bath (reservoir) $B$, with total energy fixed at $E_{\mathrm{tot}}$. Assume:
1. The coupling between $S$ and $B$ is weak, so energies add approximately:
   $$
   E_{\mathrm{tot}} \approx E_S + E_B.
   $$

2. The composite system is described by the {{< knowl id="microcanonical-measure" text="microcanonical ensemble" >}} at energy $E_{\mathrm{tot}}$ (or in a thin {{< knowl id="microcanonical-shell" text="energy shell" >}}).

Let $s$ denote a microstate of $S$ with energy $E_S(s)$. Under the microcanonical distribution of the composite system, the probability of observing $S$ in microstate $s$ is proportional to the number of compatible bath microstates at energy $E_B=E_{\mathrm{tot}}-E_S(s)$:
$$
\mathbb{P}(s) \;\propto\; \Omega_B\!\big(E_{\mathrm{tot}}-E_S(s)\big),
$$

where $\Omega_B$ is the bath density of states.

## Entropy expansion and emergence of the Boltzmann weight

Write the bath microcanonical entropy as
$$
S_B(E) \;=\; k_B \log \Omega_B(E),
$$
as in {{< knowl id="boltzmann-entropy-microcanonical" text="Boltzmann microcanonical entropy" >}}.

If the bath is much larger than the subsystem, then $E_S$ is a small perturbation on the bath energy scale, and one expands:
$$
S_B(E_{\mathrm{tot}}-E_S)
\;=\;
S_B(E_{\mathrm{tot}})
-\left(\frac{\partial S_B}{\partial E}\right)_{E_{\mathrm{tot}}} E_S
+\text{higher-order terms}.
$$

Exponentiating and using $\Omega_B(E)=\exp(S_B(E)/k_B)$ gives
$$
\Omega_B(E_{\mathrm{tot}}-E_S)
\;\approx\;
\Omega_B(E_{\mathrm{tot}})\,\exp\!\left(-\beta\,E_S\right),
$$
with
$$
\beta \;=\; \frac{1}{k_B}\left(\frac{\partial S_B}{\partial E}\right)_{E_{\mathrm{tot}}}.
$$

This identifies $\beta$ with the bath inverse temperature, matching {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="thermodynamic inverse temperature" >}} and the microcanonical derivative rule in {{< knowl id="construction-temperature-from-entropy" text="constructing temperature from entropy" >}}.

Therefore,
$$
\mathbb{P}(s) \;\propto\; e^{-\beta E_S(s)},
$$
which is exactly the canonical Boltzmann weight.

Normalizing over subsystem microstates produces the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}:
$$
Z_S(\beta) \;=\; \sum_{s} e^{-\beta E_S(s)}
\quad\text{(discrete states)},
\qquad
Z_S(\beta) \;=\; \int e^{-\beta H_S(x)}\,\mathrm{d}\mu_S(x)
\quad\text{(continuous phase space)}.
$$

## Laplace transform relation: Z as a transform of Ω

The same relationship can be expressed directly in terms of the subsystem density of states $\Omega_S(E)$. Formally,
$$
Z_S(\beta)
\;=\;
\int \Omega_S(E)\,e^{-\beta E}\,\mathrm{d}E,
$$
so the canonical ensemble is a Laplace-transform reweighting of the microcanonical counting measure. This is the analytic backbone of the equivalence between ensembles in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}.

Under suitable convexity/regularity assumptions, the dominant contribution to this integral at large system size is governed by a saddle point, and the canonical free energy becomes a Legendre-type transform of the microcanonical entropy density (compare {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} and {{< knowl id="construction-legendre-s-to-f" text="Legendre construction from S to F" >}}).

## Physical interpretation and limits of the construction

- **Why it works:** the bath entropy is extensive, so its derivative $\partial_E S_B$ changes slowly when energy is exchanged with a small subsystem. That is the precise sense in which the bath “imposes” an approximately constant temperature on $S$.
- **Fluctuations:** canonical energy fluctuations of $S$ arise because $E_S$ is not fixed; they are encoded by derivatives of $\log Z_S$ (see {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuation formulas from log Z" >}}).
- **Ensemble equivalence:** in large systems with short-range interactions and no phase coexistence pathologies, microcanonical and canonical descriptions yield the same thermodynamics; outside these regimes, equivalence can fail and the microcanonical entropy may be nonconcave.

This subsystem–reservoir derivation is the standard conceptual route from isolated dynamics (microcanonical) to thermal equilibrium at fixed temperature (canonical).
