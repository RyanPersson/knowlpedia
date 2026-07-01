+++
id = "stat-mech/kosterlitz-thouless-transition"
title = "Kosterlitz–Thouless (BKT) transition"
kind = "knowl"
summary = "A 2D topological phase transition driven by vortex unbinding, featuring quasi-long-range order and an essential singularity in the correlation length."
aliases = ["kosterlitz-thouless-transition", "Kosterlitz–Thouless (BKT) transition"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/kosterlitz-thouless-transition.md"
+++

## Definition (BKT transition)
A **Kosterlitz–Thouless** (also called **Berezinskii–Kosterlitz–Thouless**, BKT) transition is a phase transition in two-dimensional systems with a continuous $U(1)$-type order parameter (e.g., the 2D XY model) in which:
- there is **no conventional long-range order** at any positive temperature,
- the low-temperature phase exhibits **quasi-long-range order** with algebraic decay of correlations,
- the high-temperature phase exhibits **exponential decay** of correlations,
- the transition is driven by the **unbinding of vortex–antivortex pairs** (topological defects).

## Hallmark features
### Correlation decay regimes
Let $G(r)=\langle e^{i(\theta(r)-\theta(0))}\rangle$ denote the two-point function in an angle representation.
- Low temperature ($T<T_c$):
  $$
  G(r)\sim r^{-\eta(T)} \quad \text{(algebraic decay).}
  $$

- High temperature ($T>T_c$):
  $$
  G(r)\sim e^{-r/\xi(T)} \quad \text{(exponential decay).}
  $$

### Essential singularity of the correlation length
As $T\downarrow T_c$ from above, the correlation length diverges faster than any power law:
$$
\xi(T) \sim \exp\!\left(\frac{b}{\sqrt{T-T_c}}\right),
$$

for a nonuniversal constant $b>0$ (model-dependent).

### Universal jump (stiffness / helicity modulus)
In the 2D XY model, the superfluid stiffness (helicity modulus) $\Upsilon(T)$ exhibits a universal jump at $T_c$:
$$
\Upsilon(T_c^-)=\frac{2T_c}{\pi}.
$$

(Precise definitions depend on boundary conditions and how $\Upsilon$ is measured/defined.)

## RG perspective (brief)
The BKT transition is associated with an RG flow in a two-parameter space (often expressed in terms of a stiffness and a vortex fugacity), featuring:
- a low-temperature line of fixed points (power-law phase),
- a separatrix ending at the transition,
- flow to a disordered phase when vortices proliferate.

## Prerequisites / cross-links
- [[stat-mech/topological-defect-vortex|vortices as topological defects]]
- [[stat-mech/kosterlitz-thouless-theorem|Kosterlitz–Thouless theorem (rigorous results)]]
- [[stat-mech/mermin-wagner-theorem|Mermin–Wagner theorem]]
- [[stat-mech/continuous-symmetry-on-spins|continuous symmetries on spins]]
- [[stat-mech/correlation-length|correlation length]]
- [[stat-mech/correlation-function-two-point|two-point correlation function]]
