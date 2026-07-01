+++
id = "stat-mech/free-energy-statistical"
title = "Statistical mechanical free energy"
kind = "knowl"
summary = "Free energy defined from the partition function; it generates thermodynamic observables and encodes equilibrium via a variational principle."
aliases = ["free-energy-statistical", "Statistical mechanical free energy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/free-energy-statistical.md"
+++

**Definition (canonical free energy).**
For a system with [[stat-mech/hamiltonian-function-classical|Hamiltonian]] $H$ in the [[stat-mech/canonical-ensemble|canonical ensemble]], the [[stat-mech/partition-function-canonical|canonical partition function]] at inverse temperature [[thermodynamics/inverse-temperature-beta|β]] is $Z(\beta,V,N)$. The **Helmholtz free energy** in statistical mechanics is
$$
F(T,V,N) = -k_B T \,\ln Z(\beta,V,N),
\qquad \beta=\frac{1}{k_B T}.
$$
It matches the thermodynamic [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] in the thermodynamic limit (up to conventions for additive constants).

Equivalently, one often uses the dimensionless free energy (Massieu potential)
$$
\Phi(\beta,V,N)=\ln Z(\beta,V,N),
$$
which is especially convenient because its derivatives produce [[stat-mech/construction-observables-from-log-z|equilibrium observables from log Z]].

**Key formulas (generating properties).**
Let $\langle \cdot \rangle$ denote the [[stat-mech/ensemble-average|ensemble average]] in the canonical ensemble. Then
$$
\langle H\rangle = -\frac{\partial}{\partial \beta}\ln Z,
\qquad
S = k_B\big(\ln Z + \beta \langle H\rangle\big),
$$
and the pressure can be extracted via [[stat-mech/pressure-from-partition-function|pressure from the partition function]].

**Variational (Gibbs) principle.**
Let $\rho$ range over all normalized probability densities on phase space (or over all probability measures on microstates). The functional
$$
\mathcal{F}[\rho]=\langle H\rangle_\rho - T\,S_G[\rho]
$$

uses the [[stat-mech/gibbs-entropy-shannon|Gibbs (Shannon) entropy]] $S_G[\rho]$. The canonical equilibrium state minimizes $\mathcal{F}[\rho]$, and its minimum value equals $F(T,V,N)$. This viewpoint is tightly connected to [[probability/relative-entropy-kl-divergence|relative entropy]] and convex duality ideas such as the [[convex-analysis/legendre-transform|Legendre transform]].

**Other ensembles.**
Analogous definitions hold in other ensembles: for the [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]] with [[stat-mech/grand-partition-function|grand partition function]] $\Xi(\beta,\mu,V)$, the grand potential is
$$
\Omega(T,\mu,V) = -k_B T \,\ln \Xi,
$$
matching the thermodynamic [[thermodynamics/grand-potential|grand potential]]. These relationships are organized conceptually by Legendre-transform constructions such as [[stat-mech/construction-legendre-s-to-f|Legendre transform from entropy to free energy]].
