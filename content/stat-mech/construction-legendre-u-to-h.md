---
title: "Legendre transform from internal energy to enthalpy"
description: "Construct enthalpy by Legendre transforming internal energy with respect to volume (replace V by p)."
---

Suppose the macroscopic energy of a single-component system is written in the energy representation as
$U=U(S,V,N)$, where $U$ is the {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} and $S,V,N$ are the natural extensive variables. The conjugate intensive variables are
temperature $T$, {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} $p$, and chemical potential $\mu$.

**Definition (enthalpy as a Legendre transform in $V$).**  
Define $p$ in the energy representation by
$$
p=-\left(\frac{\partial U}{\partial V}\right)_{S,N},
\qquad
T=\left(\frac{\partial U}{\partial S}\right)_{V,N},
\qquad
\mu=\left(\frac{\partial U}{\partial N}\right)_{S,V}.
$$

The enthalpy is the Legendre transform of $U$ that replaces $V$ by $p$:
$$
H(S,p,N)=\min_{V}\Bigl\{\,U(S,V,N)+p\,V\Bigr\}.
$$

At the minimizing volume $V^\star(S,p,N)$, the stationarity condition reproduces the defining relation
$p=-(\partial U/\partial V)_{S,N}$, and then $H=U+pV$ evaluated at $V^\star$.

**Differentials and interpretation.**  
Starting from the fundamental differential
$$
dU=T\,dS-p\,dV+\mu\,dN,
$$
the transformed potential satisfies
$$
dH=T\,dS+V\,dp+\mu\,dN.
$$

Thus $H$ is the natural potential when entropy (or heat input) and pressure are controlled, because changes in $p$ appear linearly with coefficient $V$. Physically, the additional term $pV$ accounts for the mechanical work needed to “make room” for the system against an external pressure reservoir.

**Link to ensembles.**  
In the {{< knowl id="isothermal-isobaric-ensemble" text="isothermal–isobaric ensemble" >}}, the combination $U+pV$ appears in the Boltzmann weight before taking the temperature transform, and this structure is reflected in the {{< knowl id="isothermal-isobaric-partition-function" text="isothermal–isobaric partition function" >}}. Completing the additional Legendre transform in $S$ leads to {{< knowl id="construction-legendre-u-to-g" text="the Gibbs free energy construction" >}}.
