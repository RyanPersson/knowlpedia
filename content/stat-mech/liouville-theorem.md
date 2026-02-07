---
title: "Liouville theorem (invariance of phase-space volume)"
description: "Hamiltonian time evolution preserves phase-space volume; equivalently, the Liouville measure dq dp is invariant under the Hamiltonian flow."
---

## Statement
Let $\Gamma$ be the classical {{< knowl id="phase-space-classical" section="stat-mech" text="phase space" >}} with canonical coordinates $(q,p)$ and let $H(q,p)$ be a smooth {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="Hamiltonian function" >}} generating Hamilton’s equations:
$$
\dot q = \frac{\partial H}{\partial p},\qquad
\dot p = -\frac{\partial H}{\partial q}.
$$

Let $\Phi^t:\Gamma\to\Gamma$ be the associated flow map. Then **Liouville’s theorem** states that the standard phase-space volume measure (Liouville measure) is invariant:
$$
\text{Vol}(\Phi^t(A))=\text{Vol}(A)
$$

for every measurable set $A\subset\Gamma$ and all $t$ for which the flow exists. Equivalently, the Jacobian determinant satisfies
$$
\det(D\Phi^t)=1,
$$
and the phase-space divergence of the Hamiltonian vector field is zero.

## Key hypotheses
- Classical Hamiltonian dynamics on $\Gamma$ with sufficiently smooth $H$ so the flow exists and is differentiable.
- Canonical (symplectic) coordinates on phase space.

## Conclusions
- Phase-space volume is conserved under time evolution: Hamiltonian dynamics is incompressible in phase space.
- The induced invariant reference measure underlies equilibrium ensembles; for example, the {{< knowl id="microcanonical-measure" section="stat-mech" text="microcanonical measure" >}} is stationary under Hamiltonian time evolution (assuming energy is conserved and appropriate regularity/ergodic assumptions are treated separately).
## significance/proof
Compute the divergence of the Hamiltonian vector field $(\dot q,\dot p)$:
$$
\nabla\cdot(\dot q,\dot p)
={}
\sum_i \left(\frac{\partial \dot q_i}{\partial q_i} + \frac{\partial \dot p_i}{\partial p_i}\right)
={}
\sum_i \left(\frac{\partial^2 H}{\partial q_i\partial p_i} - \frac{\partial^2 H}{\partial p_i\partial q_i}\right)=0.
$$

Zero divergence implies the Jacobian determinant of the flow is constant in time, and at $t=0$ it equals $1$, hence it is $1$ for all $t$.  
In statistical mechanics, this invariance justifies using uniform phase-space weighting (subject to constraints like fixed energy) and supports conservation of ensemble densities under the Liouville equation, connecting microscopic reversibility to macroscopic equilibrium descriptions.
