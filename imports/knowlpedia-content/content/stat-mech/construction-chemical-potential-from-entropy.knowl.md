+++
id = "stat-mech/construction-chemical-potential-from-entropy"
title = "Chemical potential from entropy"
kind = "knowl"
summary = "Construct chemical potential as an entropy derivative with respect to particle number in the microcanonical description."
aliases = ["construction-chemical-potential-from-entropy", "Chemical potential from entropy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-chemical-potential-from-entropy.md"
+++

In microcanonical statistical mechanics, a [[stat-mech/macrostate|macrostate]] is characterized by $(U,V,N)$, and its entropy is typically the [[stat-mech/boltzmann-entropy-microcanonical|microcanonical (Boltzmann) entropy]] $S(U,V,N)$ built from the [[stat-mech/density-of-states|density of states]] (or the phase-space volume of the [[stat-mech/microcanonical-shell|energy shell]]).

**Definition (chemical potential from the entropy).**
Given $S(U,V,N)$, define temperature via [[stat-mech/construction-temperature-from-entropy|the energy derivative of the entropy]] and define the chemical potential $\mu$ as the conjugate to particle number:
$$
\frac{1}{T}
=\left(\frac{\partial S}{\partial U}\right)_{V,N},
\qquad
-\frac{\mu}{T}
=\left(\frac{\partial S}{\partial N}\right)_{U,V}.
$$

Equivalently, using $\beta=1/(k_B T)$ from [[thermodynamics/inverse-temperature-beta|inverse temperature]],
$$
\beta\,\mu=-\frac{1}{k_B}\left(\frac{\partial S}{\partial N}\right)_{U,V}.
$$

**Key identity and interpretation.**
Together with the volume derivative, this is summarized by
$$
dS=\frac{1}{T}\,dU+\frac{p}{T}\,dV-\frac{\mu}{T}\,dN,
$$

so $-\mu/T$ is the marginal entropy change when adding particles at fixed $U$ and $V$. Physically, $\mu$ is the intensive “cost” (in energy units) that controls particle exchange: if two subsystems can exchange particles while keeping total $U$ and $V$ fixed, maximizing total entropy forces equality of $\mu/T$ between them, and (when they also share energy) equality of $\mu$ as the familiar [[thermodynamics/chemical-potential-thermo|chemical potential]] equilibrium condition.

**Connection to the grand canonical ensemble.**
When $N$ fluctuates due to contact with a particle reservoir, the equilibrium weighting is governed by $\mu$ in the [[stat-mech/grand-canonical-ensemble|grand canonical ensemble]]. This construction is reflected in the factor $\exp(\beta\mu N)$ that enters the [[stat-mech/construction-grand-canonical-partition-function|grand canonical partition function construction]], and it is the Legendre-conjugate variable used when passing from $F(T,V,N)$ to the [[stat-mech/construction-legendre-f-to-omega|grand potential via a Legendre transform]].
