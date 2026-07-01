+++
id = "stat-mech/hamiltonian-function-classical"
title = "Hamiltonian function (classical)"
kind = "knowl"
summary = "The total energy function on phase space that generates time evolution in Hamiltonian mechanics."
aliases = ["hamiltonian-function-classical", "Hamiltonian function (classical)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/hamiltonian-function-classical.md"
+++

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

In the [[stat-mech/canonical-ensemble|canonical ensemble]], the equilibrium probability density on [[stat-mech/phase-space-classical|phase space]] is
$$
\rho(q, p) = \frac{1}{Z} e^{-\beta H(q, p)},
$$

where $\beta = 1/(k_B T)$ is the [[thermodynamics/inverse-temperature-beta|inverse temperature]] and $Z$ is the [[stat-mech/partition-function-canonical|partition function]].
