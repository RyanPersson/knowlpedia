---
title: "Legendre transform from internal energy to Gibbs free energy"
description: "Construct Gibbs free energy by Legendre transforming internal energy in both entropy and volume (replace S,V by T,p)."
---

Let the internal energy be written in the energy representation $U=U(S,V,N)$ (see {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}). The conjugate variables are temperature $T=(\partial U/\partial S)_{V,N}$ and pressure $p=-(\partial U/\partial V)_{S,N}$.

**Definition (Gibbs free energy as a double Legendre transform).**  
The Gibbs free energy $G(T,p,N)$ is obtained by trading $(S,V)$ for $(T,p)$ via a two-variable {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}:
$$
G(T,p,N)=\min_{S,V}\Bigl\{\,U(S,V,N)-T\,S+p\,V\Bigr\}.
$$

At the minimizer $(S^\star,V^\star)$, the stationarity conditions enforce
$$
T=\left(\frac{\partial U}{\partial S}\right)_{V,N}\Bigg|_{(S^\star,V^\star)},
\qquad
p=-\left(\frac{\partial U}{\partial V}\right)_{S,N}\Bigg|_{(S^\star,V^\star)}.
$$

Equivalently, one can perform the transform sequentially: first form {{< knowl id="construction-legendre-u-to-h" text="the enthalpy" >}} $H(S,p,N)$ by transforming in $V$, then transform in $S$ to get $G=H-T S$; or start from {{< knowl id="construction-legendre-s-to-f" text="the Helmholtz free energy" >}} and transform in $V$ to get $G=F+pV$ at the volume where $p=-(\partial F/\partial V)_{T,N}$.

**Differential and physical meaning.**  
The Gibbs free energy obeys
$$
dG=-S\,dT+V\,dp+\mu\,dN,
$$

so at fixed $(T,p,N)$ the equilibrium macrostate minimizes $G$. This is why $G$ (the {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}}) governs phase coexistence and chemical equilibrium under laboratory conditions where $T$ and $p$ are controlled.

**Statistical-mechanical representation.**  
In the {{< knowl id="isothermal-isobaric-ensemble" text="isothermal–isobaric ensemble" >}}, $G$ is obtained from the {{< knowl id="isothermal-isobaric-partition-function" text="NpT partition function" >}} $\Delta(T,p,N)$ by the same rule as other equilibrium potentials:
$$
G(T,p,N)=-k_B T\log \Delta(T,p,N).
$$

Derivatives of $G$ recover response variables; for example, the chemical potential satisfies $\mu=(\partial G/\partial N)_{T,p}$, connecting this construction to {{< knowl id="construction-chemical-potential-from-entropy" text="chemical potential from entropy" >}} and {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="the thermodynamic chemical potential" >}}.
