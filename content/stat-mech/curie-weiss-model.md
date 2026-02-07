---
title: "Curie–Weiss model"
description: "Mean-field Ising ferromagnet with explicit variational free energy and self-consistency equation; exhibits spontaneous magnetization and a second-order phase transition."
---

## Spins, Hamiltonian, and magnetization
The Curie–Weiss model is a fully connected mean-field analogue of the {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}.
Let $\sigma_i\in\{-1,+1\}$ for $i=1,\dots,N$ and define the empirical magnetization
$$
m_N(\sigma)=\frac{1}{N}\sum_{i=1}^N \sigma_i .
$$

With coupling $J>0$ (ferromagnetic) and external field $h\in\mathbb{R}$, the Hamiltonian is
$$
H_N(\sigma)=-\frac{J}{2N}\left(\sum_{i=1}^N \sigma_i\right)^2 - h\sum_{i=1}^N \sigma_i
= -\frac{J N}{2}\,m_N(\sigma)^2 - h N\,m_N(\sigma).
$$
This is a canonical example of {{< knowl id="mean-field-approximation" text="mean-field approximation" >}}.

## Partition function reduced to a sum over magnetization
In the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, the partition function is
$$
Z_N(\beta,h)=\sum_{\sigma\in\{-1,+1\}^N} e^{-\beta H_N(\sigma)}
=\sum_{\sigma} \exp\!\left(\beta N\left(\frac{J}{2}m_N(\sigma)^2+h\,m_N(\sigma)\right)\right).
$$

Grouping configurations by magnetization values $m\in\{-1,-1+2/N,\dots,1\}$ yields
$$
Z_N(\beta,h)=\sum_{m} \binom{N}{\frac{N(1+m)}{2}}\,
\exp\!\left(\beta N\left(\frac{J}{2}m^2+h\,m\right)\right).
$$

## Variational free energy in the thermodynamic limit
Using Stirling’s approximation,
$$
\frac{1}{N}\ln \binom{N}{\frac{N(1+m)}{2}}
\to s(m),
\qquad
s(m)= -\frac{1+m}{2}\ln\frac{1+m}{2}-\frac{1-m}{2}\ln\frac{1-m}{2},
$$
the pressure/free-energy per spin is obtained by Laplace’s method. Equivalently, the limiting free energy density can be written as
$$
f(\beta,h)= -\frac{1}{\beta}\lim_{N\to\infty}\frac{1}{N}\ln Z_N(\beta,h)
=\inf_{m\in[-1,1]} \Phi_{\beta,h}(m),
$$
where the mean-field Landau functional is
$$
\Phi_{\beta,h}(m)= -\frac{J}{2}m^2 - h m - \frac{1}{\beta}\,s(m).
$$
This is a concrete instance of a {{< knowl id="landau-free-energy-functional" text="Landau free energy functional" >}}.

## Self-consistency equation
Stationary points satisfy $\partial_m \Phi_{\beta,h}(m)=0$, which gives the Curie–Weiss mean-field equation
$$
m=\tanh\!\bigl(\beta(Jm+h)\bigr).
$$

Solutions describe possible equilibrium magnetizations; global minimizers of $\Phi_{\beta,h}$ determine the thermodynamic phase.

## Phase transition and spontaneous magnetization
At zero field $h=0$:
- For $T>T_c$ (equivalently $\beta J<1$), the only solution is $m=0$ and it is the unique minimizer of $\Phi_{\beta,0}$.
- For $T<T_c$ (equivalently $\beta J>1$), there are two symmetric nonzero minimizers $\pm m_*(T)$ solving
  $$
  m_*=\tanh(\beta J m_*).
  $$
This is the appearance of {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} with magnetization as the {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}.

The critical temperature is
$$
T_c=\frac{J}{k_B}.
$$
This provides a clean mean-field example of a {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transition" >}}.

## Susceptibility and Curie–Weiss law
For $T>T_c$ and small $h$, linearizing $m=\tanh(\beta(Jm+h))$ gives
$$
(1-\beta J)m \approx \beta h,
\qquad\Rightarrow\qquad
\chi := \left.\frac{\partial m}{\partial h}\right|_{h=0}
\approx \frac{\beta}{1-\beta J}
=\frac{1}{k_B(T-T_c)}.
$$

Thus the susceptibility diverges as $T\downarrow T_c$ (from above).

## Large-deviation viewpoint
The reduction to a one-dimensional variational problem reflects concentration of $m_N$ and can be formulated as a large-deviation principle for magnetization (see {{< knowl id="ldp-rate-function-magnetization" text="LDP rate function for magnetization" >}}), where $\Phi_{\beta,h}(m)$ plays the role of a rate-function-like effective potential (up to constants).
