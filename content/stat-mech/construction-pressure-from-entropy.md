---
title: "Pressure from entropy"
description: "Construct thermodynamic pressure as an entropy derivative with respect to volume in the microcanonical description."
---

In the microcanonical viewpoint, a {{< knowl id="macrostate" text="macrostate" >}} is specified by conserved quantities such as energy $U$, volume $V$, and particle number $N$. Its entropy is often taken to be the {{< knowl id="boltzmann-entropy-microcanonical" text="microcanonical (Boltzmann) entropy" >}}
defined from the phase-space volume of the {{< knowl id="microcanonical-shell" text="energy shell" >}}.

**Definition (pressure from the entropy).**  
Given an entropy function $S(U,V,N)$, define the temperature via {{< knowl id="construction-temperature-from-entropy" text="the entropy derivative with respect to energy" >}} and then define the pressure by the conjugate entropy derivative with respect to volume:
$$
\frac{1}{T}
=\left(\frac{\partial S}{\partial U}\right)_{V,N},
\qquad
\frac{p}{T}
=\left(\frac{\partial S}{\partial V}\right)_{U,N}.
$$
Equivalently,
$$
p(U,V,N)=T(U,V,N)\left(\frac{\partial S}{\partial V}\right)_{U,N}.
$$

In terms of the {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta=1/(k_B T)$ (with {{< knowl id="boltzmann-constant" section="thermodynamics" text="Boltzmann’s constant" >}} $k_B$),
$$
\beta\,p=\frac{1}{k_B}\left(\frac{\partial S}{\partial V}\right)_{U,N}.
$$

**Key identity and interpretation.**  
These definitions are encoded in the fundamental differential form
$$
dS=\frac{1}{T}\,dU+\frac{p}{T}\,dV-\frac{\mu}{T}\,dN,
$$

so $p/T$ measures how rapidly the number of accessible microstates grows under an infinitesimal expansion at fixed $U$ and $N$. In equilibrium, this pressure matches the mechanical {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} that balances an external constraint; it is the coefficient of the reversible $p\,dV$ work term in the {{< knowl id="first-law-thermodynamics" section="thermodynamics" text="first law" >}} written in entropy variables.

**Connection to free energy and partition functions.**  
After constructing the {{< knowl id="construction-legendre-s-to-f" text="Helmholtz free energy by Legendre transforming the entropy" >}}, the same pressure can be obtained at fixed $T$ from
$$
p=-\left(\frac{\partial F}{\partial V}\right)_{T,N},
$$
which matches the canonical expression described in {{< knowl id="pressure-from-partition-function" text="pressure from the partition function" >}}.
