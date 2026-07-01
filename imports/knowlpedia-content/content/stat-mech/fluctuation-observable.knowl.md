+++
id = "stat-mech/fluctuation-observable"
title = "Fluctuation of an Observable"
kind = "knowl"
summary = "The centered (mean-zero) version of an observable, A − ⟨A⟩, whose moments encode thermal noise and correlations."
aliases = ["fluctuation-observable", "Fluctuation of an Observable"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/fluctuation-observable.md"
+++

In statistical mechanics, an **observable** $A$ assigns a numerical value to each [[stat-mech/microstate-classical|microstate]] (for a classical system, a point in [[stat-mech/phase-space-classical|phase space]]). Once an ensemble measure is chosen (e.g. [[stat-mech/canonical-ensemble|canonical ensemble]] or [[stat-mech/microcanonical-measure|microcanonical measure]]), $A$ becomes a random variable in the probabilistic sense (compare [[probability/random-variable|random variable]]), and its **ensemble mean** is [[stat-mech/ensemble-average|⟨A⟩]].

The **fluctuation** (or **centered observable**) associated with $A$ is
$$
\delta A \;:=\; A - \langle A\rangle.
$$
This is an observable with zero ensemble mean:
$$
\langle \delta A\rangle = 0.
$$

If $A_x$ is a *local* observable (e.g. a spin or density at site/position $x$), then its fluctuation is $\delta A_x = A_x - \langle A_x\rangle$. Fluctuations are the basic objects behind [[stat-mech/variance-observable-ensemble|variances]], [[stat-mech/covariance-observables-ensemble|covariances]], and [[stat-mech/connected-correlation-function|connected correlation functions]].

## Key formulas
- **Variance (typical size of fluctuations):**
  $$
  \mathrm{Var}(A) \;=\; \langle (\delta A)^2\rangle.
  $$
  This is the content of [[stat-mech/variance-observable-ensemble|ensemble variance]].

- **Covariance (joint fluctuations):**
  $$
  \mathrm{Cov}(A,B) \;=\; \langle \delta A\,\delta B\rangle,
  $$
  as in [[stat-mech/covariance-observables-ensemble|ensemble covariance]].

- **Connected two-point correlations (spatial correlations of fluctuations):** for local observables $A_x,B_y$,
  $$
  \langle A_x B_y\rangle_c \;=\; \langle \delta A_x\,\delta B_y\rangle,
  $$
  which is the two-point case of [[stat-mech/connected-correlation-function|connected correlations]] and relates to the [[stat-mech/correlation-function-two-point|two-point correlation function]].

## Physical interpretation
$\delta A$ measures how much $A$ typically deviates from its thermodynamic “typical value” $\langle A\rangle$ under the chosen ensemble. In a finite system these deviations are unavoidable (thermal noise). In many systems and for many *self-averaging* observables, relative fluctuations shrink as system size grows toward the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], which is why macroscopic [[stat-mech/macrostate|macrostates]] can be stable even though underlying microstates fluctuate.
