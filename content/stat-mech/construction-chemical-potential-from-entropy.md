---
title: "Chemical potential from entropy"
description: "Construct chemical potential as an entropy derivative with respect to particle number in the microcanonical description."
---

In microcanonical statistical mechanics, a {{< knowl id="macrostate" text="macrostate" >}} is characterized by $(U,V,N)$, and its entropy is typically the {{< knowl id="boltzmann-entropy-microcanonical" text="microcanonical (Boltzmann) entropy" >}} $S(U,V,N)$ built from the {{< knowl id="density-of-states" text="density of states" >}} (or the phase-space volume of the {{< knowl id="microcanonical-shell" text="energy shell" >}}).

**Definition (chemical potential from the entropy).**  
Given $S(U,V,N)$, define temperature via {{< knowl id="construction-temperature-from-entropy" text="the energy derivative of the entropy" >}} and define the chemical potential $\mu$ as the conjugate to particle number:
$$
\frac{1}{T}
=\left(\frac{\partial S}{\partial U}\right)_{V,N},
\qquad
-\frac{\mu}{T}
=\left(\frac{\partial S}{\partial N}\right)_{U,V}.
$$

Equivalently, using $\beta=1/(k_B T)$ from {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}},
$$
\beta\,\mu=-\frac{1}{k_B}\left(\frac{\partial S}{\partial N}\right)_{U,V}.
$$

**Key identity and interpretation.**  
Together with the volume derivative, this is summarized by
$$
dS=\frac{1}{T}\,dU+\frac{p}{T}\,dV-\frac{\mu}{T}\,dN,
$$

so $-\mu/T$ is the marginal entropy change when adding particles at fixed $U$ and $V$. Physically, $\mu$ is the intensive “cost” (in energy units) that controls particle exchange: if two subsystems can exchange particles while keeping total $U$ and $V$ fixed, maximizing total entropy forces equality of $\mu/T$ between them, and (when they also share energy) equality of $\mu$ as the familiar {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}} equilibrium condition.

**Connection to the grand canonical ensemble.**  
When $N$ fluctuates due to contact with a particle reservoir, the equilibrium weighting is governed by $\mu$ in the {{< knowl id="grand-canonical-ensemble" text="grand canonical ensemble" >}}. This construction is reflected in the factor $\exp(\beta\mu N)$ that enters the {{< knowl id="construction-grand-canonical-partition-function" text="grand canonical partition function construction" >}}, and it is the Legendre-conjugate variable used when passing from $F(T,V,N)$ to the {{< knowl id="construction-legendre-f-to-omega" text="grand potential via a Legendre transform" >}}.
