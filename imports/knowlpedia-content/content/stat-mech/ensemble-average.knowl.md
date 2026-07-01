+++
id = "stat-mech/ensemble-average"
title = "Ensemble average"
kind = "knowl"
summary = "The predicted equilibrium value of an observable: its expectation with respect to the ensemble probability measure."
aliases = ["ensemble-average", "Ensemble average"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/ensemble-average.md"
+++

**Definition.**
An **observable** is a function $A$ of the [[stat-mech/microstate-classical|microstate]] (classically, a function on [[stat-mech/phase-space-classical|phase space]]; on a discrete state space, a function on the set of states). Given an ensemble described by a [[probability/probability-measure|probability measure]] $P$ on microstates, the **ensemble average** of $A$ is the [[probability/expectation|expectation]]
$$
\langle A\rangle = \int A(x)\,dP(x).
$$

If $P$ has a density $\rho(x)$ with respect to the [[stat-mech/phase-space-volume-element|phase-space volume element]] $d\Gamma$, then
$$
\langle A\rangle = \int A(x)\,\rho(x)\,d\Gamma(x),
\qquad \int \rho\,d\Gamma = 1.
$$

For a discrete ensemble with probabilities $\{p_i\}$, this is $\langle A\rangle=\sum_i A_i p_i$.

**Canonical and microcanonical cases.**
- In the [[stat-mech/canonical-ensemble|canonical ensemble]], $\rho_\beta(x)=e^{-\beta H(x)}/Z$ where $H$ is the [[stat-mech/hamiltonian-function-classical|Hamiltonian]] and $Z$ is the [[stat-mech/partition-function-canonical|partition function]]. Then $\langle H\rangle$ is the internal energy predicted at temperature $T$.
- In the [[stat-mech/microcanonical-measure|microcanonical ensemble]], $P$ is (approximately) uniform on the [[stat-mech/microcanonical-shell|energy shell]], so $\langle A\rangle$ is the phase-space average of $A$ over that constraint surface.

**Physical interpretation.**
$\langle A\rangle$ is the equilibrium prediction for repeated sampling of the system under the macroscopic constraints defining the ensemble. In many-body systems, large-$N$ behavior often makes $\langle A\rangle$ representative of typical outcomes (self-averaging), and different ensembles can give the same limit for suitable observables (equivalence of ensembles).

**Fluctuations around the mean.**
Once $\langle A\rangle$ is defined, fluctuations are quantified by the [[stat-mech/variance-observable-ensemble|variance]]
$$
\mathrm{Var}(A)=\langle (A-\langle A\rangle)^2\rangle,
$$

and for two observables $A,B$ by the [[stat-mech/covariance-observables-ensemble|covariance]]
$$
\mathrm{Cov}(A,B)=\langle (A-\langle A\rangle)(B-\langle B\rangle)\rangle.
$$

These are organized systematically by [[stat-mech/fluctuation-observable|fluctuation formulas]] and by cumulant identities derived from $\ln Z$ (or $\ln \Xi$) in [[stat-mech/construction-fluctuation-formulas-log-z|fluctuations from log Z]].
