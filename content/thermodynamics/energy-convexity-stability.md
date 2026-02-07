---
title: "Energy convexity and thermodynamic stability"
description: "Convexity of the energy fundamental relation as a stability condition, equivalent to entropy concavity and positivity of key response functions."
---

In the **energy representation** of equilibrium thermodynamics, the {{< knowl id="fundamental-relation-energy" text="fundamental relation" >}} expresses the {{< knowl id="internal-energy-thermo" text="internal energy" >}} as a function of the {{< knowl id="extensive-variable" text="extensive variables" >}}, typically
$U = U(S,V,N,\dots)$, where $S$ is {{< knowl id="thermodynamic-entropy" text="thermodynamic entropy" >}}, $V$ is {{< knowl id="volume-thermo" text="volume" >}}, and $N$ is {{< knowl id="particle-number" text="particle number" >}}.

**Definition (energy convexity).** The equilibrium energy function $U(S,V,N,\dots)$ is **convex** if for any two admissible macrostates $X_1=(S_1,V_1,N_1,\dots)$ and $X_2=(S_2,V_2,N_2,\dots)$ and any $0\le \lambda\le 1$,
$$
U\!\big(\lambda X_1+(1-\lambda)X_2\big)\ \le\ \lambda\,U(X_1)\ +\ (1-\lambda)\,U(X_2).
$$

Here $\lambda X_1+(1-\lambda)X_2$ denotes the extensive variables obtained by taking weighted totals (the natural operation for composing macroscopic subsystems).

**Physical interpretation.** Energy convexity is a **stability** statement: at fixed total extensive variables, a system cannot lower its energy by splitting into two macroscopic regions (“phase separation”) with different local values of $(S,V,N,\dots)$. If convexity fails, the system can reduce $U$ by separating into distinct macrostates, signaling instability of a homogeneous equilibrium. This criterion is one of the standard formulations of {{< knowl id="thermodynamic-stability" text="thermodynamic stability" >}}.

**Equivalent stability formulation.** Energy convexity is equivalent (under mild regularity assumptions) to {{< knowl id="entropy-concavity-stability" text="concavity of the entropy representation" >}} $S=S(U,V,N,\dots)$. These are the same stability content viewed in two Legendre-dual coordinate choices.

**Local (differential) consequences.** When $U$ is twice differentiable, convexity implies the Hessian of $U(S,V,N,\dots)$ is positive semidefinite. In particular, it forces positivity of several measurable {{< knowl id="response-function-thermo" text="response functions" >}}. For example, holding $V,N$ fixed one has
$$
\frac{\partial^2 U}{\partial S^2}\Big|_{V,N}=\frac{T}{C_V}\ \ge\ 0,
$$

so the {{< knowl id="heat-capacity-constant-volume" text="heat capacity at constant volume" >}} satisfies $C_V\ge 0$ (assuming {{< knowl id="temperature-thermo" text="temperature" >}} $T>0$). Similarly, convexity in $V$ is tied to nonnegative {{< knowl id="adiabatic-compressibility" text="adiabatic compressibility" >}} (and, in appropriate ensembles, the {{< knowl id="isothermal-compressibility" text="isothermal compressibility" >}}).

**Mathematical viewpoint.** This is convexity in the usual sense of the {{< knowl id="convex-function-via-epigraph" section="convex-analysis" text="epigraph definition of a convex function" >}}. It is also what ensures thermodynamic potentials related by {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transforms" >}} are well-defined and have the expected extremum principles.
