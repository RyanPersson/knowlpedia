+++
id = "stat-mech/topological-defect-vortex"
title = "Topological defect: vortex"
kind = "knowl"
summary = "A point defect in a 2D U(1) order parameter field characterized by an integer winding number; central to BKT physics."
aliases = ["topological-defect-vortex", "Topological defect: vortex"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/topological-defect-vortex.md"
+++

## Definition (vortex in 2D U(1) systems)
Consider a two-dimensional system with a $U(1)$ order parameter that can be represented by an angle field $\theta(x)\in \mathbb{R}/2\pi\mathbb{Z}$ (e.g., planar spins $s(x)=(\cos\theta(x),\sin\theta(x))$). A **vortex** is a point defect around which $\theta$ winds nontrivially.

For a closed loop $\gamma$ encircling a defect, the **winding number** (topological charge) is
$$
m = \frac{1}{2\pi}\oint_{\gamma} \nabla\theta \cdot d\ell \in \mathbb{Z}.
$$

- $m=+1$ is a vortex, $m=-1$ an antivortex (conventions may vary).
- The integer quantization comes from $\pi_1(S^1)\cong \mathbb{Z}$.

## Energetics (spin-wave stiffness picture)
In the continuum XY/superfluid effective energy
$$
H[\theta] \approx \frac{J}{2}\int |\nabla\theta(x)|^2\,dx,
$$

a single vortex of charge $m$ in a system of linear size $L$ with microscopic core cutoff $a$ has energy scaling
$$
E_m \approx \pi J m^2 \log\!\left(\frac{L}{a}\right) + E_{\text{core}}.
$$
This logarithmic growth underlies the competition between energy and entropy that drives vortex unbinding at the [[stat-mech/kosterlitz-thouless-transition|BKT transition]].

## Vortex pairs and unbinding
- At low temperature, vortices appear mainly as tightly bound vortex–antivortex pairs, preserving quasi-long-range order.
- At high temperature, unbound vortices proliferate, producing exponential decay of correlations.

## Prerequisites / cross-links
- [[stat-mech/continuous-symmetry-on-spins|continuous symmetries on spin systems]]
- [[stat-mech/kosterlitz-thouless-transition|Kosterlitz–Thouless (BKT) transition]]
- [[stat-mech/kosterlitz-thouless-theorem|Kosterlitz–Thouless theorem]]
- [[stat-mech/mermin-wagner-theorem|Mermin–Wagner theorem]]
