+++
id = "thermodynamics/thermodynamic-stability"
title = "Thermodynamic Stability"
kind = "knowl"
summary = "A stable equilibrium extremizes the appropriate potential and has response functions with the correct sign."
aliases = ["thermodynamic-stability", "Thermodynamic Stability"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/thermodynamic-stability.md"
+++

## Definition and physical interpretation

A [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] state is **stable** if small allowed variations of the state variables do not drive the system away from equilibrium; equivalently, the equilibrium extremum is not merely stationary but locally “curved the right way.”

Which quantity must be extremized depends on the constraints imposed by the surroundings:

- For an isolated system (fixed $U,V,N$), stability means the [[thermodynamics/thermodynamic-entropy|entropy]] $S$ is **maximized** at fixed [[thermodynamics/internal-energy-thermo|internal energy]] $U$, [[thermodynamics/volume-thermo|volume]] $V$, and [[thermodynamics/particle-number|particle number]] $N$ (the [[thermodynamics/second-law-thermodynamics|second law]] viewpoint).

- For a system in contact with a thermal reservoir at fixed $T$ (and fixed $V,N$), stability means the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F$ is **minimized**.

- For fixed $T$ and [[thermodynamics/pressure-thermo|pressure]] $P$ (and fixed $N$), stability means the [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G$ is **minimized**.

Mathematically, these stability statements translate into sign conditions on second variations (or Hessians), and are tightly connected to [[convex-analysis/convex-function-via-epigraph|convexity/concavity]] properties of the fundamental relation.

## Key local consequences (signs of response functions)

For a simple compressible single-phase system in stable equilibrium, one expects measurable susceptibilities to have their “physical” sign, for example:

- Positive heat capacities, such as the [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]] $C_V$ and the [[thermodynamics/heat-capacity-constant-pressure|constant-pressure heat capacity]] $C_P$:
  $$
  C_V = \left(\frac{\partial U}{\partial T}\right)_{V,N} > 0,
  \qquad
  C_P = \left(\frac{\partial H}{\partial T}\right)_{P,N} > 0.
  $$

- Mechanical stability against volume fluctuations, often expressed as
  $$
  \left(\frac{\partial P}{\partial V}\right)_{T,N} < 0,
  $$
  which is equivalent to positivity of the [[thermodynamics/isothermal-compressibility|isothermal compressibility]].

These conditions are compactly encoded by the representation-dependent criteria [[thermodynamics/entropy-concavity-stability|entropy concavity]] (in $S(U,V,N)$) and [[thermodynamics/energy-convexity-stability|energy convexity]] (in $U(S,V,N)$). In practice, [[thermodynamics/maxwell-relation|Maxwell relations]] are often used to rewrite stability criteria in terms of experimentally accessible derivatives.
