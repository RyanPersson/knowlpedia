+++
id = "stat-mech/ensemble-equivalence-theorem"
title = "Equivalence of microcanonical and canonical ensembles (thermodynamic limit)"
kind = "knowl"
summary = "Under concavity/regularity of the entropy and short-range interactions, microcanonical and canonical ensembles yield the same macroscopic predictions in the thermodynamic limit."
aliases = ["ensemble-equivalence-theorem", "Equivalence of microcanonical and canonical ensembles (thermodynamic limit)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/ensemble-equivalence-theorem.md"
+++

## Statement (ensemble equivalence)
Consider a sequence of $N$-particle (or finite-volume) systems with Hamiltonian (see [[stat-mech/hamiltonian-function-classical|Hamiltonian]] or [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]]). Let
- $\mu^{\text{mc}}_{N,u}$ be the [[stat-mech/microcanonical-measure|microcanonical measure]] at energy density $u$,
- $\mu^{\text{can}}_{N,\beta}$ be the [[stat-mech/canonical-ensemble|canonical ensemble]] at inverse temperature $\beta$.

Assume a thermodynamic entropy density $s(u)$ exists and is concave on the relevant energy range, and that the canonical free-energy potential $\psi(\beta)$ exists and is related to $s$ by Legendre duality (see [[stat-mech/legendre-duality-free-energy-entropy|Legendre duality between free energy and entropy]]).

Then for any “macroscopic” observable $A_N$ whose fluctuations are controlled by the energy (e.g. any local observable in a short-range lattice system), if $u=u(\beta)$ is the equilibrium energy density at $\beta$, one has
\[
\lim_{N\to\infty}\Big(\mathbb E_{\mu^{\text{mc}}_{N,u(\beta)}}[A_N]-\mathbb E_{\mu^{\text{can}}_{N,\beta}}[A_N]\Big)=0,
\]
and both ensembles concentrate on the same set of equilibrium macrostates.

If $s(u)$ is not concave (e.g. due to phase coexistence or long-range interactions), then the ensembles can be nonequivalent: microcanonical equilibrium at a given $u$ need not correspond to any canonical equilibrium at any $\beta$.

## Key hypotheses
- Existence of thermodynamic limits for entropy/free energy (often from subadditivity methods).
- Short-range (or otherwise “well-behaved”) interactions ensuring additivity and concentration.
- Concavity (stability) of the entropy density $s(u)$ on the relevant domain.
- A large-deviation description of the energy or macrovariables (see [[large-deviations/large-deviation-principle|large deviation principle]]).

## Conclusions
- **Same thermodynamics:** equations of state computed from microcanonical or canonical descriptions agree in the thermodynamic limit.
- **Same typical macrostates:** both ensembles concentrate on the same equilibrium set when matched by $u(\beta)$.
- **Inequivalence criterion:** nonconcavity of $s(u)$ signals potential ensemble inequivalence and can correspond to phase transitions.

## Cross-links to definitions
- Ensembles and observables: [[stat-mech/microcanonical-measure|microcanonical measure]], [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/ensemble-average|ensemble average]].
- Entropy/free energy: [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann entropy]], [[stat-mech/free-energy-statistical|statistical free energy]], [[stat-mech/legendre-duality-free-energy-entropy|entropy–free energy duality]].
- Large deviations: [[large-deviations/large-deviation-principle|LDP]], [[stat-mech/large-deviation-equilibrium|large-deviation characterization of equilibrium]].
