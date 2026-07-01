+++
id = "stat-mech/construction-transfer-matrix-1d"
title = "Transfer-matrix construction in 1D"
kind = "knowl"
summary = "Rewrite 1D Boltzmann weights as powers of a matrix to compute partition functions, free energies, and correlations."
aliases = ["construction-transfer-matrix-1d", "Transfer-matrix construction in 1D"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-transfer-matrix-1d.md"
+++

For one-dimensional, nearest-neighbor lattice models, the **transfer matrix** turns the sum over all [[stat-mech/microstate-classical|microstates]] into linear algebra. It provides an exact route to the [[stat-mech/partition-function-canonical|canonical partition function]], the [[stat-mech/free-energy-statistical|free energy]], and decay of [[stat-mech/correlation-function-two-point|two-point correlations]] in 1D.

## Nearest-neighbor form and the transfer matrix
Consider a 1D chain of length $N$ with spins $\sigma_i\in S$ and a nearest-neighbor energy of the form
$$
H(\sigma_1,\dots,\sigma_N)=\sum_{i=1}^{N} U(\sigma_i,\sigma_{i+1}),
\qquad \sigma_{N+1}=\sigma_1
$$

(periodic boundary conditions). Fix [[thermodynamics/inverse-temperature-beta|inverse temperature $\beta$]].

Define the transfer matrix $T$ (a [[linear-algebra/matrix|matrix]] indexed by $S$) by
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

where $\mathrm{Tr}$ is the [[linear-algebra/trace|trace]]. (For open boundary conditions, one obtains a bilinear form $Z_N=\langle \ell, T^{N-1} r\rangle$ with boundary vectors encoding the end weights.)

This representation is a concrete instance of “compute thermodynamics from $\log Z$,” as in [[stat-mech/construction-observables-from-log-z|extracting observables from $\log Z$]].

## Thermodynamic limit and dominant eigenvalue
Let the eigenvalues of $T$ satisfy $|\lambda_0|\ge |\lambda_1|\ge\cdots$. Under mild positivity assumptions (typical for physical transfer matrices), $\lambda_0>0$ is the unique largest eigenvalue. Then, in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] $N\to\infty$,
$$
\frac{1}{N}\log Z_N\longrightarrow \log \lambda_0,
\qquad
f = -\frac{1}{\beta}\log \lambda_0,
$$

where $f$ is the free energy per site (a 1D analogue of the thermodynamic density encoded by [[stat-mech/free-energy-statistical|statistical free energy]]).

## Correlations and correlation length
Transfer matrices also control spatial correlations. For suitable local observables $A$ and $B$ at separation $r$, one typically finds asymptotic decay
$$
\langle A_0 B_r\rangle - \langle A_0\rangle\langle B_r\rangle \;\propto\; \left(\frac{\lambda_1}{\lambda_0}\right)^r
\quad\text{as } r\to\infty,
$$
so the associated [[stat-mech/connected-correlation-function|connected correlation]] decays exponentially. The corresponding [[stat-mech/correlation-length|correlation length]] is
$$
\xi^{-1} = -\log\left|\frac{\lambda_1}{\lambda_0}\right|.
$$

## Physical interpretation
The transfer matrix is a “propagator” that advances the system by one lattice step. Because $Z_N$ is governed by a largest eigenvalue, thermodynamic quantities in 1D with finite-range interactions are typically analytic in parameters for $T$ with strictly positive entries—one reason phase transitions are absent in many 1D short-range models.
