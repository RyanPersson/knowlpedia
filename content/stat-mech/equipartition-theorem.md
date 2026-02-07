---
title: "Equipartition theorem (classical canonical ensemble)"
description: "In the classical canonical ensemble, each quadratic degree of freedom contributes (1/2)k_B T to the mean energy."
---

## Statement
Consider a classical system with phase space {{< knowl id="phase-space-classical" section="stat-mech" text="phase space" >}} and Hamiltonian {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="Hamiltonian" >}} $H(x)$, distributed according to the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at inverse temperature $\beta = 1/(k_B T)$, i.e. with density proportional to $e^{-\beta H(x)}$.

If $H$ contains a term that is quadratic in some coordinate $y$ (a position or momentum component), of the form
- $H(x) = \frac{a}{2} y^2 + H_{\mathrm{rest}}(x)$ with $a>0$ and $H_{\mathrm{rest}}$ independent of $y$,

then the canonical expectation satisfies
$$
\left\langle \frac{a}{2}y^2 \right\rangle_\beta = \frac{1}{2}k_B T.
$$

Equivalently, each independent quadratic term contributes $\frac{1}{2}k_B T$ to the mean energy.

A common general form (under appropriate decay/regularity assumptions) is:
$$
\langle y\,\partial_y H\rangle_\beta = k_B T.
$$

## Key hypotheses
- Classical setting with {{< knowl id="phase-space-classical" section="stat-mech" text="phase space" >}} and a well-defined {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}.
- The coordinate $y$ appears quadratically and the corresponding Gaussian integral is integrable (growth/decay ensures boundary terms vanish).
- Differentiation/integration steps are justified (e.g., dominated convergence).

## Conclusion
- For each quadratic degree of freedom, the mean energy contribution is $\frac{1}{2}k_B T$.
- Summing over $m$ independent quadratic terms gives a contribution $\frac{m}{2}k_B T$ to the average internal energy (compare {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} and {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}).

## Cross-links to definitions
- {{< knowl id="canonical-ensemble" section="stat-mech" text="Canonical ensemble" >}}, {{< knowl id="ensemble-average" section="stat-mech" text="ensemble average" >}}
- {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}
- {{< knowl id="temperature-thermo" section="thermodynamics" text="thermodynamic temperature" >}}

