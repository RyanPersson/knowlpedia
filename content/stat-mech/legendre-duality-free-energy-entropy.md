---
title: "Legendre duality between free energy and entropy"
description: "In the thermodynamic limit, (dimensionless) canonical free energy is the Legendre–Fenchel transform of microcanonical entropy, with an inverse transform under concavity/regularity."
---

## Statement (entropy–free energy duality)
Let $s(u)$ be the microcanonical entropy density as a function of energy density $u$ (see {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann (microcanonical) entropy" >}}), and let
\[
\psi(\beta)=\lim_{N\to\infty}\frac{1}{N}\log Z_N(\beta)
\]
be the canonical pressure/free-energy potential (from {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}), where $\beta$ is inverse temperature (see {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}).

Under standard short-range assumptions ensuring existence of these limits and a large-deviation principle for the energy, the canonical potential is the Legendre–Fenchel transform of $s$:
\[
\psi(\beta)=\sup_{u}\big(s(u)-\beta u\big).
\]
Moreover, $s$ is the concave Legendre–Fenchel biconjugate of itself, and in particular
\[
s^{**}(u)=\inf_{\beta}\big(\psi(\beta)+\beta u\big),
\]
with $s^{**}=s$ whenever $s$ is concave and upper semicontinuous (see {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}} and {{< knowl id="fenchel-moreau-theorem" section="convex-analysis" text="Fenchel–Moreau theorem" >}}).

## Key hypotheses
- Existence of thermodynamic limits for $s(u)$ and $\psi(\beta)$ (typically short-range, stable interactions).
- A large-deviation principle for the energy under the canonical ensemble (often via {{< knowl id="varadhans-lemma" section="large-deviations" text="Varadhan’s lemma" >}}).
- Regularity ensuring $Z_N(\beta)$ grows exponentially in $N$ and $s(u)$ is well-defined on its domain.

## Conclusions
- **Forward transform:** $\psi(\beta)$ is obtained from $s(u)$ by a Legendre–Fenchel transform (a convex-analysis version of the {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}).
- **Inverse transform (when concave):** if $s$ is concave (as expected from thermodynamic stability), then $s(u)=\inf_\beta(\psi(\beta)+\beta u)$.
- **Thermodynamic identification:** in physical units, the Helmholtz free energy $F(T)$ (see {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}) is related to $\psi(\beta)$ by scaling, and the duality expresses $F$ as the appropriate Legendre transform of entropy/internal energy.

## Cross-links to definitions
- Microcanonical side: {{< knowl id="microcanonical-measure" section="stat-mech" text="microcanonical measure" >}}, {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann entropy" >}}.
- Canonical side: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}.
- Convex analysis: {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}, {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}}, {{< knowl id="fenchel-moreau-theorem" section="convex-analysis" text="Fenchel–Moreau theorem" >}}.

