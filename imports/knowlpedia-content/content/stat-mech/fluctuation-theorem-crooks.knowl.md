+++
id = "stat-mech/fluctuation-theorem-crooks"
title = "Crooks fluctuation theorem"
kind = "knowl"
summary = "Relation between forward and reverse nonequilibrium work distributions: P_F(W)/P_R(-W)=exp(β(W-ΔF)), implying Jarzynski’s equality and identifying ΔF from a crossing point."
aliases = ["fluctuation-theorem-crooks", "Crooks fluctuation theorem"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/fluctuation-theorem-crooks.md"
+++

## Setup (forward and reverse protocols)
Consider a system with control parameter $\lambda$ (e.g. a trap position, field, volume) driven by a time-dependent protocol $\lambda_t$ for $t\in[0,\tau]$.

- **Forward (F):** start in equilibrium at $\lambda_0$ with inverse temperature $\beta=1/(k_B T)$ (with $T$ the [[thermodynamics/temperature-thermo|temperature]]), typically the [[stat-mech/canonical-ensemble|canonical ensemble]].
- **Reverse (R):** start in equilibrium at $\lambda_\tau$ and drive with the time-reversed protocol $\tilde\lambda_t=\lambda_{\tau-t}$.

For each realization, define the work $W$ (see [[stat-mech/work-distribution-nonequilibrium|work distribution]]). Let $P_F(W)$ and $P_R(W)$ be the corresponding work probability densities (with respect to the relevant [[probability/probability-measure|probability measure]]).

Let $\Delta F = F(\lambda_\tau)-F(\lambda_0)$ denote the equilibrium free-energy difference at the same $\beta$ (see [[stat-mech/free-energy-difference-nonequilibrium|nonequilibrium free-energy difference]] and [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]).

## Theorem (Crooks)
Under microreversible dynamics (time-reversal symmetric Hamiltonian dynamics, or Markov dynamics satisfying microscopic reversibility such as [[stat-mech/detailed-balance|detailed balance]] with a heat bath), the work distributions satisfy
$$
\frac{P_F(W)}{P_R(-W)} \;=\; \exp\!\bigl(\beta(W-\Delta F)\bigr).
$$

### Immediate consequences
1. **Crossing point identifies $\Delta F$.**
   The value $W^\star$ where $P_F(W^\star)=P_R(-W^\star)$ satisfies $W^\star=\Delta F$.

2. **Jarzynski follows by integration.**
   Multiply both sides by $P_R(-W)e^{-\beta W}$ and integrate over $W$ to obtain
   $$
   \left\langle e^{-\beta W}\right\rangle_F \;=\; e^{-\beta \Delta F},
   $$
   i.e. [[stat-mech/jarzynski-equality|Jarzynski’s equality]].

3. **Second-law inequality.**
   Using Jensen’s inequality,
   $$
   \langle W\rangle_F \;\ge\; \Delta F,
   $$
   consistent with the [[thermodynamics/second-law-thermodynamics|second law]].

## Information-theoretic form (dissipation as relative entropy)
At the level of trajectories $\omega$ (paths), Crooks’ theorem is equivalent to a path-space likelihood ratio
$$
\ln\frac{\mathbb{P}_F(\omega)}{\mathbb{P}_R(\tilde\omega)}
={}
\beta\bigl(W(\omega)-\Delta F\bigr),
$$

so the mean dissipated work $\langle W-\Delta F\rangle_F$ is proportional to a [[probability/relative-entropy-kl-divergence|relative entropy]] between forward and reverse path measures.

## Practical note
Crooks’ relation underlies statistically efficient estimators of $\Delta F$ (e.g. Bennett-type methods) built from both $P_F$ and $P_R$; see [[stat-mech/free-energy-difference-nonequilibrium|free-energy difference from nonequilibrium work]].
