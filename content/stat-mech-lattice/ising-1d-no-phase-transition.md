---
title: "1D Ising model: no phase transition at positive temperature"
description: "Transfer-matrix solution of the 1D Ising chain showing analyticity of the free energy for T>0, exponential decay of correlations, and absence of spontaneous magnetization."
---

## Prerequisites and notation

- Lattice spin system and Hamiltonian: {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}
- Model definition: {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}, {{< knowl id="ferromagnetic-ising" section="stat-mech-lattice" text="ferromagnetic Ising interaction" >}}
- Canonical formalism: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}
- Correlations: {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}, {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}
- Order parameter language: {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}, {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}}

We consider spins $\sigma_i\in\{-1,+1\}$ on a 1D ring of $N$ sites (periodic boundary conditions).

## Example: 1D ferromagnetic Ising chain

### Hamiltonian
$$
H_N(\sigma) \;=\; -J\sum_{i=1}^N \sigma_i\sigma_{i+1} \;-\; h\sum_{i=1}^N \sigma_i,
\qquad \sigma_{N+1}=\sigma_1,
$$

with $J>0$ and external field $h\in\mathbb{R}$.

### Transfer matrix and partition function
The canonical partition function is
$$
Z_N(\beta,h)=\sum_{\sigma\in\{\pm1\}^N} e^{-\beta H_N(\sigma)}.
$$

Introduce the $2\times 2$ transfer matrix
$$
T_{\sigma,\sigma'}=\exp\!\left(\beta J\,\sigma\sigma' + \frac{\beta h}{2}(\sigma+\sigma')\right),
\qquad \sigma,\sigma'\in\{\pm1\}.
$$
Then
$$
Z_N(\beta,h)=\mathrm{Tr}\, T^N = \lambda_+^N + \lambda_-^N,
$$
where the eigenvalues are
$$
\lambda_{\pm}
= e^{\beta J}\cosh(\beta h)
\pm \sqrt{e^{2\beta J}\sinh^2(\beta h)+e^{-2\beta J}}.
$$

### Thermodynamic limit and analyticity
The (canonical) free energy per site is
$$
f(\beta,h)= -\frac{1}{\beta}\lim_{N\to\infty}\frac{1}{N}\log Z_N(\beta,h)
= -\frac{1}{\beta}\log \lambda_+.
$$

For every $\beta<\infty$ (i.e. $T>0$), $\lambda_+>\lambda_->0$ and $\lambda_+$ is a real-analytic function of $(\beta,h)$, hence $f(\beta,h)$ is analytic for $T>0$. In particular, there is **no finite-temperature phase transition** (no nonanalyticity of thermodynamic potentials), in contrast with {{< knowl id="ising-2d-phase-transition" text="the 2D Ising model" >}}.

### No spontaneous magnetization for $T>0$
Define magnetization per site
$$
m(\beta,h)= -\frac{\partial f}{\partial h}(\beta,h).
$$

Because $f(\beta,h)$ is analytic in $h$ around $h=0$ for every $T>0$, the one-sided limits agree:
$$
m(\beta,0^+)=m(\beta,0^-)=0 \quad (T>0),
$$
so there is no {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} at positive temperature.

### Exponential decay of correlations and correlation length
At $h=0$, the two-point function satisfies (in the infinite-volume limit)
$$
\langle \sigma_0\sigma_r\rangle = (\tanh(\beta J))^{r}.
$$
Thus correlations decay exponentially with
$$
\xi(\beta)=\frac{1}{-\log(\tanh(\beta J))},
$$

which is finite for every $T>0$ and diverges only as $T\downarrow 0$.

### Interpretation via Gibbs measures
In 1D with finite-range interaction, the infinite-volume Gibbs state is unique for all $T>0$, matching the absence of multiple equilibrium states seen in {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions as non-uniqueness of Gibbs measures" >}}.
