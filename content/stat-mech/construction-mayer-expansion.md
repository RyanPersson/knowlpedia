---
title: "Mayer expansion (construction)"
description: "Graph expansion of the grand partition function of a classical interacting gas in powers of activity, using the Mayer f-bond."
---

The **Mayer expansion** is a classical, explicit instance of a {{< knowl id="construction-cluster-expansion" text="cluster expansion" >}} for continuum gases. It expands the {{< knowl id="grand-partition-function" text="grand partition function" >}} in powers of the activity $z$ and expresses $\log \Xi$ (hence the pressure) as a sum over **connected graphs** built from the Mayer f-function.

## Setup: grand canonical gas with pair interactions

Consider a classical gas in a bounded region $\Lambda\subset\mathbb{R}^d$ at inverse temperature $\beta$ (see {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature $\beta$" >}}), described in the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}}. For a pair potential $\phi(x)$, the total interaction energy for $N$ particles at positions $x_1,\dots,x_N$ is
$$
U_N(x_1,\dots,x_N)=\sum_{1\le i<j\le N}\phi(x_i-x_j).
$$
The grand partition function is
$$
\Xi_\Lambda(z,\beta)
={}
\sum_{N\ge 0}\frac{z^N}{N!}\int_{\Lambda^N} \exp\!\big(-\beta\,U_N(x_1,\dots,x_N)\big)\,dx_1\cdots dx_N,
$$
where the configuration integral is an ordinary (Lebesgue) multiple integral; the underlying measure-theoretic viewpoint is the {{< knowl id="lebesgue-integral" section="measure-theory" text="Lebesgue integral" >}}.

## Mayer f-bond and graph expansion

Define the **Mayer f-function** (or f-bond)
$$
f(x)=e^{-\beta \phi(x)}-1.
$$
Since
$$
e^{-\beta U_N}=\prod_{1\le i<j\le N} e^{-\beta\phi(x_i-x_j)}
=\prod_{1\le i<j\le N}\big(1+f(x_i-x_j)\big),
$$

expanding the product produces a sum over graphs $G$ on vertex set $\{1,\dots,N\}$, where each edge $(i,j)$ contributes a factor $f(x_i-x_j)$.

The key structural fact is that $\log \Xi_\Lambda$ **is obtained by summing only connected graphs**. One convenient way to write it is
$$
\log \Xi_\Lambda(z,\beta)
={}
\sum_{n\ge 1}\frac{z^n}{n!}\int_{\Lambda^n} \Phi_n^T(x_1,\dots,x_n)\,dx_1\cdots dx_n,
$$
with the connected (truncated) kernel
$$
\Phi_n^T(x_1,\dots,x_n)
={}
\sum_{\substack{G\ \text{connected}\\\text{on }\{1,\dots,n\}}}
\ \prod_{(i,j)\in E(G)} f(x_i-x_j).
$$

## Pressure and cluster integrals

The pressure is recovered from the grand partition function using {{< knowl id="pressure-from-partition-function" text="pressure from the partition function" >}}. Formally,
$$
\beta\,p(z,\beta)
={}
\lim_{|\Lambda|\to\infty}\frac{1}{|\Lambda|}\log \Xi_\Lambda(z,\beta)
={}
\sum_{n\ge 1} b_n(\beta)\, z^n,
$$

where $b_n(\beta)$ are the **cluster integrals**. The first few have simple forms under translation invariance; for example,
$$
b_1(\beta)=1,
\qquad
b_2(\beta)=\frac12\int_{\mathbb{R}^d} f(x)\,dx
\quad (\text{when the integral exists}).
$$
The number density satisfies
$$
\rho(z,\beta)= z\,\frac{\partial}{\partial z}\big(\beta p(z,\beta)\big)
=\sum_{n\ge 1} n\,b_n(\beta)\,z^n,
$$

which is the starting point for virial expansions (pressure as a series in $\rho$) at low density.

## Convergence regime and interpretation

For physically reasonable pair potentials (typically **stable** and **tempered**) the Mayer series converges for sufficiently small activity $z$ (low density) and/or high temperature. In that regime, the connected-graph structure makes $\log\Xi_\Lambda$ extensive and compatible with the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}.

Physically, the Mayer expansion reorganizes the grand canonical sum into contributions from interacting *clusters of particles*. Disconnected groups factorize in $\Xi_\Lambda$ and cancel when taking the logarithm, leaving only genuinely collective (connected) interaction effects.
