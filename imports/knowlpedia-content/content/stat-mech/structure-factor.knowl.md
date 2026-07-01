+++
id = "stat-mech/structure-factor"
title = "Structure factor"
kind = "knowl"
summary = "The Fourier-space measure of spatial correlations (static structure factor), central to scattering and to diagnosing order and criticality."
aliases = ["structure-factor", "Structure factor"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/structure-factor.md"
+++

## Definition (static structure factor)
Let $A_x$ be a local observable on a lattice or continuum (e.g., spin component, particle density). The **connected** two-point correlation function is
$$
C(x-y)=\langle A_x A_y\rangle - \langle A_x\rangle\langle A_y\rangle.
$$

When the state is translation-invariant, the **static structure factor** is the Fourier transform of $C$:
$$
S(k)=\sum_{r} e^{ik\cdot r}\,C(r)
$$

(on a lattice, sum over $r$; in the continuum, replace by an integral with the appropriate convention). In finite volume with $N$ lattice sites, an equivalent normalization often used is
$$
S(k)=\frac{1}{N}\sum_{x,y} e^{ik\cdot(x-y)}\Big(\langle A_x A_y\rangle - \langle A\rangle^2\Big).
$$

## Interpretation and key uses
- **Scattering:** For density observables, $S(k)$ is (up to conventions) proportional to the intensity measured in X-ray/neutron scattering at momentum transfer $k$.
- **Order detection:** Long-range order produces sharp features (Bragg peaks) in $S(k)$ at ordering wavevectors.
- **Criticality:** Near a critical point, growth of long-range correlations appears as a strong enhancement of $S(k)$ at small $|k|$, controlled by the [[stat-mech/correlation-length|correlation length]] and the anomalous dimension $\eta$.

## Ornstein–Zernike form (common approximation)
If correlations decay roughly as $C(r)\sim e^{-r/\xi}$ away from criticality, then for small $|k|$ one often has the Ornstein–Zernike-like behavior
$$
S(k)\approx \frac{\chi}{1+(|k|\xi)^2},
$$

where $\chi=S(0)$ is the susceptibility (again up to conventions). See [[stat-mech/ornstein-zernike-form|Ornstein–Zernike form]] for context and refinements.

## Prerequisites / cross-links
- [[stat-mech/correlation-function-two-point|two-point correlation function]]
- [[stat-mech/correlation-length|correlation length]]
- [[stat-mech-lattice/order-parameter|order parameter]]
- [[stat-mech/ornstein-zernike-form|Ornstein–Zernike form]]
- [[stat-mech-lattice/ising-model|Ising model]]
