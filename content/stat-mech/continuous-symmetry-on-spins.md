---
title: "Continuous symmetries in spin systems"
description: "Spin models with global continuous symmetry (e.g., O(n), U(1)) and the consequences for phases, correlations, and symmetry breaking."
---

A lattice spin system has a **continuous symmetry** when its Hamiltonian is invariant under a continuous group of transformations acting on all spins simultaneously. This changes what kinds of ordered phases can exist and how correlations behave, especially in low spatial dimensions.

## Definition (global continuous symmetry)
Let $\Lambda$ be a lattice and spins $\sigma_i$ take values in a continuous manifold (e.g., $\sigma_i \in S^{n-1}\subset \mathbb{R}^n$). A typical nearest-neighbor Hamiltonian is
$$
H(\sigma) = -\sum_{\langle i,j\rangle} J_{ij}\, \sigma_i\cdot \sigma_j - \sum_{i\in\Lambda} h\cdot \sigma_i .
$$

For $h=0$, this Hamiltonian is invariant under the action of the group $G=O(n)$:
$$
H(g\sigma) = H(\sigma)\quad\text{for all }g\in O(n),
$$

where $(g\sigma)_i = g\,\sigma_i$.  
Special cases:
- **XY model**: $n=2$, symmetry group includes $SO(2)\cong U(1)$ (continuous rotations in the plane).
- **Heisenberg model**: $n=3$, symmetry group includes $SO(3)$.

This is the natural setting for {{< knowl id="spontaneous-symmetry-breaking-group" section="stat-mech-lattice" text="spontaneous symmetry breaking" >}} in models with non-discrete symmetries.

## Consequences for order and correlations
### Order parameter and symmetry
A natural {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}} is the magnetization
$$
m(\sigma)=\frac{1}{|\Lambda|}\sum_{i\in\Lambda}\sigma_i.
$$

In a symmetry-broken phase at zero field, typical infinite-volume states have nonzero $\langle m\rangle$ but the full Gibbs measure may be a mixture of rotated pure states.

### Goldstone modes (heuristic)
If a continuous symmetry is broken, slowly varying rotations of the local orientation cost little energy, producing long-wavelength modes and strong fluctuations. These fluctuations strongly constrain long-range order in low dimensions.

### Low-dimensional obstruction (key theorem)
For short-range, sufficiently regular interactions and continuous symmetries, the {{< knowl id="mermin-wagner-theorem" text="Mermin–Wagner theorem" >}} rules out spontaneous breaking of such symmetries in $d\le 2$ (at positive temperature). A common signature is that the two-point {{< knowl id="correlation-function-two-point" section="stat-mech" text="correlation function" >}} fails to approach a nonzero constant as $|i-j|\to\infty$.

### Quasi-long-range order and topological defects
In the 2D XY model, one can have power-law decay of correlations (no true long-range order) and a transition driven by unbinding of vortices; see {{< knowl id="kosterlitz-thouless-transition" text="Kosterlitz–Thouless transition" >}} and {{< knowl id="topological-defect-vortex" text="vortices" >}}.

## Prerequisites
- {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonians" >}}
- {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}} and {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}
- {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}}
