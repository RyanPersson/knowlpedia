---
title: "Free-energy difference from nonequilibrium work"
description: "Equilibrium ΔF expressed via nonequilibrium work statistics: ΔF = -β^{-1} ln ⟨e^{-βW}⟩ and related inference using Crooks’ theorem."
---

## Equilibrium free-energy difference
For a system at fixed inverse temperature $\beta=1/(k_B T)$ (with $T$ the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}) and control parameter $\lambda$, the equilibrium Helmholtz free energy is
$$
F(\lambda) \;=\; -\beta^{-1}\ln Z(\lambda),
$$

where $Z(\lambda)$ is the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}} (compare {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} and {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}).

The equilibrium free-energy difference between endpoints of a protocol is
$$
\Delta F \;=\; F(\lambda_\tau)-F(\lambda_0).
$$

## Nonequilibrium identification via work statistics
Even if the protocol $\lambda_t$ is fast and drives the system out of equilibrium, $\Delta F$ is determined by nonequilibrium work fluctuations:

### Jarzynski estimator
If realizations start in equilibrium at $\lambda_0$ and work $W$ is measured (see {{< knowl id="work-distribution-nonequilibrium" text="work distribution" >}}), then
$$
\Delta F \;=\; -\beta^{-1}\ln\left\langle e^{-\beta W}\right\rangle,
$$

which is exactly {{< knowl id="jarzynski-equality" text="Jarzynski’s equality" >}} rewritten as a formula for $\Delta F$.

### Crooks crossing / likelihood methods
If both forward and reverse experiments are available, the {{< knowl id="fluctuation-theorem-crooks" text="Crooks fluctuation theorem" >}}
$$
\frac{P_F(W)}{P_R(-W)} \;=\; e^{\beta(W-\Delta F)}
$$
implies:
- **Crossing method:** solve $P_F(W)=P_R(-W)$ to get $W=\Delta F$.
- **Likelihood-based estimation:** infer $\Delta F$ from the full set of observed forward/reverse work samples (statistically efficient in practice).

## Dissipation and information
Define dissipated work $W_{\mathrm{diss}}=W-\Delta F$. Then $\langle W_{\mathrm{diss}}\rangle\ge 0$ (by Jensen) is a nonequilibrium refinement of the {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}} and can be related to a {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} between forward and reverse path ensembles (a path-space irreversibility measure).

## Practical cautions
- The Jarzynski exponential average can be dominated by rare low-work events, leading to slow convergence for finite samples.
- Using reverse data (Crooks-based inference) often reduces variance compared to forward-only estimation.
