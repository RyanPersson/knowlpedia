---
title: "Hamiltonian function (classical)"
description: "The total energy function on phase space that generates time evolution in Hamiltonian mechanics."
---

For a classical mechanical system with phase space coordinates $(q, p) = (q_1, \ldots, q_n, p_1, \ldots, p_n)$, the **Hamiltonian** is a function
$$
H: \Gamma \to \mathbb{R}, \qquad (q, p) \mapsto H(q, p)
$$

that gives the total energy of the system and determines its time evolution via Hamilton's equations:
$$
\dot{q}_i = \frac{\partial H}{\partial p_i}, \qquad \dot{p}_i = -\frac{\partial H}{\partial q_i}.
$$

## Typical form

For many systems (e.g., particles in a potential), the Hamiltonian splits into kinetic and potential energy:
$$
H(q, p) = T(p) + V(q) = \sum_{i=1}^n \frac{p_i^2}{2m_i} + V(q_1, \ldots, q_n).
$$

## Role in statistical mechanics

In the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}, the equilibrium probability density on {{< knowl id="phase-space-classical" text="phase space" >}} is
$$
\rho(q, p) = \frac{1}{Z} e^{-\beta H(q, p)},
$$

where $\beta = 1/(k_B T)$ is the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} and $Z$ is the {{< knowl id="partition-function-canonical" text="partition function" >}}.
