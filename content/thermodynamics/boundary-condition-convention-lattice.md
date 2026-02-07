---
title: "Boundary condition convention for lattice systems"
description: "Common boundary condition choices for finite lattice models and how they affect finite-volume definitions."
---

In lattice statistical mechanics one typically defines a finite system by restricting an infinite lattice (such as \(\mathbb{Z}^d\)) to a finite region \(\Lambda\subset \mathbb{Z}^d\). To make the Hamiltonian and the finite-volume Gibbs measure well-defined, one must specify **boundary conditions** (often abbreviated "b.c."), i.e. a rule for how degrees of freedom at or outside \(\partial\Lambda\) are treated.

A standard finite-volume Gibbs measure with boundary condition \(\mathrm{bc}\) is written
$$
\mu_{\Lambda}^{\mathrm{bc}}(\sigma)
\;=\;
\frac{1}{Z_{\Lambda}^{\mathrm{bc}}}\exp\!\bigl(-\beta H_{\Lambda}^{\mathrm{bc}}(\sigma)\bigr),
\qquad
Z_{\Lambda}^{\mathrm{bc}}=\sum_{\sigma}\exp\!\bigl(-\beta H_{\Lambda}^{\mathrm{bc}}(\sigma)\bigr),
$$
where \(\sigma\) ranges over configurations on \(\Lambda\) (for example \(\sigma:\Lambda\to\{\pm 1\}\) in the Ising model).

### Common conventions
1. **Periodic boundary conditions (PBC).**
   Identify opposite faces of the finite box so that \(\Lambda\) becomes a discrete torus, e.g. \((\mathbb{Z}/L\mathbb{Z})^d\). Nearest-neighbor interactions "wrap around." This reduces boundary effects and preserves translation invariance.

2. **Free/open boundary conditions.**
   Only include interactions entirely inside \(\Lambda\). Boundary sites then have fewer interacting neighbors (no coupling to outside sites).

3. **Fixed boundary conditions.**
   Fix spins (or other degrees of freedom) outside \(\Lambda\) to a prescribed value or configuration, e.g. all \(+\) or all \(-\) in the Ising model. This is often used to select a phase or to study interfaces.

4. **Mixed or patterned boundary conditions.**
   Different parts of the boundary are fixed differently (e.g. \(+\) on one side, \(-\) on the other), or a boundary field is imposed.

5. **Twisted/antiperiodic boundary conditions.**
   Modify the wrap-around rule by a sign or twist; used to probe domain walls, topological sectors, or fermionic parity effects in certain models.

### Relation to the thermodynamic limit
For many short-range, translation-invariant models, the **free energy per site** (and other bulk thermodynamic quantities) converge to a limit that does not depend on the boundary condition, provided the boundary-to-volume ratio vanishes along the chosen sequence of regions. See {{< knowl id="thermodynamic-limit-convention" text="thermodynamic limit convention" >}} for the standard scaling limit in which boundary effects become negligible.
