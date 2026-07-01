+++
id = "stat-mech/jarzynski-equality"
title = "Jarzynski equality"
kind = "knowl"
summary = "Nonequilibrium work identity: ⟨e^{-βW}⟩ = e^{-βΔF} for protocols starting in equilibrium, yielding ΔF from nonequilibrium experiments and implying ⟨W⟩≥ΔF."
aliases = ["jarzynski-equality", "Jarzynski equality"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/jarzynski-equality.md"
+++

## Statement
Let a system at inverse temperature $\beta=1/(k_B T)$ (with $T$ the [[thermodynamics/temperature-thermo|temperature]]) start in equilibrium at control parameter $\lambda_0$, typically the [[stat-mech/canonical-ensemble|canonical ensemble]].

Drive the system with an arbitrary (possibly fast) protocol $\lambda_t$ over $t\in[0,\tau]$. For each realization, measure the work $W$ performed on the system (see [[stat-mech/work-distribution-nonequilibrium|work distribution]]). Let
$$
\Delta F \;=\; F(\lambda_\tau)-F(\lambda_0)
$$

be the equilibrium free-energy difference at the same $\beta$ (see [[stat-mech/free-energy-difference-nonequilibrium|nonequilibrium free-energy difference]]).

Then the **Jarzynski equality** is
$$
\left\langle e^{-\beta W}\right\rangle \;=\; e^{-\beta \Delta F},
$$

where $\langle\cdot\rangle$ denotes the ensemble average over repeated realizations (an [[probability/expectation|expectation]] with respect to the induced work distribution).

## Conditions (minimal checklist)
- Initial state is equilibrium at $\lambda_0$ (canonical, or appropriate equilibrium ensemble).
- Dynamics are microreversible (time-reversal symmetric Hamiltonian dynamics, or suitable stochastic dynamics coupled to a heat bath).
- Work is defined consistently with the driven parameter (protocol work).

These assumptions are also those used for the [[stat-mech/fluctuation-theorem-crooks|Crooks fluctuation theorem]], from which Jarzynski can be derived.

## Consequences
### Second-law bound (via Jensen)
Since $\exp$ is convex,
$$
e^{-\beta\langle W\rangle} \;\le\; \left\langle e^{-\beta W}\right\rangle
\;=\; e^{-\beta\Delta F},
$$
hence
$$
\langle W\rangle \;\ge\; \Delta F,
$$
consistent with the [[thermodynamics/second-law-thermodynamics|second law]].

### Dissipated work
Define the dissipated work
$$
W_{\mathrm{diss}} \;=\; W-\Delta F.
$$

Jarzynski becomes $\langle e^{-\beta W_{\mathrm{diss}}}\rangle = 1$, emphasizing that fluctuations with unusually small $W_{\mathrm{diss}}$ control the exponential average.

### Near-equilibrium expansion
If $W$ has small fluctuations around its mean, cumulant expansion gives
$$
\Delta F \approx \langle W\rangle - \frac{\beta}{2}\,\mathrm{Var}(W) + \cdots,
$$
linking nonequilibrium work fluctuations to equilibrium free-energy differences (compare with linear-response identities such as [[stat-mech/fluctuation-dissipation-theorem|fluctuation–dissipation]]).

## Practical note (convergence)
Estimating $\Delta F$ via $-\beta^{-1}\ln\langle e^{-\beta W}\rangle$ can be statistically challenging because rare low-work events dominate the exponential average. Using both forward and reverse processes with [[stat-mech/fluctuation-theorem-crooks|Crooks]] often improves efficiency.
