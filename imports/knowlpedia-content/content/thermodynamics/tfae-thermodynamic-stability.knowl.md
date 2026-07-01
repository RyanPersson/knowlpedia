+++
id = "thermodynamics/tfae-thermodynamic-stability"
title = "TFAE: Thermodynamic Stability Criteria"
kind = "knowl"
summary = "Equivalent stability conditions: concavity/convexity of thermodynamic potentials and positivity of response functions."
aliases = ["tfae-thermodynamic-stability", "TFAE: Thermodynamic Stability Criteria"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/tfae-thermodynamic-stability.md"
+++

Consider a simple macroscopic system in [[thermodynamics/thermodynamic-equilibrium|thermodynamic equilibrium]] with a differentiable fundamental relation written in the entropy representation $S=S(U,V,N)$ (or equivalently the energy representation $U=U(S,V,N)$). The following are equivalent local stability criteria (for fixed $N$ one may drop $N$ from the notation).

1. **Entropy maximum principle (microcanonical stability).**
   Among nearby equilibrium states with the same $(U,V,N)$, the equilibrium state locally maximizes [[thermodynamics/thermodynamic-entropy|entropy]]:
   $$
   \delta^2 S \le 0 \quad \text{at fixed } (U,V,N).
   $$

2. **Concavity of the entropy.**
   The function $S(U,V,N)$ is concave in its extensive variables, i.e. for $0\le \lambda \le 1$,
   $$
   S(\lambda x + (1-\lambda)y) \ge \lambda S(x) + (1-\lambda)S(y),
   $$

   where $x=(U,V,N)$ and $y=(U',V',N')$.
   Equivalently, the Hessian matrix of second derivatives of $S$ is negative semidefinite (when it exists).

3. **Convexity of the internal energy.**
   The [[thermodynamics/internal-energy-thermo|internal energy]] $U(S,V,N)$ is convex in $(S,V,N)$, equivalently its Hessian is positive semidefinite.
   (This is the Legendre-dual statement to concavity of $S$; see [[convex-analysis/legendre-transform|Legendre transform]].)

4. **Minimum principle for appropriate thermodynamic potentials.**
   At fixed intensive controls, equilibrium minimizes the corresponding potential. In particular:
   - At fixed $(T,V,N)$, equilibrium minimizes the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)=U-TS$.
   - At fixed $(T,P,N)$, equilibrium minimizes the Gibbs free energy (if used in your convention).

5. **Positivity of response functions.**
   Stability is equivalent to nonnegative susceptibilities such as:
   - **Heat capacity at constant volume:**
     $$
     C_V = \left(\frac{\partial U}{\partial T}\right)_{V,N} \ge 0,
     $$
     matching [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]].
   - **Isothermal compressibility:**
     $$
     \kappa_T = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_{T,N} \ge 0,
     $$

     equivalently $(\partial P/\partial V)_{T,N} \le 0$ where [[thermodynamics/pressure-thermo|pressure]] is $P$.

6. **Second-derivative tests for the Helmholtz free energy.**
   Using $S=-(\partial F/\partial T)_{V,N}$ and $P=-(\partial F/\partial V)_{T,N}$, stability is equivalent to
   $$
   \left(\frac{\partial^2 F}{\partial T^2}\right)_{V,N} \le 0
   \quad\text{and}\quad
   \left(\frac{\partial^2 F}{\partial V^2}\right)_{T,N} \ge 0,
   $$

   which are the differential forms of $C_V\ge 0$ and $\kappa_T\ge 0$.

Prerequisites and context: [[thermodynamics/thermodynamic-stability|thermodynamic stability]], [[thermodynamics/thermodynamic-entropy|entropy]], [[thermodynamics/internal-energy-thermo|internal energy]], [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]], [[thermodynamics/heat-capacity-constant-volume|heat capacity]], [[convex-analysis/legendre-transform|Legendre transform]].
