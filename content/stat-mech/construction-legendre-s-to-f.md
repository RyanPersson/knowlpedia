---
title: "Legendre transform from entropy to Helmholtz free energy"
description: "Construct the Helmholtz free energy by Legendre transforming the entropy with respect to energy (microcanonical → canonical)."
---

Start from an entropy representation $S(U,V,N)$, such as the {{< knowl id="boltzmann-entropy-microcanonical" text="microcanonical entropy" >}} derived from the {{< knowl id="density-of-states" text="density of states" >}}. The temperature is obtained by {{< knowl id="construction-temperature-from-entropy" text="differentiating the entropy with respect to energy" >}}, so the variable conjugate to $U$ is $1/T$ (or $\beta=1/(k_B T)$ from {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}}).

**Definition (Legendre–Fenchel transform).**  
The Helmholtz free energy $F(T,V,N)$ is constructed by trading $U$ for $T$ via a (Fenchel) {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}:
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
This construction produces the thermodynamic potential appropriate to the {{< knowl id="canonical-ensemble" text="canonical ensemble" >}}: fixing $T$ means the system explores energies, and $F$ captures the competition between energetic cost $U$ and entropic gain $T S$. In the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}}, the supremum form aligns with the {{< knowl id="laplace-principle" section="large-deviations" text="Laplace principle" >}} interpretation of Laplace-type integrals.

**Connection to the partition function.**  
For canonical statistical mechanics, the same object is obtained from the {{< knowl id="partition-function-canonical" text="canonical partition function" >}} through {{< knowl id="construction-free-energy-from-partition" text="free energy from the partition function" >}}:
$$
F(T,V,N)=-k_B T\log Z(\beta,V,N).
$$

This identification explains why derivatives of $F$ generate equilibrium response functions (e.g. pressure and chemical potential) and underlies {{< knowl id="construction-observables-from-log-z" text="extracting observables from $\log Z$" >}}.
