+++
id = "stat-mech/h-functional-boltzmann"
title = "Boltzmann H-functional"
kind = "knowl"
summary = "The functional H[f]=∫ f ln f for a dilute gas distribution f; its monotone decay along the Boltzmann equation encodes irreversible entropy production (H-theorem)."
aliases = ["h-functional-boltzmann", "Boltzmann H-functional"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/h-functional-boltzmann.md"
+++

## Definition (dilute classical gas)
Let $f(t,x,v)\ge 0$ be the one-particle distribution on phase space $(x,v)\in \mathbb{R}^d\times\mathbb{R}^d$ for a dilute gas evolving (under molecular chaos) by the [[stat-mech/boltzmann-equation-kinetic|Boltzmann equation]]. The **Boltzmann H-functional** is
$$
H[f(t)] \;=\; \int_{\mathbb{R}^d}\int_{\mathbb{R}^d} f(t,x,v)\,\ln f(t,x,v)\,dv\,dx,
$$

(with the convention $0\ln 0=0$). Often one also uses a spatially homogeneous version $H[f]=\int f(v)\ln f(v)\,dv$.

It is related to an entropy functional by
$$
S[f] \;=\; -k_B\,H[f] \;+\; \text{(additive constant depending on units)}.
$$

This $S[f]$ is the kinetic-theory counterpart of [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]] and is closely aligned with [[probability/shannon-entropy|Shannon entropy]] / [[stat-mech/gibbs-entropy-shannon|Gibbs–Shannon entropy]].

## H-theorem (monotonicity)
For sufficiently regular solutions of the Boltzmann equation,
$$
\frac{d}{dt}H[f(t)] \;\le\; 0,
$$

with equality iff $f$ is (locally) Maxwellian. Equivalently, $S[f(t)]$ is nondecreasing.

A standard explicit form of the entropy production is
$$
\frac{d}{dt}H[f(t)]
\;=\;
-\frac{1}{4}\int B(\cdot)\,\bigl(f'f_1' - f f_1\bigr)\,
\ln\!\Bigl(\frac{f'f_1'}{f f_1}\Bigr)\,d\Gamma
\;\le\; 0,
$$

where $(f,f_1)$ and $(f',f_1')$ denote pre/post-collisional values and $d\Gamma$ abbreviates the collision integration measure; the inequality follows from $(a-b)\ln(a/b)\ge 0$ for $a,b>0$.

This monotonicity is the functional core of the [[stat-mech/boltzmann-h-theorem|Boltzmann H-theorem]].

## Equilibrium characterization
In the spatially homogeneous case with fixed mass and energy, the minimizers of $H$ are Maxwell–Boltzmann distributions
$$
f_{\mathrm{eq}}(v)
={}
n\left(\frac{m}{2\pi k_B T}\right)^{d/2}
\exp\!\left(-\frac{m|v-u|^2}{2k_B T}\right),
$$

where $T$ is the [[thermodynamics/temperature-thermo|temperature]] and $u$ is the mean velocity.

## Conceptual connections
- The decay of $H$ can be reframed as decrease of a [[probability/relative-entropy-kl-divergence|relative entropy]] to equilibrium (after appropriate normalization), clarifying “entropy production” as a divergence.
- For stochastic dynamics (e.g. [[stat-mech/master-equation|master equation]] models), analogous Lyapunov functionals are built from relative entropy and link to [[stat-mech/detailed-balance|detailed balance]].
