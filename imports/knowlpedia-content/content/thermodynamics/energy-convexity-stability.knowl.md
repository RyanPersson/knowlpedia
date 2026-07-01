+++
id = "thermodynamics/energy-convexity-stability"
title = "Energy convexity and thermodynamic stability"
kind = "knowl"
summary = "Convexity of the energy fundamental relation as a stability condition, equivalent to entropy concavity and positivity of key response functions."
aliases = ["energy-convexity-stability", "Energy convexity and thermodynamic stability"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/energy-convexity-stability.md"
+++

In the **energy representation** of equilibrium thermodynamics, the [[thermodynamics/fundamental-relation-energy|fundamental relation]] expresses the [[thermodynamics/internal-energy-thermo|internal energy]] as a function of the [[thermodynamics/extensive-variable|extensive variables]], typically
$U = U(S,V,N,\dots)$, where $S$ is [[thermodynamics/thermodynamic-entropy|thermodynamic entropy]], $V$ is [[thermodynamics/volume-thermo|volume]], and $N$ is [[thermodynamics/particle-number|particle number]].

**Definition (energy convexity).** The equilibrium energy function $U(S,V,N,\dots)$ is **convex** if for any two admissible macrostates $X_1=(S_1,V_1,N_1,\dots)$ and $X_2=(S_2,V_2,N_2,\dots)$ and any $0\le \lambda\le 1$,
$$
U\!\big(\lambda X_1+(1-\lambda)X_2\big)\ \le\ \lambda\,U(X_1)\ +\ (1-\lambda)\,U(X_2).
$$

Here $\lambda X_1+(1-\lambda)X_2$ denotes the extensive variables obtained by taking weighted totals (the natural operation for composing macroscopic subsystems).

**Physical interpretation.** Energy convexity is a **stability** statement: at fixed total extensive variables, a system cannot lower its energy by splitting into two macroscopic regions (“phase separation”) with different local values of $(S,V,N,\dots)$. If convexity fails, the system can reduce $U$ by separating into distinct macrostates, signaling instability of a homogeneous equilibrium. This criterion is one of the standard formulations of [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

**Equivalent stability formulation.** Energy convexity is equivalent (under mild regularity assumptions) to [[thermodynamics/entropy-concavity-stability|concavity of the entropy representation]] $S=S(U,V,N,\dots)$. These are the same stability content viewed in two Legendre-dual coordinate choices.

**Local (differential) consequences.** When $U$ is twice differentiable, convexity implies the Hessian of $U(S,V,N,\dots)$ is positive semidefinite. In particular, it forces positivity of several measurable [[thermodynamics/response-function-thermo|response functions]]. For example, holding $V,N$ fixed one has
$$
\frac{\partial^2 U}{\partial S^2}\Big|_{V,N}=\frac{T}{C_V}\ \ge\ 0,
$$

so the [[thermodynamics/heat-capacity-constant-volume|heat capacity at constant volume]] satisfies $C_V\ge 0$ (assuming [[thermodynamics/temperature-thermo|temperature]] $T>0$). Similarly, convexity in $V$ is tied to nonnegative [[thermodynamics/adiabatic-compressibility|adiabatic compressibility]] (and, in appropriate ensembles, the [[thermodynamics/isothermal-compressibility|isothermal compressibility]]).

**Mathematical viewpoint.** This is convexity in the usual sense of the [[convex-analysis/convex-function-via-epigraph|epigraph definition of a convex function]]. It is also what ensures thermodynamic potentials related by [[convex-analysis/legendre-transform|Legendre transforms]] are well-defined and have the expected extremum principles.
