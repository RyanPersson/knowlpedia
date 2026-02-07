---
title: "Gibbs variational principle (canonical ensemble)"
description: "The canonical Gibbs state minimizes the free-energy functional, equivalently maximizing entropy under an energy penalty; the gap is relative entropy."
---

## Statement
Fix inverse temperature $\beta=1/(k_B T)$ and a Hamiltonian {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="H" >}} on a classical {{< knowl id="phase-space-classical" section="stat-mech" text="phase space" >}} with reference measure $\lambda$.
Let $\mu$ range over probability measures absolutely continuous with respect to $\lambda$, with density $\rho = d\mu/d\lambda$.

Define the entropy functional (Shannon/Gibbs entropy)
$$
S(\mu) \;=\; -k_B \int \rho \log \rho \, d\lambda,
$$

and the mean energy $\langle H\rangle_\mu = \int H\, d\mu$.

Then the canonical free energy satisfies the variational formula
$$
F(\beta) \;=\; \inf_{\mu}\Big\{\langle H\rangle_\mu - T\, S(\mu)\Big\},
$$

and the unique minimizer is the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical Gibbs measure" >}} $\mu_\beta$ with density
$\rho_\beta(x) = e^{-\beta H(x)}/Z(\beta)$, where $Z(\beta)$ is the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}.

Equivalently, for any $\mu$,
$$
\langle H\rangle_\mu - T S(\mu)
\;=\;
F(\beta) + k_B T\, D(\mu \,\|\, \mu_\beta),
$$

where $D(\mu\|\mu_\beta)$ is {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}. In particular,
$\langle H\rangle_\mu - T S(\mu) \ge F(\beta)$.

## Key hypotheses
- $Z(\beta)<\infty$ so the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} exists.
- $\mu$ is absolutely continuous with respect to $\lambda$ so that $S(\mu)$ is meaningful (otherwise interpret $S(\mu)=-\infty$).
- Integrability conditions ensuring $\langle H\rangle_\mu$ and $S(\mu)$ are well-defined for the class of measures considered.

## Conclusion
- The canonical Gibbs measure is characterized as the unique minimizer of the free-energy functional $\mu \mapsto \langle H\rangle_\mu - T S(\mu)$.
- The “suboptimality gap” to equilibrium is exactly $k_B T$ times the KL divergence to the canonical state.

## Cross-links to definitions
- {{< knowl id="canonical-ensemble" section="stat-mech" text="Canonical ensemble" >}}, {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}
- {{< knowl id="gibbs-entropy-shannon" section="stat-mech" text="Gibbs/Shannon entropy (stat mech)" >}}, {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy (probability)" >}}
- {{< knowl id="relative-entropy-kl-divergence" section="probability" text="Relative entropy (KL divergence)" >}}
- {{< knowl id="free-energy-statistical" section="stat-mech" text="Statistical free energy" >}}
## significance
Rewrite the functional at inverse temperature $\beta$ by adding and subtracting $\log Z(\beta)$, then identify the remaining term as a KL divergence using the density $\rho_\beta \propto e^{-\beta H}$. Nonnegativity of KL divergence (a form of {{< knowl id="gibbs-inequality-lemma" text="Gibbs inequality" >}}) yields the lower bound and characterizes the minimizer. This principle is the backbone of maximum-entropy and free-energy methods, and it underlies many convexity/duality results such as {{< knowl id="legendre-duality-free-energy-entropy" text="Legendre duality between free energy and entropy" >}}.
