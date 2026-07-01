+++
id = "stat-mech/ensemble-equivalence-breakdown"
title = "Breakdown of ensemble equivalence"
kind = "knowl"
summary = "When microcanonical and canonical ensembles yield different macrostates, typically due to nonconcavity of microcanonical entropy, long-range interactions, or first-order transitions."
aliases = ["ensemble-equivalence-breakdown", "Breakdown of ensemble equivalence"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/ensemble-equivalence-breakdown.md"
+++

“Ensemble equivalence” refers to the fact that different equilibrium ensembles (most commonly microcanonical vs canonical) give the same thermodynamic predictions in the thermodynamic limit. Breakdown means that, for some parameters, they do *not*.

This phenomenon is central in long-range systems and in models where the microcanonical entropy is not concave.

## Microcanonical entropy and canonical free energy

Let $e=E/V$ be energy density.

- The microcanonical entropy density is
$$
s(e) \;=\; \lim_{V\to\infty}\frac{1}{V}\log \Omega_V(E),
\qquad E=Ve,
$$
as in [[stat-mech/microcanonical-entropy-density|microcanonical entropy density]] and [[stat-mech/boltzmann-entropy-microcanonical|Boltzmann (microcanonical) entropy]].

- The canonical free energy density can be written in terms of the canonical partition function $Z_V(\beta)$ (see [[stat-mech/partition-function-canonical|canonical partition function]]):
$$
f(\beta)
\;=\;
-\frac{1}{\beta}\lim_{V\to\infty}\frac{1}{V}\log Z_V(\beta).
$$

These are related by Legendre–Fenchel duality (see [[stat-mech/tfae-legendre-duality-entropy-free-energy|Legendre duality between entropy and free energy]] and [[convex-analysis/convex-conjugate-fenchel|Fenchel conjugates]]):
$$
-\beta f(\beta) \;=\; \sup_{e}\,\bigl(s(e)-\beta e\bigr),
\qquad\text{equivalently}\qquad
f(\beta) \;=\; \inf_{e}\,\bigl(e-\beta^{-1}s(e)\bigr).
$$

## What “equivalence” means (microcanonical vs canonical)

Informally, equivalence holds when:
- the canonical energy concentrates at an energy density $e(\beta)$, and
- the microcanonical equilibrium at $e(\beta)$ yields the same macroscopic observables as the canonical equilibrium at $\beta$.

A clean sufficient condition is concavity of $s(e)$ (plus mild regularity). When $s$ is strictly concave and differentiable, the microcanonical inverse temperature is
$$
\beta \;=\; s'(e),
$$

and the mapping $e \leftrightarrow \beta$ is essentially one-to-one.

## How breakdown happens: nonconcave entropy and “convex intruders”

If $s(e)$ is *not* concave on an interval, then:
- the canonical ensemble only “sees” the concave envelope $s^{**}(e)$ (the biconjugate),
- some energy densities that are admissible microcanonically are not realized canonically as typical energies.

This is one precise sense in which ensembles become inequivalent.

A geometric picture:
- canonical equilibrium selects maximizers of $s(e)-\beta e$,
- if $s$ has a nonconcave region, the maximizer jumps between endpoints of that region as $\beta$ varies, producing phase coexistence and a first-order canonical transition (non-differentiability of $f$).

## Diagnostic: negative microcanonical heat capacity

Working in units where $k_B=1$, set $T=1/\beta$ with $\beta=s'(e)$. Then
$$
\frac{dT}{de} \;=\; -\frac{s''(e)}{[s'(e)]^2},
\qquad
C(e) \;=\; \left(\frac{dT}{de}\right)^{-1}
\;=\;
-\frac{[s'(e)]^2}{s''(e)}.
$$

Therefore:
- if $s''(e)>0$ (a local “convex” region), then $C(e)<0$.

Negative microcanonical heat capacity is incompatible with canonical equilibrium (where energy fluctuations enforce nonnegative heat capacity), and is a standard signature of nonequivalence; see [[stat-mech/microcanonical-negative-heat-capacity|microcanonical negative heat capacity]].

## Typical mechanisms and examples

- Long-range interactions (mean-field-type spin systems, gravitational models) often generate nonconcave $s(e)$; see [[stat-mech/ensemble-inequivalence-long-range|ensemble inequivalence for long-range interactions]].
- Even for short-range models, finite-size systems can show apparent nonequivalence, but in many stable short-range systems equivalence is recovered as $V\to\infty$.

## Prerequisites

- [[stat-mech/microcanonical-entropy-density|Microcanonical entropy density]]
- [[stat-mech/canonical-ensemble|Canonical ensemble]]
- [[stat-mech/partition-function-canonical|Canonical partition function]]
- [[stat-mech/tfae-legendre-duality-entropy-free-energy|Legendre duality: entropy vs free energy]]
- [[convex-analysis/legendre-transform|Legendre transform]]
- [[stat-mech/microcanonical-negative-heat-capacity|Negative heat capacity (microcanonical)]]
