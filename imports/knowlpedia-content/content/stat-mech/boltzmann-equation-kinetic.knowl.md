+++
id = "stat-mech/boltzmann-equation-kinetic"
title = "Boltzmann equation (kinetic theory)"
kind = "knowl"
summary = "Nonlinear integro-differential equation for the one-particle distribution in a dilute gas; collision operator encodes binary interactions and yields the H-theorem."
aliases = ["boltzmann-equation-kinetic", "Boltzmann equation (kinetic theory)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/boltzmann-equation-kinetic.md"
+++

The Boltzmann equation describes the evolution of a dilute gas at the level of the one-particle distribution, bridging microscopic dynamics and macroscopic thermodynamics.

Prerequisites: [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], [[thermodynamics/temperature-thermo|temperature]], [[stat-mech/canonical-ensemble|canonical ensemble]], [[stat-mech/boltzmann-h-theorem|Boltzmann H-theorem]], [[stat-mech/h-functional-boltzmann|H-functional]].

## Unknown and physical meaning
The unknown is the **one-particle distribution**
$f(t,x,v)\ge 0$ on time $t\ge 0$, position $x\in\mathbb{R}^3$ (or a box), and velocity $v\in\mathbb{R}^3$.
Macroscopic fields are velocity moments:
$$
\rho(t,x)=\int_{\mathbb{R}^3} f(t,x,v)\,dv,
\qquad
\rho u(t,x)=\int_{\mathbb{R}^3} v f(t,x,v)\,dv,
$$
and (kinetic) energy density
$$
\mathcal{E}(t,x)=\int_{\mathbb{R}^3} \frac{|v|^2}{2}\,f(t,x,v)\,dv.
$$

## Boltzmann equation (with external force)
The kinetic equation is
$$
\partial_t f + v\cdot\nabla_x f + \frac{F}{m}\cdot\nabla_v f = Q(f,f),
$$

where $F$ is an external force, $m$ the particle mass, and $Q(f,f)$ is the **collision operator**.

## Collision operator (standard binary-collision form)
A common form is
$$
Q(f,f)(v)=\int_{\mathbb{R}^3}\int_{\mathbb{S}^2}
B(|v-v_*|,\cos\theta)\,\Big(f(v')f(v_*')-f(v)f(v_*)\Big)\,d\omega\,dv_*,
$$

where $v_*$ is the collision partner velocity, $\omega\in\mathbb{S}^2$ parametrizes scattering, and $(v',v_*')$ are the post-collisional velocities determined by conservation of momentum and energy in a binary collision. The kernel $B$ encodes the interaction model (hard spheres, Maxwell molecules, etc.).

## Collision invariants and conservation laws
For collision invariants $\phi(v)\in\{1, v, |v|^2\}$ one has
$$
\int_{\mathbb{R}^3} Q(f,f)(v)\,\phi(v)\,dv = 0,
$$
which yields local balance laws for mass, momentum, and energy (up to transport terms).

## Maxwellian equilibria
Spatially homogeneous equilibria are Maxwellians:
$$
M(v)=\rho\left(\frac{m}{2\pi k T}\right)^{3/2}\exp\!\left(-\frac{m|v-u|^2}{2kT}\right),
$$

parameterized by density $\rho$, bulk velocity $u$, and temperature $T$. This connects to equilibrium ideas such as the [[stat-mech/canonical-ensemble|canonical ensemble]].

## H-theorem (entropy monotonicity)
Define the Boltzmann H-functional
$$
H[f]=\int f\log f\,dv\,dx.
$$
Along sufficiently regular solutions (with appropriate boundary/decay conditions),
$$
\frac{d}{dt}H[f(t)]\le 0,
$$
with equality only at (local) Maxwellians. This is the kinetic-theory route to entropy increase and is developed in [[stat-mech/boltzmann-h-theorem|Boltzmann H-theorem]] and [[stat-mech/h-functional-boltzmann|H-functional]].

## Modeling assumptions (context)
The equation is derived for a dilute gas under a molecular-chaos assumption (factorization of pre-collisional correlations). It is therefore an effective description rather than an exact rewriting of microscopic Hamiltonian dynamics.
