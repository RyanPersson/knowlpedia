+++
id = "stat-mech/gibbs-variational-principle"
title = "Gibbs variational principle (canonical ensemble)"
kind = "knowl"
summary = "The canonical Gibbs state minimizes the free-energy functional, equivalently maximizing entropy under an energy penalty; the gap is relative entropy."
aliases = ["gibbs-variational-principle", "Gibbs variational principle (canonical ensemble)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/gibbs-variational-principle.md"
+++

## Statement
Fix inverse temperature $\beta=1/(k_B T)$ and a Hamiltonian [[stat-mech/hamiltonian-function-classical|H]] on a classical [[stat-mech/phase-space-classical|phase space]] with reference measure $\lambda$.
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

and the unique minimizer is the [[stat-mech/canonical-ensemble|canonical Gibbs measure]] $\mu_\beta$ with density
$\rho_\beta(x) = e^{-\beta H(x)}/Z(\beta)$, where $Z(\beta)$ is the [[stat-mech/partition-function-canonical|canonical partition function]].

Equivalently, for any $\mu$,
$$
\langle H\rangle_\mu - T S(\mu)
\;=\;
F(\beta) + k_B T\, D(\mu \,\|\, \mu_\beta),
$$

where $D(\mu\|\mu_\beta)$ is [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]]. In particular,
$\langle H\rangle_\mu - T S(\mu) \ge F(\beta)$.

## Key hypotheses
- $Z(\beta)<\infty$ so the [[stat-mech/canonical-ensemble|canonical ensemble]] exists.
- $\mu$ is absolutely continuous with respect to $\lambda$ so that $S(\mu)$ is meaningful (otherwise interpret $S(\mu)=-\infty$).
- Integrability conditions ensuring $\langle H\rangle_\mu$ and $S(\mu)$ are well-defined for the class of measures considered.

## Conclusion
- The canonical Gibbs measure is characterized as the unique minimizer of the free-energy functional $\mu \mapsto \langle H\rangle_\mu - T S(\mu)$.
- The “suboptimality gap” to equilibrium is exactly $k_B T$ times the KL divergence to the canonical state.

## Cross-links to definitions
- [[stat-mech/canonical-ensemble|Canonical ensemble]], [[stat-mech/partition-function-canonical|canonical partition function]]
- [[stat-mech/gibbs-entropy-shannon|Gibbs/Shannon entropy (stat mech)]], [[probability/shannon-entropy|Shannon entropy (probability)]]
- [[probability/relative-entropy-kl-divergence|Relative entropy (KL divergence)]]
- [[stat-mech/free-energy-statistical|Statistical free energy]]
## significance
Rewrite the functional at inverse temperature $\beta$ by adding and subtracting $\log Z(\beta)$, then identify the remaining term as a KL divergence using the density $\rho_\beta \propto e^{-\beta H}$. Nonnegativity of KL divergence (a form of [[stat-mech/gibbs-inequality-lemma|Gibbs inequality]]) yields the lower bound and characterizes the minimizer. This principle is the backbone of maximum-entropy and free-energy methods, and it underlies many convexity/duality results such as [[stat-mech/legendre-duality-free-energy-entropy|Legendre duality between free energy and entropy]].
