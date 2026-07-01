+++
id = "thermodynamics/thermodynamic-limit-pressure-existence"
title = "Existence of the thermodynamic limit of the pressure"
kind = "knowl"
summary = "For translation-invariant short-range lattice systems, the finite-volume pressure (1/|Λ|) log Z_Λ has a limit as Λ grows, typically via subadditivity and Fekete’s lemma."
aliases = ["thermodynamic-limit-pressure-existence", "Existence of the thermodynamic limit of the pressure"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-limit-pressure-existence.md"
+++

## Statement (pressure limit exists)
Let $\Lambda\subset\mathbb Z^d$ be finite volumes, with a translation-invariant finite-range interaction defining a [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]] $H_\Lambda$ and finite-volume partition function (see [[stat-mech-lattice/partition-function-lattice|lattice partition function]])
\[
Z_\Lambda(\beta)=\sum_{\sigma_\Lambda}\exp\big(-\beta H_\Lambda(\sigma_\Lambda)\big).
\]
Define the finite-volume pressure
\[
p_\Lambda(\beta)=\frac{1}{|\Lambda|}\log Z_\Lambda(\beta)
\]
(see [[stat-mech-lattice/pressure-lattice|pressure (lattice)]]).

Assume standard short-range conditions (finite range or sufficiently fast decay, plus stability/regularity) so that boundary effects are at most of order $|\partial\Lambda|$. Then for any sequence of boxes $\Lambda_n\nearrow\mathbb Z^d$ with vanishing boundary-to-volume ratio,
\[
p(\beta)=\lim_{n\to\infty} p_{\Lambda_n}(\beta)
\]
exists and is independent of the chosen sequence. The limit $p(\beta)$ is the thermodynamic pressure.

## Key hypotheses
- Translation invariance and short-range interaction (finite range is the cleanest case).
- Control of boundary terms: $\log Z_{\Lambda\cup\Lambda'}$ differs from $\log Z_\Lambda+\log Z_{\Lambda'}$ by at most $O(|\partial|)$ when $\Lambda,\Lambda'$ are separated/combined appropriately.
- Temperedness/stability ensuring $Z_\Lambda(\beta)<\infty$ for all finite $\Lambda$ and relevant $\beta$.

## Conclusions
- **Existence:** $p(\beta)$ is well-defined as a thermodynamic limit.
- **Shape independence:** the limit does not depend on the particular exhausting sequence of volumes (under vanishing boundary/volume ratio).
- **Foundation for infinite-volume theory:** existence of $p(\beta)$ underlies compactness arguments for infinite-volume Gibbs measures (see [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]]).

## Cross-links to definitions
- Finite-volume objects: [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]], [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]], [[stat-mech-lattice/partition-function-lattice|partition function]], [[stat-mech-lattice/pressure-lattice|pressure]].
- Core tools: [[thermodynamics/subadditivity-partition-function|subadditivity of log partition functions]], [[stat-mech/fekete-lemma|Fekete’s lemma]].
