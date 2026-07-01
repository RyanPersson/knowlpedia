+++
id = "stat-mech/gibbs-entropy-shannon"
title = "Gibbs entropy (Shannon form)"
kind = "knowl"
summary = "Entropy of an ensemble: minus k_B times the expected log-probability of microstates."
aliases = ["gibbs-entropy-shannon", "Gibbs entropy (Shannon form)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/gibbs-entropy-shannon.md"
+++

**Definition (Gibbs/Shannon entropy).**
An equilibrium ensemble is a [[probability/probability-measure|probability measure]] on microstates (often given by a density with respect to a reference measure). For a discrete set of microstates with probabilities $\{p_i\}$, the **Gibbs (Shannon) entropy** is
$$
S_G(p)=-k_B\sum_i p_i\ln p_i.
$$

This is $k_B$ times the [[probability/shannon-entropy|Shannon entropy]].

For a classical phase-space description, let $d\Gamma$ denote the [[stat-mech/phase-space-volume-element|phase-space volume element]] and let $\rho(x)$ be a probability density on [[stat-mech/phase-space-classical|phase space]] (so $\int \rho\,d\Gamma=1$, interpreted via the [[measure-theory/lebesgue-integral|Lebesgue integral]]). Then
$$
S_G[\rho] = -k_B \int \rho(x)\,\ln \rho(x)\,d\Gamma(x).
$$

**Remark on “continuous entropy.”**
In the continuous setting, $\rho$ is a density *with respect to* a chosen reference measure (here the Liouville/phase-space volume). Changing that reference shifts $S_G$ by an additive constant. In statistical mechanics, this ambiguity matches the physical fact that entropy is defined up to an additive constant once a coarse-graining (or a microscopic phase-space cell) is fixed.

**Canonical example.**
In the [[stat-mech/canonical-ensemble|canonical ensemble]], with [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H(x)$, inverse temperature [[thermodynamics/inverse-temperature-beta|β]], and [[stat-mech/partition-function-canonical|partition function]] $Z(\beta)$, the density is
$$
\rho_\beta(x)=\frac{e^{-\beta H(x)}}{Z(\beta)}.
$$

Using the [[stat-mech/ensemble-average|ensemble average]] $U=\langle H\rangle_{\rho_\beta}$, one obtains the identity
$$
S_G[\rho_\beta] = k_B\big(\ln Z(\beta)+\beta U\big).
$$
This links Gibbs entropy directly to the logarithm of the partition function and to [[stat-mech/free-energy-statistical|statistical free energy]].

**Physical interpretation.**
$S_G$ measures uncertainty (spread) of the ensemble over microstates: it is large when probability mass is distributed over many microstates and small when concentrated. It is also the entropy functional appearing in entropy maximization constructions such as [[stat-mech/construction-entropy-maximization-thermal|maximum-entropy construction of thermal states]].

**Inequalities and irreversibility viewpoint.**
Comparing two ensembles $P$ and $Q$ naturally introduces [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]], whose nonnegativity is [[probability/gibbs-inequality-kl|Gibbs’ inequality]]. In equilibrium statistical mechanics, this underlies variational characterizations of the canonical state and convexity properties of $\ln Z$.
