+++
id = "stat-mech/tfae-legendre-duality-entropy-free-energy"
title = "TFAE: Legendre Duality Between Entropy and Free Energy"
kind = "knowl"
summary = "Equivalent formulations of thermodynamic Legendre–Fenchel duality and (in)equivalence of microcanonical and canonical ensembles."
aliases = ["tfae-legendre-duality-entropy-free-energy", "TFAE: Legendre Duality Between Entropy and Free Energy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/tfae-legendre-duality-entropy-free-energy.md"
+++

Work in the thermodynamic limit for a sequence of finite systems (classical or lattice) where both a microcanonical entropy density and a canonical log-partition density exist:

- Microcanonical entropy density $s(u)$ (see [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]]).
- Canonical pressure / log-partition density $p(\beta)$ (see [[stat-mech/pressure-log-partition-density|pressure (log-partition) density]]) for inverse temperature $\beta$ (see [[stat-mech/canonical-ensemble|canonical ensemble]]).

The following are equivalent ways to state “entropy–free energy Legendre duality holds without loss,” i.e. the canonical and microcanonical descriptions match at the level of equilibrium thermodynamics.

1. **Legendre–Fenchel transform from entropy to pressure.**
   The canonical pressure is the Legendre–Fenchel transform of $s$:
   $$
   p(\beta) = \sup_{u}\,\{ s(u) - \beta u \}.
   $$

2. **Biconjugacy from pressure back to entropy (no concavity defect).**
   The entropy is recovered exactly from $p$ by the dual transform:
   $$
   s(u) = \inf_{\beta}\,\{ p(\beta) + \beta u \}.
   $$

   Equivalently, $s$ equals its concave upper-semicontinuous envelope (it has no “nonconcave” regions).

3. **Unique saddle point / matching equations of state.**
   For each $\beta$ in the region of interest, the supremum in
   $p(\beta)=\sup_{u}\{s(u)-\beta u\}$ is attained at a unique $u_\beta$, and the duality relation holds:
   $$
   \beta \in \partial s(u_\beta),
   $$

   where $\partial s$ denotes the subgradient (singleton if $s$ is differentiable).
   In differentiable regions this becomes $\beta = s'(u_\beta)$.

4. **Differentiability of pressure and a unique energy density.**
   The pressure $p(\beta)$ is differentiable at $\beta$ and
   $$
   -p'(\beta) = u_\beta,
   $$

   meaning the canonical ensemble has a unique thermodynamic energy density at $\beta$.
   Non-differentiability of $p$ corresponds to a nontrivial subgradient and (typically) coexistence.

5. **Ensemble equivalence at the level of equilibrium macrostates.**
   The set of equilibrium macrostates selected by the microcanonical ensemble at energy $u_\beta$ coincides with the set selected by the canonical ensemble at inverse temperature $\beta$ (see [[stat-mech/ensemble-average|ensemble averages]]).
   Failure of this equivalence is captured by [[stat-mech/ensemble-equivalence-breakdown|ensemble equivalence breakdown]] and often appears in [[stat-mech/ensemble-inequivalence-long-range|long-range systems]].

6. **Large-deviation characterization of energy fluctuations.**
   Under the canonical ensemble at $\beta$, the empirical energy density satisfies a [[large-deviations/large-deviation-principle|large deviation principle]] with good rate function
   $$
   I_\beta(u) = \beta u - s(u) + p(\beta),
   $$

   and $I_\beta$ has a unique minimizer at $u=u_\beta$.
   This is the probabilistic expression of “canonical energy concentrates at the Legendre-dual point.”

Prerequisites and context: [[convex-analysis/convex-conjugate-fenchel|Fenchel (convex conjugate)]], [[convex-analysis/legendre-transform|Legendre transform]], [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]], [[stat-mech/pressure-log-partition-density|pressure (log-partition) density]], [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/partition-function-canonical|canonical partition function]].
