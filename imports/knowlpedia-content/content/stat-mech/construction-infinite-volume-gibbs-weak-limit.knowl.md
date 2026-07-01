+++
id = "stat-mech/construction-infinite-volume-gibbs-weak-limit"
title = "Infinite-volume Gibbs measure as a weak limit"
kind = "knowl"
summary = "Construct an infinite equilibrium state by taking weak limits of finite-volume Gibbs measures along increasing regions."
aliases = ["construction-infinite-volume-gibbs-weak-limit", "Infinite-volume Gibbs measure as a weak limit"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/construction-infinite-volume-gibbs-weak-limit.md"
+++

One common way to realize the [[thermodynamics/thermodynamic-limit|thermodynamic limit]] on a lattice is to start from finite boxes and pass to an infinite-volume limit in the sense of weak convergence of measures. This produces an infinite-volume Gibbs measure and connects directly to the [[stat-mech/construction-dlr-specification|DLR specification]].

## Finite-volume Gibbs measures with boundary conditions
Fix [[thermodynamics/inverse-temperature-beta|inverse temperature $\beta$]] and a boundary condition $\eta\in\Omega=S^{\mathbb{Z}^d}$ on the [[discrete-structures/lattice-zd|lattice $\mathbb{Z}^d$]]. For a [[discrete-structures/finite-box-lattice|finite box $\Lambda\subset\mathbb{Z}^d$]], define the finite-volume Gibbs measure on configurations in $\Lambda$ by
$$
\mu_\Lambda^\eta(d\sigma_\Lambda)
=\frac{1}{Z_\Lambda(\eta_{\Lambda^c})}\,
\exp\!\big(-\beta\,H_\Lambda(\sigma_\Lambda\mid \eta_{\Lambda^c})\big)\,
\rho_\Lambda(d\sigma_\Lambda).
$$

To view $\mu_\Lambda^\eta$ as a measure on the full space $\Omega$, one extends it by fixing the outside configuration to $\eta$ (so all randomness lives inside $\Lambda$). This is the finite-volume “equilibrium state given the boundary,” and it is precisely the kernel appearing in the [[stat-mech/construction-dlr-specification|DLR specification]].

## Weak limits along increasing volumes
Let $\Lambda_1\subset \Lambda_2\subset\cdots$ be an increasing exhaustion of $\mathbb{Z}^d$ by finite boxes (often centered cubes). A probability measure $\mu$ on $\Omega$ is a **weak limit point** of $\{\mu_{\Lambda_n}^\eta\}$ if there exists a subsequence $n_k$ such that
$$
\int f(\omega)\,\mu_{\Lambda_{n_k}}^\eta(d\omega)\;\longrightarrow\;\int f(\omega)\,\mu(d\omega)
\quad\text{for every bounded local observable }f.
$$

Here “local” means $f$ depends only on finitely many sites, so its [[stat-mech/ensemble-average|ensemble average]] probes a fixed finite window while the volume grows.

For finite single-site spaces $S$ (e.g. spin systems with $S=\{\pm1\}$), the configuration space $\Omega$ is compact in the product topology, and one can extract subsequential weak limits by standard compactness arguments. In more general settings (e.g. unbounded spins), additional tightness estimates are needed, but the goal is the same: produce an infinite-volume measure whose finite-window statistics stabilize.

## Resulting infinite-volume Gibbs measures
Any weak limit point $\mu$ of $\{\mu_{\Lambda_n}^\eta\}$ is an **infinite-volume Gibbs measure** for the same interaction, in the sense that it satisfies the DLR equations with the associated specification. Concretely, for every finite $\Lambda$ the conditional distribution of $\omega_\Lambda$ given $\omega_{\Lambda^c}$ under $\mu$ agrees with the corresponding Gibbs kernel from the [[stat-mech/construction-dlr-specification|DLR specification]].

## Physical interpretation: boundary selection and phases
- If the infinite-volume Gibbs measure is **unique**, then the weak limit does not depend on boundary conditions (plus, minus, periodic, etc.), and long-distance behavior is insensitive to how the system is closed off.
- If there are **multiple** Gibbs measures, different boundaries can yield different weak limits; this is one mathematical expression of phase coexistence. Such non-uniqueness is reflected in long-range behavior of the [[stat-mech/correlation-function-two-point|two-point correlation function]], the [[stat-mech/correlation-length|correlation length]], and response coefficients such as the [[stat-mech/susceptibility-stat-mech|susceptibility]].
