---
title: "Constructing observables from log partition functions"
description: "Ensemble averages and fluctuations are obtained by differentiating the log of the partition function with respect to conjugate parameters."
---

A central reason partition functions are useful is that **derivatives of their logarithms generate equilibrium observables and their fluctuations**. This is the concrete bridge between microscopic definitions (microstates and energies) and macroscopic thermodynamic response functions.

Throughout, expectations are {{< knowl id="ensemble-average" text="ensemble averages" >}} taken in the relevant ensemble.

## Canonical ensemble: derivatives of $\log Z_N$

Let $Z_N(\beta,V)$ be the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} (constructed in {{< knowl id="construction-canonical-partition-function" text="the canonical construction" >}}). Then:

### Energy and energy fluctuations

The mean energy is obtained from
$$
\langle H \rangle \;=\; -\frac{\partial}{\partial \beta}\,\log Z_N(\beta,V).
$$
The energy variance is the second derivative
$$
\mathrm{Var}(H) \;=\; \frac{\partial^2}{\partial \beta^2}\,\log Z_N(\beta,V),
$$

which is the basic instance of the general principle that second derivatives of $\log Z$ give {{< knowl id="variance-observable-ensemble" text="variances" >}}.

This links directly to heat capacity: at fixed $(N,V)$,
$$
C_V \;=\; \left(\frac{\partial \langle H\rangle}{\partial T}\right)_{N,V}
\;=\; k_B \beta^2\, \mathrm{Var}(H),
$$
connecting the fluctuation formula to {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}} and the {{< knowl id="specific-heat-fluctuation" text="specific-heat fluctuation relation" >}}.

### Conjugate observables via parameter derivatives

Suppose the Hamiltonian depends on an external parameter $\lambda$ (e.g. a field strength), $H=H_\lambda$. Then
$$
\frac{\partial}{\partial \lambda}\,\log Z_N(\beta,V;\lambda)
\;=\;
-\beta\,\Bigl\langle \frac{\partial H_\lambda}{\partial \lambda}\Bigr\rangle.
$$

Thus the observable conjugate to $\lambda$ is obtained as a derivative of $\log Z$.

## Grand canonical ensemble: derivatives of $\log \Xi$

Let $\Xi(\beta,\mu,V)$ be the {{< knowl id="grand-partition-function" text="grand partition function" >}} (constructed in {{< knowl id="construction-grand-canonical-partition-function" text="the grand-canonical construction" >}}). Then:

### Mean particle number and its fluctuations

The mean particle number is
$$
\langle N \rangle \;=\; \frac{\partial}{\partial (\beta\mu)}\,\log \Xi(\beta,\mu,V).
$$
The particle-number variance is
$$
\mathrm{Var}(N) \;=\; \frac{\partial^2}{\partial (\beta\mu)^2}\,\log \Xi(\beta,\mu,V),
$$
and more generally mixed derivatives give {{< knowl id="covariance-observables-ensemble" text="covariances" >}}.

### Energy–number covariance

Because $\Xi$ depends on both $\beta$ and $\beta\mu$, mixed derivatives encode correlations between energy and particle number. A standard example is
$$
\frac{\partial^2}{\partial \beta\,\partial (\beta\mu)} \log \Xi
\;=\;
-\mathrm{Cov}(H,N),
$$

where $\mathrm{Cov}$ is the {{< knowl id="covariance" section="probability" text="covariance" >}} of the joint fluctuations in the grand canonical ensemble.

## Log partition functions as cumulant generators

A useful viewpoint is that $\log Z$ and $\log \Xi$ are **cumulant generating objects** for the observables conjugate to the parameters. This is formalized in constructions like {{< knowl id="construction-cumulant-generating-function" text="cumulant generating functions" >}} and {{< knowl id="construction-connected-correlations-cumulants" text="connected correlations as cumulants" >}}.

## Physical interpretation

- First derivatives of $\log Z$ or $\log \Xi$ give equilibrium “equations of state” (mean values of conserved or conjugate quantities).
- Second derivatives quantify equilibrium fluctuations and linear response (susceptibilities), linking to {{< knowl id="susceptibility-stat-mech" text="susceptibility" >}} and related response coefficients.
- Taking the logarithm is essential: it converts products of partition functions (from composing subsystems) into sums, making derivatives match extensive thermodynamic behavior (see {{< knowl id="construction-free-energy-from-partition" text="free energies from partition functions" >}}).
