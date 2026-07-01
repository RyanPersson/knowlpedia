+++
id = "stat-mech/cluster-integrals-mayer"
title = "Mayer cluster integrals"
kind = "knowl"
summary = "Connected-graph coefficients in the activity expansion of the grand potential (log grand partition function) for a classical gas; generate virial coefficients and low-density thermodynamics."
aliases = ["cluster-integrals-mayer", "Mayer cluster integrals"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/cluster-integrals-mayer.md"
+++

Mayer’s cluster expansion rewrites the interacting Boltzmann weight in terms of “$f$-bonds” and organizes the resulting series by graphs. The coefficients of the *connected* graphs are the Mayer cluster integrals.

They are the standard bridge between microscopic interactions and macroscopic expansions such as [[stat-mech/virial-coefficients|virial coefficients]].

## Grand partition function and the Mayer $f$-bond

For a classical gas in a volume $V$ at inverse temperature $\beta$, with activity $z$ and pair potential $u(\cdot)$, the grand partition function is
$$
\Xi(z,V,\beta)
\;=\;
\sum_{N=0}^{\infty}\frac{z^N}{N!}
\int_{V^N}
\exp\!\bigl(-\beta U_N(x_1,\dots,x_N)\bigr)\,
dx_1\cdots dx_N,
$$
where for pair interactions
$$
U_N(x_1,\dots,x_N) \;=\; \sum_{1\le i<j\le N} u(x_i-x_j).
$$

Define the Mayer $f$-bond
$$
f_{ij} \;=\; e^{-\beta u(x_i-x_j)} - 1.
$$

Then
$$
e^{-\beta U_N}
\;=\;
\prod_{i<j} e^{-\beta u(x_i-x_j)}
\;=\;
\prod_{i<j}\bigl(1+f_{ij}\bigr),
$$

and expanding the product generates a sum over graphs on $\{1,\dots,N\}$, with an edge $\{i,j\}$ contributing a factor $f_{ij}$.

## Connected graphs and $\log \Xi$

The logarithm of the grand partition function selects *connected* contributions. A standard form of Mayer’s identity is
$$
\log \Xi(z,V,\beta)
={}
\sum_{n\ge 1}\frac{z^n}{n!}
\int_{V^n}
\left(
\sum_{G\in \mathcal{C}_n}
\prod_{\{i,j\}\in E(G)} f_{ij}
\right)\,
dx_1\cdots dx_n,
$$
where:
- $\mathcal{C}_n$ is the set of connected graphs on $n$ labeled vertices,
- $E(G)$ is the edge set of the graph $G$.

This is the origin of the “cluster” terminology: connected clusters of particles contribute to $\log \Xi$.

## Definition of Mayer cluster integrals

In the thermodynamic limit (when it exists), one defines coefficients $b_n(\beta)$ by the *activity expansion of the pressure*:
$$
\frac{1}{V}\log \Xi(z,V,\beta)
\;=\;
\sum_{n\ge 1} b_n(\beta)\, z^n.
$$

These $b_n$ are the Mayer cluster integrals (up to common convention-dependent prefactors, e.g. thermal wavelength factors in continuum gases).

In this normalization, the pressure and density follow from derivatives of $\log \Xi$:
$$
\beta p \;=\; \frac{1}{V}\log \Xi \;=\; \sum_{n\ge 1} b_n z^n,
$$
and
$$
\rho \;=\; z\,\partial_z\!\left(\frac{1}{V}\log \Xi\right)
\;=\;
\sum_{n\ge 1} n\, b_n z^n.
$$

This “log-partition per volume” viewpoint is the same object used in [[stat-mech/pressure-log-partition-density|pressure as log-partition density]].

## From cluster integrals to virial coefficients

Eliminating $z$ between $\beta p(z)$ and $\rho(z)$ yields the virial expansion
$$
\beta p \;=\; \rho + B_2\rho^2 + B_3\rho^3 + \cdots
$$

with coefficients $B_n$ that are polynomials in the $b_n$ (see [[stat-mech/virial-coefficients|virial coefficients]]).

In the common convention where the ideal term is normalized so that $b_1=1$, the first relations are
$$
B_2 = -b_2,
\qquad
B_3 = 4b_2^2 - 2b_3.
$$

## Convergence and cluster expansion theorems

Rigorous results typically prove that the series for $\log \Xi$ converges for sufficiently small $|z|$ under stability and regularity assumptions on the interaction. This is the content of [[stat-mech/cluster-expansion-theorem|cluster expansion theorems]], and it underlies analytic control of [[stat-mech/virial-expansion-convergence|virial expansion convergence]].

## Prerequisites

- [[stat-mech/canonical-ensemble|Canonical ensemble (background on partition functions)]]
- [[stat-mech/partition-function-canonical|Canonical partition function]]
- [[stat-mech/virial-coefficients|Virial coefficients]]
- [[stat-mech/cluster-expansion-theorem|Cluster expansion theorem]]
- [[stat-mech/pressure-log-partition-density|Pressure as log-partition density]]
