---
title: "Antiferromagnetic Ising model"
description: "Nearest-neighbor Ising spin system with couplings that favor antiparallel alignment, leading to Néel (staggered) order on bipartite lattices."
---


The **antiferromagnetic Ising model** is a special case of the {{< knowl id="ising-model" text="Ising model" >}} in which the interaction energetically favors *opposite* spins on neighboring sites.

Let $\Lambda$ be a finite subset of $\mathbb{Z}^d$ with the usual {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor adjacency" >}} (or more generally a finite graph). A {{< knowl id="spin-configuration" text="spin configuration" >}} is a map $\sigma:\Lambda\to\{-1,+1\}$ (so the {{< knowl id="spin-space" text="spin space" >}} is $\{-1,+1\}$). With a {{< knowl id="boundary-condition-lattice" text="boundary condition" >}} $\eta$ on $\Lambda^c$, the standard nearest-neighbor antiferromagnetic {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}} is
$$
H_\Lambda(\sigma\mid \eta)
={}
J\sum_{\langle x,y\rangle:\, x,y\in\Lambda}\sigma_x\sigma_y
+
J\sum_{\substack{\langle x,y\rangle:\\ x\in\Lambda,\,y\notin\Lambda}}\sigma_x\eta_y
-{}
h\sum_{x\in\Lambda}\sigma_x,
\qquad J>0,
$$

where $h$ is an {{< knowl id="external-field-coupling" text="external field" >}} and $\langle x,y\rangle$ denotes a nearest-neighbor edge.

At {{< knowl id="inverse-temperature-beta" section="thermodynamics" text="inverse temperature" >}} $\beta$, the corresponding {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} is
$$
\mu_{\Lambda,\beta}^{\eta}(\sigma)
={}
\frac{1}{Z_{\Lambda,\beta}(\eta)}\exp\!\big(-\beta H_\Lambda(\sigma\mid\eta)\big),
$$

where $Z_{\Lambda,\beta}(\eta)$ is the {{< knowl id="partition-function-lattice" text="partition function" >}}.

## Key properties

- **Local energetic preference (antialignment).** Since $J>0$ multiplies $\sigma_x\sigma_y$, an edge contributes lower energy when $\sigma_x\sigma_y=-1$, i.e. neighboring spins are opposite.

- **Bipartite lattices and Néel order.** On a bipartite lattice (e.g. $\mathbb{Z}^d$), the ground states are the two “checkerboard” configurations (Néel states) obtained by fixing opposite spins on the two sublattices. The natural {{< knowl id="order-parameter" text="order parameter" >}} is the *staggered magnetization*
  $$
  m_{\mathrm{stag}}(\sigma)=\frac{1}{|\Lambda|}\sum_{x\in\Lambda}\varepsilon_x\,\sigma_x,
  $$

  where $\varepsilon_x=\pm 1$ records the sublattice (for $\mathbb{Z}^d$, one choice is $\varepsilon_x=(-1)^{x_1+\cdots+x_d}$).

- **Gauge transform at zero field (bipartite case).** When $h=0$ and the underlying graph is bipartite, flipping all spins on one sublattice maps the antiferromagnetic model to a {{< knowl id="ferromagnetic-ising" text="ferromagnetic Ising model" >}} (up to an additive constant in the energy). This equivalence generally fails when $h\neq 0$.

- **Frustration on non-bipartite graphs.** On non-bipartite lattices (e.g. triangular lattice), not all edges can be simultaneously satisfied; this produces *frustration* and can lead to highly degenerate ground states and altered (or suppressed) ordering behavior.

- **Phase transitions and symmetry breaking.** In dimensions $d\ge 2$ (and for sufficiently short-range interactions), the antiferromagnetic model on a bipartite lattice typically exhibits a low-temperature ordered phase characterized by nonzero staggered magnetization and {{< knowl id="spontaneous-symmetry-breaking" text="spontaneous symmetry breaking" >}} in the infinite-volume limit, formulated via {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} and {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}.

## Physical interpretation

The antiferromagnetic Ising model is a minimal model for **antiferromagnets**, where neighboring magnetic moments prefer to point in opposite directions due to exchange interactions. On bipartite lattices this produces **Néel order** (alternating sublattice magnetization). Unlike the ferromagnetic case, the usual uniform {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}} can vanish even in an ordered phase; the physically meaningful “magnetization” is staggered.

