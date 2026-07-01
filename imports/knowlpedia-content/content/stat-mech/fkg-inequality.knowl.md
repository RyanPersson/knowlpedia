+++
id = "stat-mech/fkg-inequality"
title = "FKG inequality"
kind = "knowl"
summary = "Positive association for log-supermodular measures; in particular, ferromagnetic lattice Gibbs measures satisfy positive correlation of increasing observables."
aliases = ["fkg-inequality", "FKG inequality"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/fkg-inequality.md"
+++

## Statement

Let $\Omega=\{-1,+1\}^\Lambda$ with $\Lambda$ finite, equipped with the product partial order $\sigma\le \eta$ iff $\sigma_i\le \eta_i$ for all $i\in\Lambda$.

A function $f:\Omega\to\mathbb{R}$ is **increasing** if $\sigma\le \eta$ implies $f(\sigma)\le f(\eta)$.

A probability measure $\mu$ on $\Omega$ satisfies the **FKG lattice condition** (log-supermodularity) if for all $\sigma,\eta\in\Omega$,
$$
\mu(\sigma\wedge \eta)\,\mu(\sigma\vee \eta)\;\ge\;\mu(\sigma)\,\mu(\eta),
$$

where $(\sigma\wedge\eta)_i=\min\{\sigma_i,\eta_i\}$ and $(\sigma\vee\eta)_i=\max\{\sigma_i,\eta_i\}$.

**FKG inequality (positive association).**
If $\mu$ satisfies the FKG lattice condition, then for all bounded increasing functions $f,g$,
$$
\mathbb{E}_\mu[f\,g]\;\ge\;\mathbb{E}_\mu[f]\;\mathbb{E}_\mu[g],
$$

where $\mathbb{E}_\mu[\cdot]$ denotes expectation (see [[probability/expectation|expectation]]).

## Key hypotheses and conclusions

### Hypotheses
- Finite partially ordered configuration space $\Omega=\{-1,+1\}^\Lambda$.
- A [[probability/probability-measure|probability measure]] $\mu$ satisfying the FKG lattice condition.
- Observables $f,g$ are bounded and increasing.

### Conclusions
- **Nonnegative covariance of increasing observables:** for increasing $f,g$,
  $$
  \mathrm{Cov}_\mu(f,g)=\mathbb{E}_\mu[f g]-\mathbb{E}_\mu[f]\mathbb{E}_\mu[g]\ge 0.
  $$
- **Monotonicity and comparison:** positive association is a key input for stochastic domination and monotone coupling arguments (often used to compare different boundary conditions or external fields in lattice systems).

## Connection to lattice Gibbs measures

For the ferromagnetic [[stat-mech-lattice/ising-model|Ising model]] (and more generally many attractive lattice systems), the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] satisfies the FKG lattice condition when the couplings are ferromagnetic ($J_{ij}\ge 0$). In that setting, the FKG inequality yields positivity of correlations for *increasing* observables, and it is a standard tool for proving existence and ordering of infinite-volume Gibbs states (see [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] and [[stat-mech-lattice/phase-transition-gibbs|phase transitions]]).

In statistical mechanics, FKG is one of the main correlation-inequality engines, complementary to the more model-specific [[stat-mech/gks-inequalities|GKS inequalities]] and [[stat-mech/griffiths-inequalities|Griffiths inequalities]].
