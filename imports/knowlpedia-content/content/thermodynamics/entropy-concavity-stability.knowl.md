+++
id = "thermodynamics/entropy-concavity-stability"
title = "Entropy Concavity and Stability"
kind = "knowl"
summary = "Stability in the entropy representation is equivalent to entropy being concave in the extensive variables."
aliases = ["entropy-concavity-stability", "Entropy Concavity and Stability"]
domains = ["thermodynamics"]
legacy_source_path = "thermodynamics/entropy-concavity-stability.md"
+++

## Definition (global concavity)

Let the [[thermodynamics/fundamental-relation-entropy|fundamental relation in the entropy representation]] be $S=S(U,V,N)$ for a single-phase system, with $(U,V,N)$ being [[thermodynamics/extensive-variable|extensive variables]]. The entropy is **concave** if for any two states $x_1=(U_1,V_1,N_1)$ and $x_2=(U_2,V_2,N_2)$ and any $\lambda\in[0,1]$,
$$
S\!\big(\lambda x_1 + (1-\lambda)x_2\big)
\ge
\lambda S(x_1) + (1-\lambda)S(x_2).
$$

Physically, this expresses that “mixing” or composing subsystems at fixed total $(U,V,N)$ cannot reduce total [[thermodynamics/thermodynamic-entropy|entropy]]; it is the mathematical backbone of why the [[thermodynamics/thermodynamic-equilibrium|equilibrium]] state of an isolated system is a stable entropy maximum, i.e. a core part of [[thermodynamics/thermodynamic-stability|thermodynamic stability]].

## Local (differential) criterion

If $S$ is twice differentiable, concavity is equivalent to the Hessian (matrix of second [[real-analysis/partial-derivative|partial derivatives]]) with respect to $(U,V,N)$ being negative semidefinite. For example, restricting attention to $(U,V)$ at fixed $N$, one requires
$$
\left(\frac{\partial^2 S}{\partial U^2}\right)_{V,N} \le 0,
\qquad
\det
\begin{pmatrix}
S_{UU} & S_{UV}\\
S_{VU} & S_{VV}
\end{pmatrix}
\ge 0,
$$

with $S_{UU}$ etc. denoting the corresponding second derivatives at fixed $N$.

## Consequences for response functions

Concavity translates into positivity of familiar [[thermodynamics/response-function-thermo|response functions]]:

- Using the defining relation $1/T = (\partial S/\partial U)_{V,N}$ for the [[thermodynamics/temperature-thermo|temperature]] $T$, one finds
  $$
  \left(\frac{\partial^2 S}{\partial U^2}\right)_{V,N}
  ={}
  -\frac{1}{T^2}\left(\frac{\partial T}{\partial U}\right)_{V,N}
  ={}
  -\frac{1}{T^2\,C_V},
  $$

  where $C_V$ is the [[thermodynamics/heat-capacity-constant-volume|constant-volume heat capacity]]. Thus $S_{UU}\le 0$ implies $C_V\ge 0$ (strict concavity corresponds to $C_V>0$).

- Through Legendre transforms to potentials such as the [[thermodynamics/helmholtz-free-energy|Helmholtz free energy]] $F(T,V,N)$ and [[thermodynamics/gibbs-free-energy|Gibbs free energy]] $G(T,P,N)$ (a thermodynamic instance of the [[convex-analysis/legendre-transform|Legendre transform]]), entropy concavity enforces mechanical stability conditions like $(\partial P/\partial V)_{T,N}<0$, i.e. a positive [[thermodynamics/isothermal-compressibility|isothermal compressibility]].

- A standard identity relating measurable susceptibilities,
  $$
  C_P - C_V = \frac{T V \alpha^2}{\kappa_T},
  $$

  shows (for $T>0$) that positivity of the [[thermodynamics/isothermal-compressibility|isothermal compressibility]] and the [[thermodynamics/thermal-expansion-coefficient|thermal expansion coefficient]] implies the [[thermodynamics/heat-capacity-constant-pressure|constant-pressure heat capacity]] satisfies $C_P\ge C_V$.
