+++
id = "thermodynamics/homogeneous-function-degree-one"
title = "Homogeneous function of degree one"
kind = "knowl"
summary = "A function f is degree-one homogeneous if scaling all arguments by λ scales the value by λ; this encodes extensivity in thermodynamics."
aliases = ["homogeneous-function-degree-one", "Homogeneous function of degree one"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/homogeneous-function-degree-one.md"
+++

A function $f(x_1,\dots,x_n)$ is **homogeneous of degree one** if, for all $\lambda>0$,
$$
f(\lambda x_1,\dots,\lambda x_n) = \lambda\, f(x_1,\dots,x_n).
$$
In thermodynamics, degree-one homogeneity is the mathematical expression of **extensivity**: doubling the size of a system (in a sense that scales all extensive variables together) doubles extensive thermodynamic potentials.

**Physical interpretation (thermodynamics).** For a simple macroscopic system obeying the [[thermodynamics/extensivity-postulate|extensivity postulate]] and [[thermodynamics/additivity-postulate|additivity postulate]], state functions like the [[thermodynamics/thermodynamic-entropy|entropy]] in the [[thermodynamics/fundamental-relation-entropy|entropy fundamental relation]] or the [[thermodynamics/internal-energy-thermo|internal energy]] in the [[thermodynamics/fundamental-relation-energy|energy fundamental relation]] are modeled as degree-one homogeneous in their extensive arguments:
$S(U,V,N,\dots)$ and $U(S,V,N,\dots)$.
This approximation is most accurate in the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] and can fail when surface terms, long-range interactions, or finite-size effects are significant.

**Key consequences.**
- **Euler relation.** If $U(S,V,N,\dots)$ is differentiable and degree-one homogeneous, then Euler’s theorem gives the [[thermodynamics/euler-relation-thermodynamics|Euler relation]]
  $U = TS - PV + \mu N + \cdots$,
  where $T,P,\mu$ are the conjugate intensive variables defined by derivatives of $U$.
- **Gibbs–Duhem relation.** Differentiating the Euler relation and comparing with $dU = T\,dS - P\,dV + \mu\,dN + \cdots$ yields the [[thermodynamics/gibbs-duhem-relation|Gibbs–Duhem relation]], constraining how intensive variables can change together.
- **Intensive variables are scale-invariant.** Under the same scaling of extensive variables, conjugate intensive variables such as [[thermodynamics/temperature-thermo|temperature]], [[thermodynamics/pressure-thermo|pressure]], and [[thermodynamics/chemical-potential-thermo|chemical potential]] remain unchanged (consistent with the definition of an [[thermodynamics/intensive-variable|intensive variable]]).
