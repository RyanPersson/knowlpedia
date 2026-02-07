---
title: "Isolated system"
description: "A thermodynamic system that exchanges neither matter nor energy with its surroundings."
---

An **isolated system** is a {{< knowl id="thermodynamic-system" text="thermodynamic system" >}} that exchanges **no matter** and **no energy** with its {{< knowl id="surroundings-environment" text="surroundings" >}} across the {{< knowl id="system-boundary" text="boundary" >}}. Equivalently, there is no heat transfer, no work transfer, and no particle transport through the boundary.

In practice, isolation is an idealization: interactions with the environment are negligible on the timescale of interest.

## Physical interpretation
A typical mental model is a rigid, sealed container with perfectly insulating walls in an otherwise empty environment. The system may still undergo internal changes (chemical reactions, phase changes, mixing, relaxation), but these occur without any net exchange with the surroundings.

Isolation is stronger than simply being {{< knowl id="closed-system" text="closed" >}}: a closed system forbids matter exchange, whereas an isolated system forbids both matter and energy exchange.

## Key thermodynamic relations
- **Conservation of internal energy:** By the {{< knowl id="first-law-thermodynamics" text="first law" >}}, with no heat or work transfer,
  $$ dU = 0, $$

  where $U$ is the {{< knowl id="internal-energy-thermo" text="internal energy" >}}.
- **Fixed particle number:** No matter crosses the boundary, so in particular
  $$ dN = 0 $$

  for the {{< knowl id="particle-number" text="particle number" >}} $N$ (for a single-component system).
- **Entropy production constraint:** The {{< knowl id="second-law-thermodynamics" text="second law" >}} implies that the {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}} $S$ cannot decrease:
  $$ dS \ge 0. $$

  Equality corresponds to reversible evolution (an ideal limiting case); spontaneous internal processes in an isolated system are typically irreversible and yield $dS>0$.

## Equilibrium viewpoint
For an isolated system with fixed constraints (e.g., fixed $U$, $V$, and $N$), {{< knowl id="thermodynamic-equilibrium" text="equilibrium" >}} corresponds to a state that is stable against spontaneous change; thermodynamically, it is characterized by maximal entropy consistent with those constraints.
