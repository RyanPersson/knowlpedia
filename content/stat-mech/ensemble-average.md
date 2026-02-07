---
title: "Ensemble average"
description: "The predicted equilibrium value of an observable: its expectation with respect to the ensemble probability measure."
---

**Definition.**  
An **observable** is a function $A$ of the {{< knowl id="microstate-classical" text="microstate" >}} (classically, a function on {{< knowl id="phase-space-classical" text="phase space" >}}; on a discrete state space, a function on the set of states). Given an ensemble described by a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} $P$ on microstates, the **ensemble average** of $A$ is the {{< knowl id="expectation" section="probability" text="expectation" >}}
$$
\langle A\rangle = \int A(x)\,dP(x).
$$

If $P$ has a density $\rho(x)$ with respect to the {{< knowl id="phase-space-volume-element" text="phase-space volume element" >}} $d\Gamma$, then
$$
\langle A\rangle = \int A(x)\,\rho(x)\,d\Gamma(x),
\qquad \int \rho\,d\Gamma = 1.
$$

For a discrete ensemble with probabilities $\{p_i\}$, this is $\langle A\rangle=\sum_i A_i p_i$.

**Canonical and microcanonical cases.**  
- In the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}, $\rho_\beta(x)=e^{-\beta H(x)}/Z$ where $H$ is the {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} and $Z$ is the {{< knowl id="partition-function-canonical" text="partition function" >}}. Then $\langle H\rangle$ is the internal energy predicted at temperature $T$.  
- In the {{< knowl id="microcanonical-measure" text="microcanonical ensemble" >}}, $P$ is (approximately) uniform on the {{< knowl id="microcanonical-shell" text="energy shell" >}}, so $\langle A\rangle$ is the phase-space average of $A$ over that constraint surface.

**Physical interpretation.**  
$\langle A\rangle$ is the equilibrium prediction for repeated sampling of the system under the macroscopic constraints defining the ensemble. In many-body systems, large-$N$ behavior often makes $\langle A\rangle$ representative of typical outcomes (self-averaging), and different ensembles can give the same limit for suitable observables (equivalence of ensembles).

**Fluctuations around the mean.**  
Once $\langle A\rangle$ is defined, fluctuations are quantified by the {{< knowl id="variance-observable-ensemble" text="variance" >}}
$$
\mathrm{Var}(A)=\langle (A-\langle A\rangle)^2\rangle,
$$

and for two observables $A,B$ by the {{< knowl id="covariance-observables-ensemble" text="covariance" >}}
$$
\mathrm{Cov}(A,B)=\langle (A-\langle A\rangle)(B-\langle B\rangle)\rangle.
$$

These are organized systematically by {{< knowl id="fluctuation-observable" text="fluctuation formulas" >}} and by cumulant identities derived from $\ln Z$ (or $\ln \Xi$) in {{< knowl id="construction-fluctuation-formulas-log-z" text="fluctuations from log Z" >}}.
