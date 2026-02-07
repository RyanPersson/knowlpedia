---
title: "Example: classical monatomic ideal gas"
description: "Canonical-ensemble computation for a classical ideal gas: partition function, equation of state, energy, heat capacity, and entropy."
---

Consider $N$ identical noninteracting monatomic particles of mass $m$ in a volume $V$ (a {{< knowl id="thermodynamic-system" section="thermodynamics" text="thermodynamic system" >}}). A classical {{< knowl id="microstate-classical" section="stat-mech" text="microstate" >}} is $(q_1,\dots,q_N,p_1,\dots,p_N)$ with Hamiltonian
$$H(p,q)=\sum_{i=1}^N \frac{|p_i|^2}{2m}.$$

In the {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}} at inverse temperature $\beta=1/(k_B T)$, the $N$-particle {{< knowl id="partition-function-canonical" section="stat-mech" text="partition function" >}} is
$$
Z_N(\beta)=\frac{1}{N!\,h^{3N}}\int_{V^N}\!dq\int_{\mathbb R^{3N}}\!dp\;e^{-\beta H(p,q)}
= \frac{1}{N!}\left(\frac{V}{\lambda_T^3}\right)^N,
$$
where the thermal wavelength is
$$\lambda_T=\frac{h}{\sqrt{2\pi m k_B T}}.$$

Key thermodynamic results:

- **Helmholtz free energy.** Using {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}},
  $$F(T,V,N)=-k_B T\log Z_N.$$

- **Equation of state (ideal gas law).**
  $$p = -\left(\frac{\partial F}{\partial V}\right)_{T,N} = \frac{N k_B T}{V}, \qquad\text{so } pV=Nk_BT.$$

  Here $p$ is the {{< knowl id="pressure-thermo" section="thermodynamics" text="pressure" >}}.

- **Internal energy and heat capacity.**
  $$U = -\frac{\partial}{\partial\beta}\log Z_N = \frac{3}{2}N k_B T,$$
  hence
  $$C_V=\left(\frac{\partial U}{\partial T}\right)_{V,N}=\frac{3}{2}N k_B,$$
  matching {{< knowl id="heat-capacity-constant-volume" section="thermodynamics" text="heat capacity at constant volume" >}}.

- **Entropy.** From $S=-(\partial F/\partial T)_{V,N}$ ({{< knowl id="thermodynamic-entropy" section="thermodynamics" text="entropy" >}}),
  $$S = N k_B\left[\ln\!\left(\frac{V}{N\lambda_T^3}\right)+\frac{5}{2}\right],$$

  which is the {{< knowl id="sackur-tetrode-entropy" text="Sackur–Tetrode formula" >}} in its $T$-representation.

- **Energy fluctuations (canonical).** The canonical variance satisfies
  $$\mathrm{Var}(U)=k_B T^2 C_V,$$
  relating {{< knowl id="variance" section="probability" text="variance" >}} to thermodynamic response.

Prerequisites: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}, {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}, {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}}.
