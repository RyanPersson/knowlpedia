---
title: "Maxwell relations theorem"
description: "Because thermodynamic potentials are state functions (exact differentials), their mixed second derivatives agree, yielding Maxwell relations among response functions."
---

## Statement

Let $\Phi=\Phi(x_1,\dots,x_n)$ be a thermodynamic potential expressed in its natural variables, and assume $\Phi$ is twice continuously differentiable. If its differential has the form
$$
d\Phi = \sum_{i=1}^n A_i\,dx_i,
$$

then exactness of $d\Phi$ implies symmetry of mixed partial derivatives:
$$
\frac{\partial A_i}{\partial x_j} = \frac{\partial A_j}{\partial x_i}
\qquad (i\neq j).
$$
These identities are called **Maxwell relations**.

For a simple one-component system (fixed particle number $N$) the standard thermodynamic potentials yield the familiar relations:

- From internal energy $U(S,V)$:
  $$
  dU = T\,dS - P\,dV,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial T}{\partial V}\right)_{S} = -\left(\frac{\partial P}{\partial S}\right)_{V}.
  $$

- From Helmholtz free energy $F(T,V)$:
  $$
  dF = -S\,dT - P\,dV,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial S}{\partial V}\right)_{T} = \left(\frac{\partial P}{\partial T}\right)_{V}.
  $$

- From Gibbs free energy $G(T,P)$:
  $$
  dG = -S\,dT + V\,dP,
  \qquad\Rightarrow\qquad
  \left(\frac{\partial S}{\partial P}\right)_{T} = -\left(\frac{\partial V}{\partial T}\right)_{P}.
  $$

(Analogous relations hold when including particle number and chemical potential among the variables.)

## Key hypotheses and conclusions

**Hypotheses**
- The system admits an equilibrium thermodynamic description (states in {{< knowl id="thermodynamic-equilibrium" section="thermodynamics" text="thermodynamic equilibrium" >}}).
- Thermodynamic potentials are well-defined {{< knowl id="thermodynamic-state" section="thermodynamics" text="state functions" >}} and are $C^2$ in their natural variables.
- The differential forms written for $dU,dF,dG,\ldots$ hold (typically derived from the first and second laws plus Legendre transforms).

**Conclusions**
- Mixed partial derivatives of potentials coincide, producing Maxwell relations.
- Maxwell relations provide experimentally useful identities that connect hard-to-measure derivatives (often involving entropy) to easier ones (often involving pressure/volume/temperature).

## Cross-links to definitions

Thermodynamic objects:
- {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}, {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}, {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}}, {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}}.
- {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}, {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}, {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}.

Structural/mathematical links:
- {{< knowl id="maxwell-relation" section="thermodynamics" text="Maxwell relation (definition)" >}}.
- {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}} (thermodynamic potentials as Legendre transforms of $U$).
- {{< knowl id="prop-maxwell-from-mixed-partials" section="stat-mech" text="Maxwell-from-mixed-partials proposition" >}} and {{< knowl id="corollary-maxwell-standard-identities" section="stat-mech" text="standard Maxwell identities corollary" >}}.
**Idea.** A thermodynamic potential is a state function, so its differential is exact (see {{< knowl id="exact-differential-criterion" section="stat-mech" text="exact differential criterion" >}}). Exactness implies equality of mixed second derivatives (Clairaut/Schwarz theorem), which directly produces the Maxwell relations once the coefficients in $dU,dF,dG,\ldots$ are identified with $T,S,P,V,\mu,N$.

**Significance.** Maxwell relations are consistency conditions for equilibrium thermodynamics and a practical computational tool: they turn “entropy derivatives” into measurable response derivatives and are central in deriving identities for heat capacities, compressibilities, and susceptibilities.
