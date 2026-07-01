+++
id = "thermodynamics/isolated-system"
title = "Isolated system"
kind = "knowl"
summary = "A thermodynamic system that exchanges neither matter nor energy with its surroundings."
aliases = ["isolated-system", "Isolated system"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/isolated-system.md"
+++

An **isolated system** is a [[thermodynamics/thermodynamic-system|thermodynamic system]] that exchanges **no matter** and **no energy** with its [[thermodynamics/surroundings-environment|surroundings]] across the [[thermodynamics/system-boundary|boundary]]. Equivalently, there is no heat transfer, no work transfer, and no particle transport through the boundary.

In practice, isolation is an idealization: interactions with the environment are negligible on the timescale of interest.

## Physical interpretation
A typical mental model is a rigid, sealed container with perfectly insulating walls in an otherwise empty environment. The system may still undergo internal changes (chemical reactions, phase changes, mixing, relaxation), but these occur without any net exchange with the surroundings.

Isolation is stronger than simply being [[thermodynamics/closed-system|closed]]: a closed system forbids matter exchange, whereas an isolated system forbids both matter and energy exchange.

## Key thermodynamic relations
- **Conservation of internal energy:** By the [[thermodynamics/first-law-thermodynamics|first law]], with no heat or work transfer,
  $$ dU = 0, $$

  where $U$ is the [[thermodynamics/internal-energy-thermo|internal energy]].
- **Fixed particle number:** No matter crosses the boundary, so in particular
  $$ dN = 0 $$

  for the [[thermodynamics/particle-number|particle number]] $N$ (for a single-component system).
- **Entropy production constraint:** The [[thermodynamics/second-law-thermodynamics|second law]] implies that the [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] $S$ cannot decrease:
  $$ dS \ge 0. $$

  Equality corresponds to reversible evolution (an ideal limiting case); spontaneous internal processes in an isolated system are typically irreversible and yield $dS>0$.

## Equilibrium viewpoint
For an isolated system with fixed constraints (e.g., fixed $U$, $V$, and $N$), [[thermodynamics/thermodynamic-equilibrium|equilibrium]] corresponds to a state that is stable against spontaneous change; thermodynamically, it is characterized by maximal entropy consistent with those constraints.
