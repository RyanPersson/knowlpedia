+++
id = "stat-mech/construction-mean-field-variational"
title = "Mean-field variational construction"
kind = "knowl"
summary = "Approximate an interacting Gibbs state by minimizing a free-energy functional over factorized trial measures."
aliases = ["construction-mean-field-variational", "Mean-field variational construction"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-mean-field-variational.md"
+++

Mean-field theory can be formulated cleanly as a constrained minimization of the [[stat-mech/free-energy-statistical|canonical free energy]]. The key idea is to replace the true interacting equilibrium measure by a simpler trial measure (often a product measure) and choose it by a variational principle.

## Variational principle for the canonical free energy
For a Hamiltonian $H$ at [[thermodynamics/inverse-temperature-beta|inverse temperature $\beta$]], the [[stat-mech/canonical-ensemble|canonical ensemble]] has partition function $Z$ and free energy
$$
F(\beta) = -\frac{1}{\beta}\log Z,
\qquad
Z=\sum_{\omega}\exp\!\big(-\beta H(\omega)\big)
$$
(or an integral, for continuous microstates).

Let $q$ be any trial [[probability/probability-measure|probability distribution]] on microstates. Define its entropy as the [[stat-mech/gibbs-entropy-shannon|Gibbs/Shannon entropy]] $S(q)$ and denote by $\langle\cdot\rangle_q$ the [[probability/expectation|expectation]] under $q$. Then one has the exact identity
$$
F(\beta)
={}
\langle H\rangle_q-\frac{1}{\beta}S(q)
-\frac{1}{\beta}D(q\|p),
$$

where $p$ is the true Gibbs distribution and $D(q\|p)$ is the [[probability/relative-entropy-kl-divergence|relative entropy (KL divergence)]]. Since $D(q\|p)\ge 0$ by [[probability/gibbs-inequality-kl|Gibbs' inequality]], this implies the **variational upper bound**
$$
F(\beta)\le \langle H\rangle_q-\frac{1}{\beta}S(q)
\quad\text{for every trial }q,
$$

with equality if and only if $q=p$.

This is an “energy minus temperature times entropy” competition, consistent with [[stat-mech/construction-entropy-maximization-thermal|entropy maximization under constraints]] and with the Legendre-structure viewpoint in [[stat-mech/construction-legendre-s-to-f|constructing $F$ from $S$]].

## Mean-field restriction: product trial measures
The mean-field approximation chooses a restricted family of trial measures, typically factorized:
$$
q(\omega)=\prod_{i\in\Lambda} q_i(\omega_i),
$$
so correlations are neglected at the level of the ansatz. Minimizing the bound
$\langle H\rangle_q-\beta^{-1}S(q)$ over this family yields self-consistency equations for the one-site marginals $q_i$ (or for order parameters such as magnetization).

This mean-field variational viewpoint is closely related to the [[stat-mech/construction-bogoliubov-variational-bound|Bogoliubov variational bound]], which produces the same type of upper bound by comparison with a solvable reference Hamiltonian.

## Example: Curie–Weiss/Ising mean-field equation
For Ising spins $s_i\in\{\pm1\}$ with a mean-field Hamiltonian
$$
H(s)= -\frac{J}{2N}\Big(\sum_{i=1}^N s_i\Big)^2 - h\sum_{i=1}^N s_i,
$$
a translation-invariant product ansatz is characterized by the magnetization
$m=\langle s_i\rangle_q$. The resulting mean-field free-energy density can be written as a function of $m$:
$$
f_{\mathrm{MF}}(m)
={}
-\frac{J}{2}m^2-hm
+\frac{1}{\beta}\left[
\frac{1+m}{2}\log\frac{1+m}{2}
+
\frac{1-m}{2}\log\frac{1-m}{2}
\right].
$$

Stationarity $\partial_m f_{\mathrm{MF}}(m)=0$ yields the self-consistency equation
$$
m=\tanh\!\big(\beta(Jm+h)\big).
$$

## Physical interpretation
Mean-field theory replaces the fluctuating influence of neighbors by an average “molecular field,” while still accounting for thermal disorder through the entropy term. Minimizers of the variational functional approximate equilibrium macrostates; differentiating the resulting approximate free energy yields approximate response functions such as the [[stat-mech/susceptibility-stat-mech|susceptibility]].
