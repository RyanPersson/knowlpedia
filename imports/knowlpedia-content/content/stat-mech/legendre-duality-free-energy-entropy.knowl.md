+++
id = "stat-mech/legendre-duality-free-energy-entropy"
title = "Legendre duality between free energy and entropy"
kind = "knowl"
summary = "In the thermodynamic limit, (dimensionless) canonical free energy is the Legendre–Fenchel transform of microcanonical entropy, with an inverse transform under concavity/regularity."
aliases = ["legendre-duality-free-energy-entropy", "Legendre duality between free energy and entropy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/legendre-duality-free-energy-entropy.md"
+++

## Statement (entropy–free energy duality)
Let $s(u)$ be the microcanonical entropy density as a function of energy density $u$ (see [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann (microcanonical) entropy]]), and let
\[
\psi(\beta)=\lim_{N\to\infty}\frac{1}{N}\log Z_N(\beta)
\]
be the canonical pressure/free-energy potential (from [[stat-mech/partition-function-canonical|canonical partition function]]), where $\beta$ is inverse temperature (see [[thermodynamics/temperature-thermo|temperature]]).

Under standard short-range assumptions ensuring existence of these limits and a large-deviation principle for the energy, the canonical potential is the Legendre–Fenchel transform of $s$:
\[
\psi(\beta)=\sup_{u}\big(s(u)-\beta u\big).
\]
Moreover, $s$ is the concave Legendre–Fenchel biconjugate of itself, and in particular
\[
s^{**}(u)=\inf_{\beta}\big(\psi(\beta)+\beta u\big),
\]
with $s^{**}=s$ whenever $s$ is concave and upper semicontinuous (see [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]] and [[convex-analysis/fenchel-moreau-theorem|Fenchel–Moreau theorem]]).

## Key hypotheses
- Existence of thermodynamic limits for $s(u)$ and $\psi(\beta)$ (typically short-range, stable interactions).
- A large-deviation principle for the energy under the canonical ensemble (often via [[large-deviations/varadhans-lemma|Varadhan’s lemma]]).
- Regularity ensuring $Z_N(\beta)$ grows exponentially in $N$ and $s(u)$ is well-defined on its domain.

## Conclusions
- **Forward transform:** $\psi(\beta)$ is obtained from $s(u)$ by a Legendre–Fenchel transform (a convex-analysis version of the [[convex-analysis/legendre-transform|Legendre transform]]).
- **Inverse transform (when concave):** if $s$ is concave (as expected from thermodynamic stability), then $s(u)=\inf_\beta(\psi(\beta)+\beta u)$.
- **Thermodynamic identification:** in physical units, the Helmholtz free energy $F(T)$ (see [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]]) is related to $\psi(\beta)$ by scaling, and the duality expresses $F$ as the appropriate Legendre transform of entropy/internal energy.

## Cross-links to definitions
- Microcanonical side: [[stat-mech/microcanonical-measure|microcanonical measure]], [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann entropy]].
- Canonical side: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|partition function]], [[stat-mech/free-energy-statistical|statistical free energy]].
- Convex analysis: [[convex-analysis/legendre-transform|Legendre transform]], [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugate]], [[convex-analysis/fenchel-moreau-theorem|Fenchel–Moreau theorem]].
