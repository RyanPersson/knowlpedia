+++
id = "stat-mech/susceptibility-stat-mech"
title = "Susceptibility"
kind = "knowl"
summary = "Linear response of an order parameter to a conjugate field; equivalently a fluctuation or an integrated connected correlation."
aliases = ["susceptibility-stat-mech", "Susceptibility"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/susceptibility-stat-mech.md"
+++

In statistical mechanics, a **susceptibility** is a linear-response coefficient: it measures how much an [[stat-mech/ensemble-average|ensemble average]] of an observable changes when one perturbs the Hamiltonian by a small conjugate field.

## Definition (response to a field)

Suppose a field $h$ couples linearly to an extensive observable $M$ (e.g. magnetization) through
$$
H_h \;=\; H_0 - h\,M,
$$

with equilibrium described by the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta$. Let $V$ denote volume (or number of sites). The **susceptibility per unit volume** is
$$
\chi
\;=\;
\frac{1}{V}\left.\frac{\partial \langle M\rangle}{\partial h}\right|_{h=0}.
$$
This is the prototypical example; more generally, susceptibilities form a matrix of derivatives relating intensive “fields” to extensive “responses,” mirroring the thermodynamic distinction between [[thermodynamics/intensive-variable|intensive]] and [[thermodynamics/extensive-variable|extensive]] variables.

## Partition-function and fluctuation formulas

Let $Z(\beta,h)$ be the [[stat-mech/partition-function-canonical|canonical partition function]] for $H_h$. Then
$$
\langle M\rangle \;=\; \frac{1}{\beta}\,\frac{\partial}{\partial h}\log Z(\beta,h),
$$
so the susceptibility can be written as a second derivative:
$$
\chi
\;=\;
\frac{1}{\beta V}\left.\frac{\partial^2}{\partial h^2}\log Z(\beta,h)\right|_{h=0}.
$$

Using standard identities (see [[stat-mech/construction-fluctuation-formulas-log-z|fluctuation formulas from $\log Z$]]), one obtains the fluctuation–response relation
$$
\chi
\;=\;
\frac{\beta}{V}\,\Big(\langle M^2\rangle - \langle M\rangle^2\Big)
\;=\;
\frac{\beta}{V}\,\mathrm{Var}(M),
$$

where the variance is the [[stat-mech/variance-observable-ensemble|ensemble variance]] of $M$.

More generally, if $h$ couples to $X$ and one measures the response of $A$, then
$$
\left.\frac{\partial \langle A\rangle}{\partial h}\right|
\;=\;
\beta\,\mathrm{Cov}(A,X),
$$
expressed via the [[stat-mech/covariance-observables-ensemble|ensemble covariance]].

## Correlation-function representation

If $M$ is a spatial sum of local degrees of freedom, for example $M=\sum_x s_x$, then translation invariance gives
$$
\frac{1}{V}\,\mathrm{Var}(M)
\;=\;
\sum_x \langle s_x s_0\rangle_c,
$$
so
$$
\chi \;=\; \beta \sum_x \langle s_x s_0\rangle_c.
$$

Here $\langle s_x s_0\rangle_c$ is the [[stat-mech/connected-correlation-function|connected two-point correlation]]. This identity makes the link to the [[stat-mech/correlation-length|correlation length]] transparent: if connected correlations decay slowly in space, the spatial sum is large, and the susceptibility becomes large.

## Physical interpretation

- **Large susceptibility** means the system is easily polarized/ordered by a small field; microscopically, this corresponds to large fluctuations (large $\mathrm{Var}(M)$) and/or long-range correlations.
- Near continuous phase transitions, the susceptibility often grows strongly or diverges in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], reflecting the growth of correlated domains measured by the correlation length.
