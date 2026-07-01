+++
id = "stat-mech/construction-pressure-from-entropy"
title = "Pressure from entropy"
kind = "knowl"
summary = "Construct thermodynamic pressure as an entropy derivative with respect to volume in the microcanonical description."
aliases = ["construction-pressure-from-entropy", "Pressure from entropy"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-pressure-from-entropy.md"
+++

In the microcanonical viewpoint, a [[stat-mech/macrostate|macrostate]] is specified by conserved quantities such as energy $U$, volume $V$, and particle number $N$. Its entropy is often taken to be the [[stat-mech/boltzmann-entropy-microcanonical|microcanonical (Boltzmann) entropy]]
defined from the phase-space volume of the [[stat-mech/microcanonical-shell|energy shell]].

**Definition (pressure from the entropy).**
Given an entropy function $S(U,V,N)$, define the temperature via [[stat-mech/construction-temperature-from-entropy|the entropy derivative with respect to energy]] and then define the pressure by the conjugate entropy derivative with respect to volume:
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

In terms of the [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta=1/(k_B T)$ (with [[thermodynamics/boltzmann-constant|Boltzmann’s constant]] $k_B$),
$$
\beta\,p=\frac{1}{k_B}\left(\frac{\partial S}{\partial V}\right)_{U,N}.
$$

**Key identity and interpretation.**
These definitions are encoded in the fundamental differential form
$$
dS=\frac{1}{T}\,dU+\frac{p}{T}\,dV-\frac{\mu}{T}\,dN,
$$

so $p/T$ measures how rapidly the number of accessible microstates grows under an infinitesimal expansion at fixed $U$ and $N$. In equilibrium, this pressure matches the mechanical [[thermodynamics/pressure-thermo|pressure]] that balances an external constraint; it is the coefficient of the reversible $p\,dV$ work term in the [[thermodynamics/first-law-thermodynamics|first law]] written in entropy variables.

**Connection to free energy and partition functions.**
After constructing the [[stat-mech/construction-legendre-s-to-f|Helmholtz free energy by Legendre transforming the entropy]], the same pressure can be obtained at fixed $T$ from
$$
p=-\left(\frac{\partial F}{\partial V}\right)_{T,N},
$$
which matches the canonical expression described in [[stat-mech/pressure-from-partition-function|pressure from the partition function]].
