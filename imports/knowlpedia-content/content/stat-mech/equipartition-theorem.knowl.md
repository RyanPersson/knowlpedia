+++
id = "stat-mech/equipartition-theorem"
title = "Equipartition theorem (classical canonical ensemble)"
kind = "knowl"
summary = "In the classical canonical ensemble, each quadratic degree of freedom contributes (1/2)k_B T to the mean energy."
aliases = ["equipartition-theorem", "Equipartition theorem (classical canonical ensemble)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/equipartition-theorem.md"
+++

## Statement
Consider a classical system with phase space [[stat-mech/phase-space-classical|phase space]] and Hamiltonian [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H(x)$, distributed according to the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta = 1/(k_B T)$, i.e. with density proportional to $e^{-\beta H(x)}$.

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
- Classical setting with [[stat-mech/phase-space-classical|phase space]] and a well-defined [[stat-mech/canonical-ensemble|canonical ensemble]].
- The coordinate $y$ appears quadratically and the corresponding Gaussian integral is integrable (growth/decay ensures boundary terms vanish).
- Differentiation/integration steps are justified (e.g., dominated convergence).

## Conclusion
- For each quadratic degree of freedom, the mean energy contribution is $\frac{1}{2}k_B T$.
- Summing over $m$ independent quadratic terms gives a contribution $\frac{m}{2}k_B T$ to the average internal energy (compare [[thermodynamics/internal-energy-thermo|internal energy]] and [[thermodynamics/temperature-thermo|temperature]]).

## Cross-links to definitions
- [[stat-mech/canonical-ensemble|Canonical ensemble]], [[stat-mech/ensemble-average|ensemble average]]
- [[stat-mech/partition-function-canonical|canonical partition function]]
- [[thermodynamics/temperature-thermo|thermodynamic temperature]]
