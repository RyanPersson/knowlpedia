---
title: "Homogeneous function of degree one"
description: "A function f is degree-one homogeneous if scaling all arguments by λ scales the value by λ; this encodes extensivity in thermodynamics."
---

A function $f(x_1,\dots,x_n)$ is **homogeneous of degree one** if, for all $\lambda>0$,
$$
f(\lambda x_1,\dots,\lambda x_n) = \lambda\, f(x_1,\dots,x_n).
$$
In thermodynamics, degree-one homogeneity is the mathematical expression of **extensivity**: doubling the size of a system (in a sense that scales all extensive variables together) doubles extensive thermodynamic potentials.

**Physical interpretation (thermodynamics).** For a simple macroscopic system obeying the {{< knowl id="extensivity-postulate" text="extensivity postulate" >}} and {{< knowl id="additivity-postulate" text="additivity postulate" >}}, state functions like the {{< knowl id="thermodynamic-entropy" text="entropy" >}} in the {{< knowl id="fundamental-relation-entropy" text="entropy fundamental relation" >}} or the {{< knowl id="internal-energy-thermo" text="internal energy" >}} in the {{< knowl id="fundamental-relation-energy" text="energy fundamental relation" >}} are modeled as degree-one homogeneous in their extensive arguments:
$S(U,V,N,\dots)$ and $U(S,V,N,\dots)$.
This approximation is most accurate in the {{< knowl id="thermodynamic-limit" text="thermodynamic limit" >}} and can fail when surface terms, long-range interactions, or finite-size effects are significant.

**Key consequences.**
- **Euler relation.** If $U(S,V,N,\dots)$ is differentiable and degree-one homogeneous, then Euler’s theorem gives the {{< knowl id="euler-relation-thermodynamics" text="Euler relation" >}}
  $U = TS - PV + \mu N + \cdots$,
  where $T,P,\mu$ are the conjugate intensive variables defined by derivatives of $U$.
- **Gibbs–Duhem relation.** Differentiating the Euler relation and comparing with $dU = T\,dS - P\,dV + \mu\,dN + \cdots$ yields the {{< knowl id="gibbs-duhem-relation" text="Gibbs–Duhem relation" >}}, constraining how intensive variables can change together.
- **Intensive variables are scale-invariant.** Under the same scaling of extensive variables, conjugate intensive variables such as {{< knowl id="temperature-thermo" text="temperature" >}}, {{< knowl id="pressure-thermo" text="pressure" >}}, and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} remain unchanged (consistent with the definition of an {{< knowl id="intensive-variable" text="intensive variable" >}}).
