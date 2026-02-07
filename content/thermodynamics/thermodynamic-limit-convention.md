---
title: "Thermodynamic limit convention"
description: "Standard convention for taking particle number and volume to infinity while keeping density fixed."
---

The **thermodynamic limit** is the standard scaling limit used to define bulk (infinite-system) thermodynamic quantities from finite systems.

### Continuum convention (particles in a volume)
For a system of \(N\) particles in volume \(V\), the thermodynamic limit is taken as
$$
N \to \infty,\qquad V \to \infty,\qquad \frac{N}{V} \to \rho,
$$
where \(\rho\) is the fixed particle density. Intensive parameters such as temperature \(T\) (equivalently \(\beta=1/(k_BT)\)) and external fields are held fixed.

One typically defines bulk quantities as limits of densities, for example the free energy density (or free energy per particle) when the limit exists:
$$
f(\beta,\rho)
={}
\lim_{N,V\to\infty\atop N/V\to\rho}\frac{F_{N,V}(\beta)}{V}
={}
-\frac{1}{\beta}\lim_{N,V\to\infty\atop N/V\to\rho}\frac{1}{V}\ln Z_{N,V}(\beta).
$$
By convention, \(\ln\) is the natural logarithm; see {{< knowl id="logarithm-convention-natural" text="natural logarithm convention" >}}.

### Lattice convention (finite regions growing to infinity)
For lattice models on \(\mathbb{Z}^d\), one takes a sequence of finite regions \(\Lambda_1\subset \Lambda_2\subset \cdots\) with \(|\Lambda_n|\to\infty\). A common regularity requirement is that boundary effects vanish in proportion to volume, e.g.
$$
\frac{|\partial \Lambda_n|}{|\Lambda_n|} \to 0,
$$
for an appropriate notion of boundary \(\partial\Lambda_n\) (a "van Hove" type condition).

Bulk free energy per site is then defined by
$$
f(\beta) = -\frac{1}{\beta}\lim_{n\to\infty}\frac{1}{|\Lambda_n|}\ln Z_{\Lambda_n}.
$$

### Boundary conditions and the limit
Finite-volume quantities depend on the choice of boundary condition, but for many short-range models the thermodynamic limit of bulk densities (when it exists) is independent of boundary conditions along regular sequences of regions. See {{< knowl id="boundary-condition-convention-lattice" text="boundary condition convention for lattice systems" >}}.
