---
title: "Thermodynamic Stability"
description: "A stable equilibrium extremizes the appropriate potential and has response functions with the correct sign."
---

## Definition and physical interpretation

A {{< knowl id="thermodynamic-equilibrium" text="thermodynamic equilibrium" >}} state is **stable** if small allowed variations of the state variables do not drive the system away from equilibrium; equivalently, the equilibrium extremum is not merely stationary but locally “curved the right way.”

Which quantity must be extremized depends on the constraints imposed by the surroundings:

- For an isolated system (fixed $U,V,N$), stability means the {{< knowl id="thermodynamic-entropy" text="entropy" >}} $S$ is **maximized** at fixed {{< knowl id="internal-energy-thermo" text="internal energy" >}} $U$, {{< knowl id="volume-thermo" text="volume" >}} $V$, and {{< knowl id="particle-number" text="particle number" >}} $N$ (the {{< knowl id="second-law-thermodynamics" text="second law" >}} viewpoint).

- For a system in contact with a thermal reservoir at fixed $T$ (and fixed $V,N$), stability means the {{< knowl id="helmholtz-free-energy" text="Helmholtz free energy" >}} $F$ is **minimized**.

- For fixed $T$ and {{< knowl id="pressure-thermo" text="pressure" >}} $P$ (and fixed $N$), stability means the {{< knowl id="gibbs-free-energy" text="Gibbs free energy" >}} $G$ is **minimized**.

Mathematically, these stability statements translate into sign conditions on second variations (or Hessians), and are tightly connected to {{< knowl id="convex-function-via-epigraph" section="convex-analysis" text="convexity/concavity" >}} properties of the fundamental relation.

## Key local consequences (signs of response functions)

For a simple compressible single-phase system in stable equilibrium, one expects measurable susceptibilities to have their “physical” sign, for example:

- Positive heat capacities, such as the {{< knowl id="heat-capacity-constant-volume" text="constant-volume heat capacity" >}} $C_V$ and the {{< knowl id="heat-capacity-constant-pressure" text="constant-pressure heat capacity" >}} $C_P$:
  $$
  C_V = \left(\frac{\partial U}{\partial T}\right)_{V,N} > 0,
  \qquad
  C_P = \left(\frac{\partial H}{\partial T}\right)_{P,N} > 0.
  $$

- Mechanical stability against volume fluctuations, often expressed as
  $$
  \left(\frac{\partial P}{\partial V}\right)_{T,N} < 0,
  $$
  which is equivalent to positivity of the {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}}.

These conditions are compactly encoded by the representation-dependent criteria {{< knowl id="entropy-concavity-stability" text="entropy concavity" >}} (in $S(U,V,N)$) and {{< knowl id="energy-convexity-stability" text="energy convexity" >}} (in $U(S,V,N)$). In practice, {{< knowl id="maxwell-relation" text="Maxwell relations" >}} are often used to rewrite stability criteria in terms of experimentally accessible derivatives.
