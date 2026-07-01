+++
id = "stat-mech/kosterlitz-thouless-theorem"
title = "Kosterlitz–Thouless theorem (2D XY transition via vortex unbinding)"
kind = "knowl"
summary = "In the 2D XY model, a topological transition separates an exponential-correlation phase from a quasi-long-range ordered phase with power-law correlations and a universal stiffness jump."
aliases = ["kosterlitz-thouless-theorem", "Kosterlitz–Thouless theorem (2D XY transition via vortex unbinding)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/kosterlitz-thouless-theorem.md"
+++

## Context
The 2D XY model has a continuous $U(1)$ symmetry (see [[stat-mech/continuous-symmetry-on-spins|continuous symmetry]]), so by the [[stat-mech/mermin-wagner-theorem|Mermin–Wagner theorem]] it cannot have conventional spontaneous magnetization at $T>0$. Nevertheless, it exhibits a genuine phase transition of *topological* character, driven by vortices (see [[stat-mech/topological-defect-vortex|vortices as topological defects]]).

A standard nearest-neighbor XY Hamiltonian on the 2D square lattice is
$$
H(\theta)= -J\sum_{\langle i,j\rangle}\cos(\theta_i-\theta_j),
\qquad \theta_i\in[0,2\pi),
$$
with equilibrium described by a finite-volume Gibbs measure (see [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]]) and its infinite-volume limits (see [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measure]]).

## Theorem (Kosterlitz–Thouless; standard qualitative conclusions)
There exists a critical temperature $T_{KT}>0$ such that:

1. **High-temperature phase ($T>T_{KT}$):** correlations decay exponentially, i.e. there is a finite [[stat-mech/correlation-length|correlation length]] $\xi(T)<\infty$ with
   $$
   \langle e^{i(\theta_0-\theta_x)}\rangle \approx e^{-|x|/\xi(T)}.
   $$

2. **Low-temperature phase ($0<T<T_{KT}$):** there is **quasi-long-range order**: correlations decay as a power law,
   $$
   \langle e^{i(\theta_0-\theta_x)}\rangle \approx |x|^{-\eta(T)},
   \qquad \eta(T)\in(0,1/4],
   $$

   so the [[stat-mech/correlation-function-two-point|two-point function]] decays slowly but still tends to $0$ as $|x|\to\infty$ (consistent with Mermin–Wagner).

3. **Topological mechanism:** at $T_{KT}$, vortex–antivortex pairs unbind (see [[stat-mech/topological-defect-vortex|vortex unbinding picture]]), producing a transition without a conventional symmetry-breaking order parameter.

4. **Characteristic singularities:** the correlation length diverges with an essential singularity as $T\downarrow T_{KT}$ from above,
   $$
   \xi(T)\sim \exp\!\left(\frac{b}{\sqrt{T-T_{KT}}}\right)
   \quad (T\downarrow T_{KT}),
   $$

   for some $b>0$ (model-dependent).

5. **Universal jump (stiffness/helicity modulus):** the spin-wave stiffness drops discontinuously at $T_{KT}$, with the universal value
   $$
   \Upsilon(T_{KT}^-)=\frac{2}{\pi}T_{KT},
   $$

   where $\Upsilon$ is the helicity modulus (an equilibrium linear response quantity related to [[stat-mech/fluctuation-dissipation-theorem|fluctuation–dissipation]] ideas).

## Connections and interpretations
- This theorem is the mathematical backbone of the [[stat-mech/kosterlitz-thouless-transition|Kosterlitz–Thouless transition]] concept and motivates renormalization ideas (see [[stat-mech/renormalization-group-transformation|renormalization group transformations]], [[stat-mech/rg-fixed-point|RG fixed points]]).
- The transition is a central example where symmetry-based order parameters fail, but topology and defects govern phases.

## Prerequisites and connections (cross-links)
- Equilibrium and ensembles: [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|partition function]], [[stat-mech/ensemble-average|ensemble averages]].
- Low-dimensional constraints: [[stat-mech/mermin-wagner-theorem|Mermin–Wagner theorem]].
- Phase diagnostics: [[stat-mech-lattice/tfae-phase-transition-indicators|equivalent phase-transition indicators]], [[stat-mech/structure-factor|structure factor]].
