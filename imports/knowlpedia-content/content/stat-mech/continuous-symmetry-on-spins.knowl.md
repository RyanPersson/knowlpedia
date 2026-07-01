+++
id = "stat-mech/continuous-symmetry-on-spins"
title = "Continuous symmetries in spin systems"
kind = "knowl"
summary = "Spin models with global continuous symmetry (e.g., O(n), U(1)) and the consequences for phases, correlations, and symmetry breaking."
aliases = ["continuous-symmetry-on-spins", "Continuous symmetries in spin systems"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/continuous-symmetry-on-spins.md"
+++

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

This is the natural setting for [[stat-mech-lattice/spontaneous-symmetry-breaking-group|spontaneous symmetry breaking]] in models with non-discrete symmetries.

## Consequences for order and correlations
### Order parameter and symmetry
A natural [[stat-mech-lattice/order-parameter|order parameter]] is the magnetization
$$
m(\sigma)=\frac{1}{|\Lambda|}\sum_{i\in\Lambda}\sigma_i.
$$

In a symmetry-broken phase at zero field, typical infinite-volume states have nonzero $\langle m\rangle$ but the full Gibbs measure may be a mixture of rotated pure states.

### Goldstone modes (heuristic)
If a continuous symmetry is broken, slowly varying rotations of the local orientation cost little energy, producing long-wavelength modes and strong fluctuations. These fluctuations strongly constrain long-range order in low dimensions.

### Low-dimensional obstruction (key theorem)
For short-range, sufficiently regular interactions and continuous symmetries, the [[stat-mech/mermin-wagner-theorem|Mermin–Wagner theorem]] rules out spontaneous breaking of such symmetries in $d\le 2$ (at positive temperature). A common signature is that the two-point [[stat-mech/correlation-function-two-point|correlation function]] fails to approach a nonzero constant as $|i-j|\to\infty$.

### Quasi-long-range order and topological defects
In the 2D XY model, one can have power-law decay of correlations (no true long-range order) and a transition driven by unbinding of vortices; see [[stat-mech/kosterlitz-thouless-transition|Kosterlitz–Thouless transition]] and [[stat-mech/topological-defect-vortex|vortices]].

## Prerequisites
- [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonians]]
- [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]] and [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]]
- [[stat-mech/correlation-length|correlation length]]
