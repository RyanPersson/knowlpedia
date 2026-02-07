---
title: "Positivity of $C_V$ from thermodynamic stability"
description: "Thermodynamic stability implies the isochoric heat capacity is nonnegative (and typically positive away from singular points)."
---

## Statement

For a stable equilibrium thermodynamic system, the {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="constant-volume heat capacity" >}} satisfies
$$
C_V \ge 0
$$

(at fixed $V$ and fixed composition, e.g. fixed $N$). Equivalently, at fixed $V,N$ the temperature is a nondecreasing function of entropy, and entropy is a nondecreasing function of temperature.

## Key hypotheses

A convenient set of sufficient hypotheses is:

- The system is in {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}} and admits a smooth fundamental relation either as
  - energy representation $U=U(S,V,N)$ ({{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} as a function of {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}), or
  - entropy representation $S=S(U,V,N)$.
- Thermodynamic stability in the usual sense (see {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}), e.g.
  - $U(S,V,N)$ is convex in $S$ at fixed $V,N$, or equivalently
  - $S(U,V,N)$ is concave in $U$ at fixed $V,N$.
- Temperature $T>0$ in the region of interest (see {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}).

## Key conclusions

- The heat capacity at constant volume is nonnegative:
  $$
  C_V = \left(\frac{\partial U}{\partial T}\right)_{V,N}
      = T\left(\frac{\partial S}{\partial T}\right)_{V,N}
      \ge 0.
  $$

- If stability is strict (strict convexity/concavity), then $C_V>0$ and $T(S)$ is strictly increasing at fixed $V,N$.
- Vanishing curvature can lead to $C_V$ diverging (a common signature near criticality), consistent with $C_V\ge 0$.

## Cross-links to definitions

- {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="$C_V$ (constant-volume heat capacity)" >}}
- {{< knowl id="thermodynamic-stability" section="thermodynamics" text="thermodynamic stability" >}}
- {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}, {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}

