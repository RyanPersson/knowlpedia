+++
id = "stat-mech/pressure-log-partition-density"
title = "Pressure / log-partition density"
kind = "knowl"
summary = "Thermodynamic-limit pressure as volume-normalized log partition function; derivatives generate densities and correlations."
aliases = ["pressure-log-partition-density", "Pressure / log-partition density"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/pressure-log-partition-density.md"
+++

## Extension: pressure as a thermodynamic-limit object

For a finite system in volume $\Lambda$ with canonical partition function $Z_\Lambda(\beta,\mathbf{h})$ (possibly including external fields/couplings $\mathbf{h}$), define the **log-partition density**
$$
\psi_\Lambda(\beta,\mathbf{h})=\frac{1}{|\Lambda|}\log Z_\Lambda(\beta,\mathbf{h}),
\qquad
\psi(\beta,\mathbf{h})=\lim_{\Lambda\uparrow\infty}\psi_\Lambda(\beta,\mathbf{h}),
$$
when the limit exists.

In thermodynamic language, the **pressure** is typically
$$
p(\beta,\mathbf{h})=\frac{1}{\beta}\,\psi(\beta,\mathbf{h}),
\qquad
f(\beta,\mathbf{h})=-\frac{1}{\beta}\,\psi(\beta,\mathbf{h}),
$$

so that $f$ is the Helmholtz free energy density (compare [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] and [[stat-mech/free-energy-statistical|statistical free energy]]).

### Why it matters: generating thermodynamics by differentiation

When differentiation under the limit is justified, derivatives of $\psi$ produce macroscopic observables:

- **Energy density**
$$
u(\beta,\mathbf{h})=-\partial_\beta \psi(\beta,\mathbf{h}).
$$
- **Field-conjugate densities** (schematically)
$$
\partial_{h_i}\psi(\beta,\mathbf{h})=\langle O_i\rangle_{\beta,\mathbf{h}},
$$
where the right-hand side is an [[stat-mech/ensemble-average|ensemble average]].

- **Fluctuations / susceptibilities** are second derivatives, linking $\psi$ to [[probability/variance|variances]] and two-point [[stat-mech/correlation-function-two-point|correlation functions]].

### Convexity and phase transitions

- As a log-moment generating function, $\psi(\beta,\mathbf{h})$ is convex in $\mathbf{h}$ and typically convex in $\beta$ after appropriate reparameterizations (a convex-analysis perspective connected to [[convex-analysis/convex-conjugate-fenchel|Fenchel duality]]).
- Non-analyticity of $\psi$ (or $p$ or $f$) in the thermodynamic limit is a standard signature among [[stat-mech-lattice/tfae-phase-transition-indicators|phase transition indicators]].

### Prerequisites / cross-links

- [[stat-mech/partition-function-canonical|canonical partition function]], [[stat-mech/canonical-ensemble|canonical ensemble]]
- [[thermodynamics/pressure-thermo|pressure (thermodynamics)]], [[thermodynamics/thermodynamic-stability|thermodynamic stability]]
- [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]] (via Legendre–Fenchel duality)
