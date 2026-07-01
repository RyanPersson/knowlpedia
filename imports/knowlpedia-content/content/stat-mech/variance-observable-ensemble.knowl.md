+++
id = "stat-mech/variance-observable-ensemble"
title = "Ensemble Variance of an Observable"
kind = "knowl"
summary = "The second central moment ⟨(A−⟨A⟩)²⟩, quantifying the typical size of thermal fluctuations."
aliases = ["variance-observable-ensemble", "Ensemble Variance of an Observable"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/variance-observable-ensemble.md"
+++

Given an observable $A$ and an ensemble (so that [[stat-mech/ensemble-average|⟨·⟩]] is defined), the **variance** is the basic scalar measure of the size of fluctuations. It is the statistical-mechanics specialization of [[probability/variance|variance]].

The **ensemble variance** of $A$ is
$$
\mathrm{Var}(A)
\;:=\;
\left\langle \bigl(A-\langle A\rangle\bigr)^2 \right\rangle
\;=\;
\langle (\delta A)^2\rangle,
$$

where $\delta A$ is the [[stat-mech/fluctuation-observable|fluctuation of the observable]].

Equivalently,
$$
\mathrm{Var}(A) = \langle A^2\rangle - \langle A\rangle^2.
$$

Basic facts (for real-valued $A$):
- $\mathrm{Var}(A)\ge 0$.
- $\mathrm{Var}(A)=0$ iff $A$ is almost surely constant under the ensemble measure (no thermal fluctuations of $A$ in that ensemble).

## Variance from the partition function
In a Gibbs-type ensemble, variances appear as second derivatives of $\log Z$ with respect to parameters coupled to observables; see [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from log Z]] and [[stat-mech/construction-observables-from-log-z|observables from log Z]].

A canonical example is the energy $H$ in the [[stat-mech/canonical-ensemble|canonical ensemble]] with [[stat-mech/partition-function-canonical|partition function]] $Z(\beta)$. Then
$$
\langle H\rangle = -\frac{\partial}{\partial \beta}\log Z(\beta),
\qquad
\mathrm{Var}(H) = \frac{\partial^2}{\partial \beta^2}\log Z(\beta),
$$

where $\beta$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]].

Using $\beta = 1/(k_B T)$ (with [[thermodynamics/boltzmann-constant|Boltzmann constant]] $k_B$ and thermodynamic temperature $T$), one obtains the standard fluctuation relation
$$
\mathrm{Var}(H) = k_B\,T^2\,C_V,
$$

where $C_V$ is the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]]; this is emphasized in [[stat-mech/specific-heat-fluctuation|specific heat from fluctuations]].

## Physical interpretation
- $\mathrm{Var}(A)$ sets the *typical fluctuation scale* of $A$: roughly, $A$ wanders around $\langle A\rangle$ by an amount of order $\sqrt{\mathrm{Var}(A)}$.
- For extensive observables (often scaling like system size), $\mathrm{Var}(A)$ often scales extensively as well, so the *relative* size $\sqrt{\mathrm{Var}(A)}/|\langle A\rangle|$ can shrink with system size, supporting macroscopic reproducibility in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]].
