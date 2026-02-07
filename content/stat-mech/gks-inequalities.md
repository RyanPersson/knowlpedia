---
title: "GKS inequalities (Griffiths–Kelly–Sherman)"
description: "Ferromagnetic Ising correlation inequalities: nonnegativity of truncated correlations and monotonicity/convexity of the finite-volume pressure."
---

## Statement

Consider the finite-volume {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} on a finite $\Lambda$ with spins $\sigma_i\in\{-1,+1\}$ and Hamiltonian
$$
H_\Lambda(\sigma)
= -\sum_{\{i,j\}\subset \Lambda} J_{ij}\,\sigma_i\sigma_j - \sum_{i\in\Lambda} h_i\,\sigma_i,
$$

with **ferromagnetic couplings** $J_{ij}\ge 0$ and **nonnegative fields** $h_i\ge 0$.

Let $Z_\Lambda(J,h)$ be the {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}} and let $\langle\cdot\rangle_\Lambda$ denote expectation under the corresponding {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}.

For $A\subset\Lambda$, write $\sigma_A=\prod_{i\in A}\sigma_i$.

**GKS inequalities.** For all $A,B\subset\Lambda$,
1. (**GKS I**) $\langle \sigma_A\rangle_\Lambda \ge 0$.
2. (**GKS II**) $\langle \sigma_A\sigma_B\rangle_\Lambda - \langle \sigma_A\rangle_\Lambda\,\langle \sigma_B\rangle_\Lambda \ge 0$.

In particular, all covariances of spin monomials are nonnegative.

A useful reformulation is in terms of the finite-volume pressure
$$
p_\Lambda(J,h)=\frac{1}{|\Lambda|}\log Z_\Lambda(J,h)
$$

(see {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}}): derivatives of $\log Z_\Lambda$ with respect to fields/couplings are (truncated) correlations, so GKS II asserts nonnegativity of the corresponding second derivatives.

## Key hypotheses and conclusions

### Hypotheses
- Finite volume $\Lambda$ and Ising spins.
- Ferromagnetic pair couplings $J_{ij}\ge 0$.
- Nonnegative external fields $h_i\ge 0$.
- Gibbs measure context: {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}.

### Conclusions
- **Positivity of correlations:** all moments $\langle\sigma_A\rangle_\Lambda$ are nonnegative.
- **Positive truncated correlations:** $\mathrm{Cov}_\Lambda(\sigma_A,\sigma_B)\ge 0$.
- **Monotonicity/convexity consequences:** since
  - $\partial \log Z_\Lambda/\partial h_i = \langle\sigma_i\rangle_\Lambda$,
  - $\partial^2 \log Z_\Lambda/\partial h_i\partial h_j = \langle\sigma_i\sigma_j\rangle_\Lambda-\langle\sigma_i\rangle_\Lambda\langle\sigma_j\rangle_\Lambda$,
  nonnegativity of truncated correlations implies that magnetizations and many other observables are monotone in fields and that $\log Z_\Lambda$ is convex in the field variables.

## Cross-links and relations

- The pair of inequalities above implies the {{< knowl id="griffiths-inequalities" text="Griffiths inequalities" >}} as a special case (many authors use the names interchangeably for the Ising ferromagnet).
- For increasing observables (not necessarily spin monomials), positivity of correlations can also be obtained from the {{< knowl id="fkg-inequality" text="FKG inequality" >}} when the measure is attractive.

