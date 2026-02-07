---
title: "Statistical mechanical free energy"
description: "Free energy defined from the partition function; it generates thermodynamic observables and encodes equilibrium via a variational principle."
---

**Definition (canonical free energy).**  
For a system with {{< knowl id="hamiltonian-function-classical" text="Hamiltonian" >}} $H$ in the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}, the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} at inverse temperature {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="β" >}} is $Z(\beta,V,N)$. The **Helmholtz free energy** in statistical mechanics is
$$
F(T,V,N) = -k_B T \,\ln Z(\beta,V,N),
\qquad \beta=\frac{1}{k_B T}.
$$
It matches the thermodynamic {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} in the thermodynamic limit (up to conventions for additive constants).

Equivalently, one often uses the dimensionless free energy (Massieu potential)
$$
\Phi(\beta,V,N)=\ln Z(\beta,V,N),
$$
which is especially convenient because its derivatives produce {{< knowl id="construction-observables-from-log-z" text="equilibrium observables from log Z" >}}.

**Key formulas (generating properties).**  
Let $\langle \cdot \rangle$ denote the {{< knowl id="ensemble-average" text="ensemble average" >}} in the canonical ensemble. Then
$$
\langle H\rangle = -\frac{\partial}{\partial \beta}\ln Z,
\qquad
S = k_B\big(\ln Z + \beta \langle H\rangle\big),
$$
and the pressure can be extracted via {{< knowl id="pressure-from-partition-function" text="pressure from the partition function" >}}.

**Variational (Gibbs) principle.**  
Let $\rho$ range over all normalized probability densities on phase space (or over all probability measures on microstates). The functional
$$
\mathcal{F}[\rho]=\langle H\rangle_\rho - T\,S_G[\rho]
$$

uses the {{< knowl id="gibbs-entropy-shannon" text="Gibbs (Shannon) entropy" >}} $S_G[\rho]$. The canonical equilibrium state minimizes $\mathcal{F}[\rho]$, and its minimum value equals $F(T,V,N)$. This viewpoint is tightly connected to {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy" >}} and convex duality ideas such as the {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}.

**Other ensembles.**  
Analogous definitions hold in other ensembles: for the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}} with {{< knowl id="grand-partition-function" text="grand partition function" >}} $\Xi(\beta,\mu,V)$, the grand potential is
$$
\Omega(T,\mu,V) = -k_B T \,\ln \Xi,
$$
matching the thermodynamic {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}}. These relationships are organized conceptually by Legendre-transform constructions such as {{< knowl id="construction-legendre-s-to-f" text="Legendre transform from entropy to free energy" >}}.
