---
title: "Crooks fluctuation theorem"
description: "Relation between forward and reverse nonequilibrium work distributions: P_F(W)/P_R(-W)=exp(β(W-ΔF)), implying Jarzynski’s equality and identifying ΔF from a crossing point."
---

## Setup (forward and reverse protocols)
Consider a system with control parameter $\lambda$ (e.g. a trap position, field, volume) driven by a time-dependent protocol $\lambda_t$ for $t\in[0,\tau]$.

- **Forward (F):** start in equilibrium at $\lambda_0$ with inverse temperature $\beta=1/(k_B T)$ (with $T$ the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}), typically the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}.
- **Reverse (R):** start in equilibrium at $\lambda_\tau$ and drive with the time-reversed protocol $\tilde\lambda_t=\lambda_{\tau-t}$.

For each realization, define the work $W$ (see {{< knowl id="work-distribution-nonequilibrium" text="work distribution" >}}). Let $P_F(W)$ and $P_R(W)$ be the corresponding work probability densities (with respect to the relevant {{< knowl id="probability-measure" section="probability" text="probability measure" >}}).

Let $\Delta F = F(\lambda_\tau)-F(\lambda_0)$ denote the equilibrium free-energy difference at the same $\beta$ (see {{< knowl id="free-energy-difference-nonequilibrium" text="nonequilibrium free-energy difference" >}} and {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}).

## Theorem (Crooks)
Under microreversible dynamics (time-reversal symmetric Hamiltonian dynamics, or Markov dynamics satisfying microscopic reversibility such as {{< knowl id="detailed-balance" text="detailed balance" >}} with a heat bath), the work distributions satisfy
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
   i.e. {{< knowl id="jarzynski-equality" text="Jarzynski’s equality" >}}.

3. **Second-law inequality.**  
   Using Jensen’s inequality,
   $$
   \langle W\rangle_F \;\ge\; \Delta F,
   $$
   consistent with the {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}}.

## Information-theoretic form (dissipation as relative entropy)
At the level of trajectories $\omega$ (paths), Crooks’ theorem is equivalent to a path-space likelihood ratio
$$
\ln\frac{\mathbb{P}_F(\omega)}{\mathbb{P}_R(\tilde\omega)}
={}
\beta\bigl(W(\omega)-\Delta F\bigr),
$$

so the mean dissipated work $\langle W-\Delta F\rangle_F$ is proportional to a {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} between forward and reverse path measures.

## Practical note
Crooks’ relation underlies statistically efficient estimators of $\Delta F$ (e.g. Bennett-type methods) built from both $P_F$ and $P_R$; see {{< knowl id="free-energy-difference-nonequilibrium" text="free-energy difference from nonequilibrium work" >}}.
