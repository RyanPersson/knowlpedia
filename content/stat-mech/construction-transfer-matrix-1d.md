---
title: "Transfer-matrix construction in 1D"
description: "Rewrite 1D Boltzmann weights as powers of a matrix to compute partition functions, free energies, and correlations."
---

For one-dimensional, nearest-neighbor lattice models, the **transfer matrix** turns the sum over all {{< knowl id="microstate-classical" text="microstates" >}} into linear algebra. It provides an exact route to the {{< knowl id="partition-function-canonical" text="canonical partition function" >}}, the {{< knowl id="free-energy-statistical" text="free energy" >}}, and decay of {{< knowl id="correlation-function-two-point" text="two-point correlations" >}} in 1D.

## Nearest-neighbor form and the transfer matrix
Consider a 1D chain of length $N$ with spins $\sigma_i\in S$ and a nearest-neighbor energy of the form
$$
H(\sigma_1,\dots,\sigma_N)=\sum_{i=1}^{N} U(\sigma_i,\sigma_{i+1}),
\qquad \sigma_{N+1}=\sigma_1
$$

(periodic boundary conditions). Fix {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature $\beta$" >}}.

Define the transfer matrix $T$ (a {{< knowl id="matrix" section="linear-algebra" text="matrix" >}} indexed by $S$) by
$$
T_{ab}=\exp\!\big(-\beta\,U(a,b)\big).
$$

More generally, if the Hamiltonian includes on-site terms $V(\sigma_i)$, one often splits them symmetrically into neighboring factors so that $T_{ab}=\exp(-\beta[U(a,b)+\tfrac12 V(a)+\tfrac12 V(b)])$; this keeps the representation exact and symmetric.

## Partition function as a trace
The periodic-chain partition function is
$$
Z_N=\sum_{\sigma_1,\dots,\sigma_N}\exp\!\big(-\beta H(\sigma_1,\dots,\sigma_N)\big)
=\mathrm{Tr}\big(T^N\big),
$$

where $\mathrm{Tr}$ is the {{< knowl id="trace" section="linear-algebra" text="trace" >}}. (For open boundary conditions, one obtains a bilinear form $Z_N=\langle \ell, T^{N-1} r\rangle$ with boundary vectors encoding the end weights.)

This representation is a concrete instance of “compute thermodynamics from $\log Z$,” as in {{< knowl id="construction-observables-from-log-z" text="extracting observables from $\log Z$" >}}.

## Thermodynamic limit and dominant eigenvalue
Let the eigenvalues of $T$ satisfy $|\lambda_0|\ge |\lambda_1|\ge\cdots$. Under mild positivity assumptions (typical for physical transfer matrices), $\lambda_0>0$ is the unique largest eigenvalue. Then, in the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}} $N\to\infty$,
$$
\frac{1}{N}\log Z_N\longrightarrow \log \lambda_0,
\qquad
f = -\frac{1}{\beta}\log \lambda_0,
$$

where $f$ is the free energy per site (a 1D analogue of the thermodynamic density encoded by {{< knowl id="free-energy-statistical" text="statistical free energy" >}}).

## Correlations and correlation length
Transfer matrices also control spatial correlations. For suitable local observables $A$ and $B$ at separation $r$, one typically finds asymptotic decay
$$
\langle A_0 B_r\rangle - \langle A_0\rangle\langle B_r\rangle \;\propto\; \left(\frac{\lambda_1}{\lambda_0}\right)^r
\quad\text{as } r\to\infty,
$$
so the associated {{< knowl id="connected-correlation-function" text="connected correlation" >}} decays exponentially. The corresponding {{< knowl id="correlation-length" text="correlation length" >}} is
$$
\xi^{-1} = -\log\left|\frac{\lambda_1}{\lambda_0}\right|.
$$

## Physical interpretation
The transfer matrix is a “propagator” that advances the system by one lattice step. Because $Z_N$ is governed by a largest eigenvalue, thermodynamic quantities in 1D with finite-range interactions are typically analytic in parameters for $T$ with strictly positive entries—one reason phase transitions are absent in many 1D short-range models.
