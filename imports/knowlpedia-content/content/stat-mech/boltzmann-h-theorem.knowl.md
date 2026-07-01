+++
id = "stat-mech/boltzmann-h-theorem"
title = "Boltzmann H-theorem"
kind = "knowl"
summary = "Monotonicity of Boltzmann’s H-functional (entropy increase) for dilute gases evolving under the Boltzmann equation, under molecular chaos."
aliases = ["boltzmann-h-theorem", "Boltzmann H-theorem"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/boltzmann-h-theorem.md"
+++

## Statement (kinetic theory setting)

Let $f(t,x,v)\ge 0$ be the one-particle distribution of a dilute classical gas evolving by the [[stat-mech/boltzmann-equation-kinetic|Boltzmann equation]]
$$
\partial_t f + v\cdot \nabla_x f + \frac{F}{m}\cdot \nabla_v f = Q(f,f),
$$

where $Q$ is the binary-collision operator with a nonnegative collision kernel.

Define the [[stat-mech/h-functional-boltzmann|Boltzmann H-functional]]
$$
H[f](t) := \int f(t,x,v)\,\ln f(t,x,v)\,dx\,dv
$$
(typically on a domain with suitable boundary conditions, or in the spatially homogeneous case).

Then, for sufficiently regular solutions and admissible collision kernels,
$$
\frac{d}{dt}H[f](t) \le 0,
$$

with equality (for appropriate classes of solutions) if and only if $f$ is a local Maxwellian (i.e., a collision equilibrium).

Equivalently, the kinetic entropy $S_{\mathrm{kin}}(t):= -k_B\,H[f](t)$ is nondecreasing, matching the direction of the [[thermodynamics/second-law-thermodynamics|second law]] at this level of description.

## Entropy production formula

In the spatially homogeneous case (or after integrating out transport terms), one can write
$$
-\frac{d}{dt}H[f](t)=\frac14\int (f'f_1'-ff_1)\,
\ln\!\Big(\frac{f'f_1'}{ff_1}\Big)\,B(\cdots)\,d\omega\,dv\,dv_1 \;\ge\; 0,
$$

where $(v,v_1)\mapsto(v',v_1')$ is the post-collision velocity map, $B\ge 0$ is the collision kernel, and the inequality uses $(a-b)\ln(a/b)\ge 0$ for $a,b>0$.

## Assumptions and scope

- **Dilute gas + binary collisions:** encoded in the collision operator $Q(f,f)$.
- **Molecular chaos (Stosszahlansatz):** the crucial closure assumption leading from reversible microscopic dynamics to the irreversible kinetic equation.
- **Regularity / integrability:** needed to justify differentiating $H[f]$ and exchanging integrals.

## Conceptual meaning

- The H-theorem provides a precise sense in which *coarse-grained* entropy increases for kinetic evolution, even though the underlying microscopic dynamics (at the [[stat-mech/microstate-classical|microstate]] level) are reversible.
- It is a prototype mechanism for emergence of irreversibility and motivates connections between kinetic entropy and [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]].
