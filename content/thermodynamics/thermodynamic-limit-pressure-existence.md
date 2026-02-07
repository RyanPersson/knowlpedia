---
title: "Existence of the thermodynamic limit of the pressure"
description: "For translation-invariant short-range lattice systems, the finite-volume pressure (1/|Λ|) log Z_Λ has a limit as Λ grows, typically via subadditivity and Fekete’s lemma."
---

## Statement (pressure limit exists)
Let $\Lambda\subset\mathbb Z^d$ be finite volumes, with a translation-invariant finite-range interaction defining a {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}} $H_\Lambda$ and finite-volume partition function (see {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="lattice partition function" >}})
\[
Z_\Lambda(\beta)=\sum_{\sigma_\Lambda}\exp\big(-\beta H_\Lambda(\sigma_\Lambda)\big).
\]
Define the finite-volume pressure
\[
p_\Lambda(\beta)=\frac{1}{|\Lambda|}\log Z_\Lambda(\beta)
\]
(see {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure (lattice)" >}}).

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
- **Foundation for infinite-volume theory:** existence of $p(\beta)$ underlies compactness arguments for infinite-volume Gibbs measures (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}}).

## Cross-links to definitions
- Finite-volume objects: {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}, {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}}, {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}}.
- Core tools: {{< knowl id="subadditivity-partition-function" text="subadditivity of log partition functions" >}}, {{< knowl id="fekete-lemma" section="stat-mech" text="Fekete’s lemma" >}}.

