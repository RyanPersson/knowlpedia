---
title: "Legendre transform swaps conjugate variables"
description: "A Legendre transform replaces a natural variable by its conjugate variable, with the new potential’s derivatives returning the swapped pair (up to sign)."
---

## Statement

Let $X(x,y)$ be a thermodynamic potential (a state function) with $x$ one of its natural variables and $y$ collecting the remaining variables. Assume $X$ is differentiable and define the conjugate variable
$ p := \left(\frac{\partial X}{\partial x}\right)_y $
and the (partial) Legendre transform in $x$ by
$$
Y(p,y) := X(x,y) - p\,x,
$$

where $x=x(p,y)$ is chosen so that $p = \left(\frac{\partial X}{\partial x}\right)_y$.

Then the differential of $Y$ is
$$
dY = -x\,dp + \sum_i \left(\frac{\partial X}{\partial y_i}\right)_x\,dy_i,
$$

so the variable $x$ has been replaced by its conjugate $p$ as an independent variable, and the conjugacy is recovered by
$$
\left(\frac{\partial Y}{\partial p}\right)_y = -x.
$$

In thermodynamics, this “swap” is the mechanism behind passing from the {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} $U(S,V,N)$ to standard thermodynamic potentials such as the {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} $F(T,V,N)=U-TS$, the {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}} $G(T,P,N)=U-TS+PV$, and the {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}} $\Omega(T,V,\mu)=U-TS-\mu N$.

## Key hypotheses

- $X(x,y)$ is a well-defined state function (depends only on the {{< knowl id="thermodynamic-state" section="thermodynamics" text="thermodynamic state" >}}).
- $X$ is differentiable in $x$ and the map $x \mapsto p=(\partial X/\partial x)_y$ can be locally inverted (often ensured by appropriate convexity/concavity assumptions; see {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}).

## Key conclusions

- The Legendre-transformed potential $Y$ has $p$ (not $x$) as a natural variable.
- Conjugate variables are recovered by differentiation:
  - $p = (\partial X/\partial x)_y$ in the original potential,
  - $x = -(\partial Y/\partial p)_y$ in the transformed potential.
- In thermodynamic examples, the transform replaces an extensive variable (e.g. $S$) by its conjugate intensive variable (e.g. {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}} $T$), or replaces $V$ by {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}} $P$, or $N$ by {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}} $\mu$, with the corresponding sign conventions.

## Cross-links to definitions

- {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}
- {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}}, {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}
- {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}, {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}, {{< knowl id="chemical-potential-thermo" section="thermodynamics" text="chemical potential" >}}
- {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}, {{< knowl id="gibbs-free-energy" section="thermodynamics" text="Gibbs free energy" >}}, {{< knowl id="grand-potential" section="thermodynamics" text="grand potential" >}}

Significance: the Legendre transform produces potentials whose natural variables match common experimental controls (e.g. fixing $T$ rather than $S$), while preserving access to the conjugate extensive quantities through derivatives (e.g. $S=-\partial F/\partial T$ at fixed $V,N$).

