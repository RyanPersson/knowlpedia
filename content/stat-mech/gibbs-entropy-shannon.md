---
title: "Gibbs entropy (Shannon form)"
description: "Entropy of an ensemble: minus k_B times the expected log-probability of microstates."
---

**Definition (Gibbs/Shannon entropy).**  
An equilibrium ensemble is a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} on microstates (often given by a density with respect to a reference measure). For a discrete set of microstates with probabilities $\{p_i\}$, the **Gibbs (Shannon) entropy** is
$$
S_G(p)=-k_B\sum_i p_i\ln p_i.
$$

This is $k_B$ times the {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}.

For a classical phase-space description, let $d\Gamma$ denote the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} and let $\rho(x)$ be a probability density on {{< knowl id="phase-space-classical" text="phase space" >}} (so $\int \rho\,d\Gamma=1$, interpreted via the {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}}). Then
$$
S_G[\rho] = -k_B \int \rho(x)\,\ln \rho(x)\,d\Gamma(x).
$$

**Remark on “continuous entropy.”**  
In the continuous setting, $\rho$ is a density *with respect to* a chosen reference measure (here the Liouville/phase-space volume). Changing that reference shifts $S_G$ by an additive constant. In statistical mechanics, this ambiguity matches the physical fact that entropy is defined up to an additive constant once a coarse-graining (or a microscopic phase-space cell) is fixed.

**Canonical example.**  
In the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}, with {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} $H(x)$, inverse temperature {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="β" >}}, and {{< knowl id="partition-function-canonical" text="partition function" >}} $Z(\beta)$, the density is
$$
\rho_\beta(x)=\frac{e^{-\beta H(x)}}{Z(\beta)}.
$$

Using the {{< knowl id="ensemble-average" text="ensemble average" >}} $U=\langle H\rangle_{\rho_\beta}$, one obtains the identity
$$
S_G[\rho_\beta] = k_B\big(\ln Z(\beta)+\beta U\big).
$$
This links Gibbs entropy directly to the logarithm of the partition function and to {{< knowl id="free-energy-statistical" text="statistical free energy" >}}.

**Physical interpretation.**  
$S_G$ measures uncertainty (spread) of the ensemble over microstates: it is large when probability mass is distributed over many microstates and small when concentrated. It is also the entropy functional appearing in entropy maximization constructions such as {{< knowl id="construction-entropy-maximization-thermal" text="maximum-entropy construction of thermal states" >}}.

**Inequalities and irreversibility viewpoint.**  
Comparing two ensembles $P$ and $Q$ naturally introduces {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}, whose nonnegativity is {{< knowl id="gibbs-inequality-kl" section="probability" text="Gibbs’ inequality" >}}. In equilibrium statistical mechanics, this underlies variational characterizations of the canonical state and convexity properties of $\ln Z$.
