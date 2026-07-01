+++
id = "stat-mech-lattice/gibbs-specification"
title = "Gibbs specification"
kind = "knowl"
summary = "A consistent family of finite-volume conditional distributions giving the local Gibbs law in every finite region as a function of the outside configuration."
aliases = ["gibbs-specification", "Gibbs specification"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/gibbs-specification.md"
+++

Let $\Omega$ be the [[stat-mech-lattice/configuration-space-lattice|configuration space]] of a lattice spin system (built from a [[stat-mech-lattice/spin-space|single-site spin space]]), equipped with its natural [[measure-theory/sigma-algebra|sigma-algebra]] of cylinder events. A **specification** is a family of probability kernels
$$
\gamma = \bigl(\gamma_\Lambda\bigr)_{\Lambda\Subset\mathbb{Z}^d},
$$

indexed by finite regions $\Lambda$, where each $\gamma_\Lambda(\,\cdot\,\mid \eta)$ is a [[probability/probability-measure|probability measure]] on $\Omega$ depending measurably on the outside configuration $\eta\in\Omega$. (Formally, it is a family of [[probability/conditional-probability|conditional probability]] kernels.)

A **Gibbs specification** associated with inverse temperature $\beta$ and a given [[stat-mech-lattice/interaction-potential-phi|interaction potential]] (or, equivalently, a [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]]) is the specification whose kernel on a finite region $\Lambda$ is obtained by:
1. sampling spins in $\Lambda$ according to the [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] with boundary condition $\eta_{\Lambda^c}$, and
2. keeping spins outside $\Lambda$ fixed equal to $\eta_{\Lambda^c}$.

Concretely, if $\lambda$ is an a priori single-spin measure and $H_\Lambda(\sigma_\Lambda\mid\eta)$ is the finite-volume Hamiltonian, then the conditional law on $\Lambda$ is
$$
\gamma_\Lambda(d\sigma_\Lambda \mid \eta)
={}
\frac{1}{Z_\Lambda(\beta,\eta)}
\exp\!\bigl(-\beta\,H_\Lambda(\sigma_\Lambda\mid\eta)\bigr)\,
\lambda_\Lambda(d\sigma_\Lambda),
$$

with $Z_\Lambda(\beta,\eta)$ the [[stat-mech-lattice/partition-function-lattice|lattice partition function]]. This kernel extends to a probability measure on $\Omega$ by combining the sampled $\sigma_\Lambda$ with the fixed exterior configuration $\eta_{\Lambda^c}$.

## Key properties

- **Properness (fixes the exterior).** Under $\gamma_\Lambda(\cdot\mid\eta)$, the configuration on $\Lambda^c$ is almost surely equal to $\eta_{\Lambda^c}$.

- **Consistency (compatibility).** If $\Lambda\subset\Delta$, then conditioning in stages is the same as conditioning once:
  applying $\gamma_\Lambda$ and then $\gamma_\Delta$ yields the same result as applying $\gamma_\Delta$ directly (as kernels on $\Omega$).

- **Local dependence for short-range models.** For [[stat-mech-lattice/finite-range-interaction-lattice|finite-range interactions]], $\gamma_\Lambda(\cdot\mid\eta)$ depends on $\eta$ only through spins near the boundary of $\Lambda$.

- **Bridge to infinite volume.** A Gibbs specification is the input for the [[stat-mech-lattice/dlr-equation|DLR equation]], which characterizes [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] as measures consistent with these local conditionals.

## Physical interpretation

A Gibbs specification is a precise encoding of “local equilibrium”: no matter what the global system looks like, the distribution of spins in a finite window $\Lambda$ conditioned on the surrounding environment should be given by the appropriate Boltzmann weights for that window, with the environment acting as the boundary condition.
