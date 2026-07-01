+++
id = "stat-mech/construction-legendre-s-to-f"
title = "Legendre transform from entropy to Helmholtz free energy"
kind = "knowl"
summary = "Construct the Helmholtz free energy by Legendre transforming the entropy with respect to energy (microcanonical → canonical)."
aliases = ["construction-legendre-s-to-f", "Legendre transform from entropy to Helmholtz free energy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-legendre-s-to-f.md"
+++

Start from an entropy representation $S(U,V,N)$, such as the [[stat-mech/boltzmann-entropy-microcanonical|microcanonical entropy]] derived from the [[stat-mech/density-of-states|density of states]]. The temperature is obtained by [[stat-mech/construction-temperature-from-entropy|differentiating the entropy with respect to energy]], so the variable conjugate to $U$ is $1/T$ (or $\beta=1/(k_B T)$ from [[thermodynamics/inverse-temperature-beta|inverse temperature]]).

**Definition (Legendre–Fenchel transform).**
The Helmholtz free energy $F(T,V,N)$ is constructed by trading $U$ for $T$ via a (Fenchel) [[convex-analysis/legendre-transform|Legendre transform]]:
$$
F(T,V,N)=\min_{U}\Bigl\{\,U-T\,S(U,V,N)\Bigr\}.
$$

The minimizing energy $U^\star(T,V,N)$ satisfies the stationarity condition
$$
\frac{1}{T}=\left(\frac{\partial S}{\partial U}\right)_{V,N}\Bigg|_{U=U^\star}.
$$
A common equivalent dimensionless form is
$$
-\beta\,F(\beta,V,N)=\sup_{U}\left\{\frac{S(U,V,N)}{k_B}-\beta\,U\right\}.
$$

This makes explicit that the transform is “sup” rather than “inf” in the entropy representation because $S$ is typically concave in $U$ for stable macroscopic systems.

**Physical meaning.**
This construction produces the thermodynamic potential appropriate to the [[stat-mech/canonical-ensemble|canonical ensemble]]: fixing $T$ means the system explores energies, and $F$ captures the competition between energetic cost $U$ and entropic gain $T S$. In the [[thermodynamics/thermodynamic-limit|thermodynamic limit]], the supremum form aligns with the [[large-deviations/laplace-principle|Laplace principle]] interpretation of Laplace-type integrals.

**Connection to the partition function.**
For canonical statistical mechanics, the same object is obtained from the [[stat-mech/partition-function-canonical|canonical partition function]] through [[stat-mech/construction-free-energy-from-partition|free energy from the partition function]]:
$$
F(T,V,N)=-k_B T\log Z(\beta,V,N).
$$

This identification explains why derivatives of $F$ generate equilibrium response functions (e.g. pressure and chemical potential) and underlies [[stat-mech/construction-observables-from-log-z|extracting observables from $\log Z$]].
