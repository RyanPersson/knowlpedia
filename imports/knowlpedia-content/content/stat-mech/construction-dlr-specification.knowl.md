+++
id = "stat-mech/construction-dlr-specification"
title = "DLR specification (Gibbsian conditional probabilities)"
kind = "knowl"
summary = "A consistent family of finite-volume conditional Gibbs kernels that defines infinite-volume Gibbs measures via the DLR equations."
aliases = ["construction-dlr-specification", "DLR specification (Gibbsian conditional probabilities)"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-dlr-specification.md"
+++

In lattice statistical mechanics on the [[discrete-structures/lattice-zd|lattice $\mathbb{Z}^d$]], an infinite system is described by a [[probability/probability-measure|probability measure]] $\mu$ on the configuration space. The **Dobrushin–Lanford–Ruelle (DLR) specification** packages the idea that *every finite region is in thermal equilibrium conditional on the outside configuration*.

## Set-up
Let $S$ be the single-site state space (e.g. $S=\{\pm1\}$ for Ising spins). The full configuration space is
$\Omega = S^{\mathbb{Z}^d}$, equipped with the product [[measure-theory/sigma-algebra|$\sigma$-algebra]] of cylinder events. A finite region is a [[discrete-structures/finite-box-lattice|finite box $\Lambda\subset\mathbb{Z}^d$]], and $\eta\in\Omega$ denotes a *boundary condition* (the configuration outside $\Lambda$).

## Definition (specification as conditional Gibbs kernels)
A **DLR specification** is a family of probability kernels $\gamma=\{\gamma_\Lambda\}_{\Lambda\Subset\mathbb{Z}^d}$ such that for each finite $\Lambda$:

1. **Kernel property:** for each boundary configuration $\eta$, $\gamma_\Lambda(\,\cdot\,|\eta)$ is a probability measure on the spins in $\Lambda$.
2. **Measurability:** for each event $A$ depending only on $\Lambda$, the map $\eta\mapsto \gamma_\Lambda(A|\eta)$ is measurable with respect to the outside variables $\eta_{\Lambda^c}$.
3. **Properness:** events depending only on $\Lambda^c$ are left unchanged (conditioning does not alter what is already fixed outside).
4. **Consistency (Markovianity across volumes):** if $\Lambda\subset\Delta$, then integrating inside $\Delta$ and then inside $\Lambda$ is the same as integrating inside $\Delta$ in one step.

Given an interaction (Hamiltonian) and [[thermodynamics/inverse-temperature-beta|inverse temperature $\beta$]], the *Gibbsian* specification has the familiar Boltzmann form: for each finite $\Lambda$ and boundary condition $\eta$,
$$
\gamma_\Lambda(d\sigma_\Lambda\mid \eta_{\Lambda^c})
=\frac{1}{Z_\Lambda(\eta_{\Lambda^c})}\,
\exp\!\big(-\beta\,H_\Lambda(\sigma_\Lambda\mid \eta_{\Lambda^c})\big)\,
\rho_\Lambda(d\sigma_\Lambda),
$$

where $H_\Lambda(\sigma_\Lambda\mid \eta_{\Lambda^c})$ is the energy contribution involving sites in $\Lambda$ (including interactions across the boundary), $\rho_\Lambda$ is a reference product measure on $S^\Lambda$ (counting measure for discrete spins, Lebesgue-type for continuous variables), and $Z_\Lambda(\eta_{\Lambda^c})$ is the finite-volume normalizing partition function.

This is the “finite-volume equilibrium given the boundary” analogue of the [[stat-mech/canonical-ensemble|canonical ensemble]].

## Definition (Gibbs measure via the DLR equations)
A probability measure $\mu$ on $\Omega$ is an **infinite-volume Gibbs measure** for the specification $\gamma$ if for every finite $\Lambda$ and every measurable event $A$,
$$
\mu(A)=\int_\Omega \gamma_\Lambda(A\mid \omega)\,\mu(d\omega).
$$

Equivalently: the conditional distribution of $\omega_\Lambda$ given $\omega_{\Lambda^c}$ under $\mu$ is exactly $\gamma_\Lambda(\,\cdot\,|\omega)$, for $\mu$-almost every outside configuration $\omega$.

## Physical interpretation
The DLR equations formalize *local equilibrium*: any finite region $\Lambda$ behaves as if it were in contact with a heat bath at $\beta$, with the exterior configuration acting as a boundary field. Multiple Gibbs measures solving the same DLR equations correspond to distinct thermodynamic phases (different boundary conditions can select different solutions), and they can be constructed concretely using the [[stat-mech/construction-infinite-volume-gibbs-weak-limit|weak-limit construction of infinite-volume Gibbs measures]].
