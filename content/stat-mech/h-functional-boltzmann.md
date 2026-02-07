---
title: "Boltzmann H-functional"
description: "The functional H[f]=∫ f ln f for a dilute gas distribution f; its monotone decay along the Boltzmann equation encodes irreversible entropy production (H-theorem)."
---

## Definition (dilute classical gas)
Let $f(t,x,v)\ge 0$ be the one-particle distribution on phase space $(x,v)\in \mathbb{R}^d\times\mathbb{R}^d$ for a dilute gas evolving (under molecular chaos) by the {{< knowl id="boltzmann-equation-kinetic" text="Boltzmann equation" >}}. The **Boltzmann H-functional** is
$$
H[f(t)] \;=\; \int_{\mathbb{R}^d}\int_{\mathbb{R}^d} f(t,x,v)\,\ln f(t,x,v)\,dv\,dx,
$$

(with the convention $0\ln 0=0$). Often one also uses a spatially homogeneous version $H[f]=\int f(v)\ln f(v)\,dv$.

It is related to an entropy functional by
$$
S[f] \;=\; -k_B\,H[f] \;+\; \text{(additive constant depending on units)}.
$$

This $S[f]$ is the kinetic-theory counterpart of {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} and is closely aligned with {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}} / {{< knowl id="gibbs-entropy-shannon" section="stat-mech" text="Gibbs–Shannon entropy" >}}.

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

This monotonicity is the functional core of the {{< knowl id="boltzmann-h-theorem" text="Boltzmann H-theorem" >}}.

## Equilibrium characterization
In the spatially homogeneous case with fixed mass and energy, the minimizers of $H$ are Maxwell–Boltzmann distributions
$$
f_{\mathrm{eq}}(v)
={}
n\left(\frac{m}{2\pi k_B T}\right)^{d/2}
\exp\!\left(-\frac{m|v-u|^2}{2k_B T}\right),
$$

where $T$ is the {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} and $u$ is the mean velocity.

## Conceptual connections
- The decay of $H$ can be reframed as decrease of a {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} to equilibrium (after appropriate normalization), clarifying “entropy production” as a divergence.
- For stochastic dynamics (e.g. {{< knowl id="master-equation" text="master equation" >}} models), analogous Lyapunov functionals are built from relative entropy and link to {{< knowl id="detailed-balance" text="detailed balance" >}}.
