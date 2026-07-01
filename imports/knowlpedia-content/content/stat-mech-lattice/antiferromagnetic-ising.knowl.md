+++
id = "stat-mech-lattice/antiferromagnetic-ising"
title = "Antiferromagnetic Ising model"
kind = "knowl"
summary = "Nearest-neighbor Ising spin system with couplings that favor antiparallel alignment, leading to Néel (staggered) order on bipartite lattices."
aliases = ["antiferromagnetic-ising", "Antiferromagnetic Ising model"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/antiferromagnetic-ising.md"
+++

The **antiferromagnetic Ising model** is a special case of the [[stat-mech-lattice/ising-model|Ising model]] in which the interaction energetically favors *opposite* spins on neighboring sites.

Let $\Lambda$ be a finite subset of $\mathbb{Z}^d$ with the usual [[discrete-structures/nearest-neighbor-zd|nearest-neighbor adjacency]] (or more generally a finite graph). A [[stat-mech-lattice/spin-configuration|spin configuration]] is a map $\sigma:\Lambda\to\{-1,+1\}$ (so the [[stat-mech-lattice/spin-space|spin space]] is $\{-1,+1\}$). With a [[stat-mech-lattice/boundary-condition-lattice|boundary condition]] $\eta$ on $\Lambda^c$, the standard nearest-neighbor antiferromagnetic [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]] is
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

where $h$ is an [[stat-mech-lattice/external-field-coupling|external field]] and $\langle x,y\rangle$ denotes a nearest-neighbor edge.

At [[thermodynamics/inverse-temperature-beta|inverse temperature]] $\beta$, the corresponding [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measure]] is
$$
\mu_{\Lambda,\beta}^{\eta}(\sigma)
={}
\frac{1}{Z_{\Lambda,\beta}(\eta)}\exp\!\big(-\beta H_\Lambda(\sigma\mid\eta)\big),
$$

where $Z_{\Lambda,\beta}(\eta)$ is the [[stat-mech-lattice/partition-function-lattice|partition function]].

## Key properties

- **Local energetic preference (antialignment).** Since $J>0$ multiplies $\sigma_x\sigma_y$, an edge contributes lower energy when $\sigma_x\sigma_y=-1$, i.e. neighboring spins are opposite.

- **Bipartite lattices and Néel order.** On a bipartite lattice (e.g. $\mathbb{Z}^d$), the ground states are the two “checkerboard” configurations (Néel states) obtained by fixing opposite spins on the two sublattices. The natural [[stat-mech-lattice/order-parameter|order parameter]] is the *staggered magnetization*
  $$
  m_{\mathrm{stag}}(\sigma)=\frac{1}{|\Lambda|}\sum_{x\in\Lambda}\varepsilon_x\,\sigma_x,
  $$

  where $\varepsilon_x=\pm 1$ records the sublattice (for $\mathbb{Z}^d$, one choice is $\varepsilon_x=(-1)^{x_1+\cdots+x_d}$).

- **Gauge transform at zero field (bipartite case).** When $h=0$ and the underlying graph is bipartite, flipping all spins on one sublattice maps the antiferromagnetic model to a [[stat-mech-lattice/ferromagnetic-ising|ferromagnetic Ising model]] (up to an additive constant in the energy). This equivalence generally fails when $h\neq 0$.

- **Frustration on non-bipartite graphs.** On non-bipartite lattices (e.g. triangular lattice), not all edges can be simultaneously satisfied; this produces *frustration* and can lead to highly degenerate ground states and altered (or suppressed) ordering behavior.

- **Phase transitions and symmetry breaking.** In dimensions $d\ge 2$ (and for sufficiently short-range interactions), the antiferromagnetic model on a bipartite lattice typically exhibits a low-temperature ordered phase characterized by nonzero staggered magnetization and [[stat-mech-lattice/spontaneous-symmetry-breaking|spontaneous symmetry breaking]] in the infinite-volume limit, formulated via [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] and [[stat-mech-lattice/phase-transition-gibbs|phase transitions]].

## Physical interpretation

The antiferromagnetic Ising model is a minimal model for **antiferromagnets**, where neighboring magnetic moments prefer to point in opposite directions due to exchange interactions. On bipartite lattices this produces **Néel order** (alternating sublattice magnetization). Unlike the ferromagnetic case, the usual uniform [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]] can vanish even in an ordered phase; the physically meaningful “magnetization” is staggered.
