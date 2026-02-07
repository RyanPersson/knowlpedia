---
title: "Negative heat capacity in the microcanonical ensemble"
description: "In the microcanonical ensemble, heat capacity can be negative when the entropy has locally convex curvature; this cannot occur in the canonical ensemble and signals possible ensemble inequivalence."
---

## Prerequisites and notation

- Microcanonical entropy density: {{< knowl id="microcanonical-entropy-density" text="microcanonical entropy density" >}}
- Canonical ensemble comparison: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}
- Thermodynamic stability language: {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}, {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity" >}}
- Inequivalence context: {{< knowl id="ensemble-inequivalence-long-range" text="ensemble inequivalence for long-range systems" >}}

## Extension (and key example mechanism): negative microcanonical heat capacity

### Microcanonical temperature and curvature criterion
Let $S(E)$ be the microcanonical entropy and write $S(E)=N s(u)$ with energy density $u=E/N$. The microcanonical inverse temperature is
$$
\beta(E)=\frac{\partial S}{\partial E}(E),
\qquad T(E)=\frac{1}{\beta(E)}.
$$

Differentiate $T$ with respect to $E$:
$$
\frac{dT}{dE} = -\frac{T^2}{N}\,s''(u).
$$
Therefore the microcanonical heat capacity
$$
C_{\mathrm{mic}}(E)=\left(\frac{dT}{dE}\right)^{-1}
$$
has the sign
$$
C_{\mathrm{mic}}(E) < 0
\quad\Longleftrightarrow\quad
s''(u) > 0.
$$
So **negative heat capacity is equivalent to local convexity of the entropy density**.

### Why canonical heat capacity cannot be negative
In the canonical ensemble, energy fluctuations satisfy
$$
\mathrm{Var}_\beta(E)=\frac{\partial^2}{\partial \beta^2}\log Z(\beta)\ge 0.
$$

Using $U(\beta)=\langle E\rangle_\beta$ and $C_{\mathrm{can}}=\frac{dU}{dT}$, one finds
$$
C_{\mathrm{can}}(\beta)=\beta^2\,\mathrm{Var}_\beta(E)\ge 0.
$$
Hence negative heat capacity is a specifically microcanonical (or finite/nonadditive) phenomenon and is incompatible with canonical stability.

### Interpretation and where it appears
- In additive short-range systems at equilibrium, $s(u)$ is typically concave in the thermodynamic limit, so $C_{\mathrm{mic}}\ge 0$.
- In **nonadditive/long-range** systems, $s(u)$ may be nonconcave, producing $C_{\mathrm{mic}}<0$ and indicating {{< knowl id="ensemble-inequivalence-long-range" text="ensemble inequivalence" >}}.
- In finite systems (e.g., small clusters) interface/surface contributions can also produce effective convex intruders in $S(E)$ over a range of energies.

### Diagnostic use
Observed $C_{\mathrm{mic}}<0$ is a strong diagnostic that:
1. microcanonical and canonical descriptions may disagree over that energy range, and
2. a convex-analytic “envelope” construction is needed to relate entropy to canonical free energy (see {{< knowl id="tfae-legendre-duality-entropy-free-energy" text="Legendre duality" >}}).
