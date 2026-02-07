---
title: "Pressure / log-partition density"
description: "Thermodynamic-limit pressure as volume-normalized log partition function; derivatives generate densities and correlations."
---

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

so that $f$ is the Helmholtz free energy density (compare {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} and {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}).

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
where the right-hand side is an {{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}}.

- **Fluctuations / susceptibilities** are second derivatives, linking $\psi$ to {{< knowl id="variance" section="probability" text="variances" >}} and two-point {{< knowl id="correlation-function-two-point" section="stat-mech" text="correlation functions" >}}.

### Convexity and phase transitions

- As a log-moment generating function, $\psi(\beta,\mathbf{h})$ is convex in $\mathbf{h}$ and typically convex in $\beta$ after appropriate reparameterizations (a convex-analysis perspective connected to {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel duality" >}}).
- Non-analyticity of $\psi$ (or $p$ or $f$) in the thermodynamic limit is a standard signature among {{< knowl id="tfae-phase-transition-indicators" section="stat-mech-lattice" text="phase transition indicators" >}}.

### Prerequisites / cross-links

- {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}, {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}
- {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure (thermodynamics)" >}}, {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}
- {{< knowl id="microcanonical-entropy-density" text="microcanonical entropy density" >}} (via Legendre–Fenchel duality)
