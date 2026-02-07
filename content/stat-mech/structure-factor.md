---
title: "Structure factor"
description: "The Fourier-space measure of spatial correlations (static structure factor), central to scattering and to diagnosing order and criticality."
---

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
- **Criticality:** Near a critical point, growth of long-range correlations appears as a strong enhancement of $S(k)$ at small $|k|$, controlled by the {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} and the anomalous dimension $\eta$.

## Ornstein–Zernike form (common approximation)
If correlations decay roughly as $C(r)\sim e^{-r/\xi}$ away from criticality, then for small $|k|$ one often has the Ornstein–Zernike-like behavior
$$
S(k)\approx \frac{\chi}{1+(|k|\xi)^2},
$$

where $\chi=S(0)$ is the susceptibility (again up to conventions). See {{< knowl id="ornstein-zernike-form" text="Ornstein–Zernike form" >}} for context and refinements.

## Prerequisites / cross-links
- {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlation function" >}}
- {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}
- {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}
- {{< knowl id="ornstein-zernike-form" text="Ornstein–Zernike form" >}}
- {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}
