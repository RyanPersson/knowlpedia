---
title: "Dobrushin uniqueness theorem"
description: "A quantitative small-dependence condition on single-site conditional distributions implies uniqueness of the infinite-volume Gibbs measure and strong mixing."
---

## Statement

Let $\gamma$ be a {{< knowl id="gibbs-specification" section="stat-mech-lattice" text="Gibbs specification" >}} on $\Omega=S^{\mathbb{Z}^d}$ with finite single-spin space $S$. For each site $i\in\mathbb{Z}^d$, write $\gamma_i(\cdot\mid\omega)$ for the single-site conditional distribution at $i$ given the external configuration $\omega$.

Define the **Dobrushin influence coefficients**
$$
C_{ij}
:=
\sup_{\substack{\omega,\omega'\in\Omega\\ \omega_k=\omega'_k\ \forall k\neq j}}
\big\|\gamma_i(\cdot\mid\omega)-\gamma_i(\cdot\mid\omega')\big\|_{\mathrm{TV}},
$$

where $\|\cdot\|_{\mathrm{TV}}$ denotes total variation distance.

If the **Dobrushin constant**
$$
\alpha := \sup_{i\in\mathbb{Z}^d}\ \sum_{j\neq i} C_{ij}
$$

satisfies $\alpha<1$, then there exists a **unique** {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measure" >}} $\mu$ consistent with $\gamma$ (equivalently, there is a unique $\mu$ satisfying the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}).

In addition, the unique Gibbs state enjoys strong mixing properties; in particular, boundary-condition influence decays quantitatively with distance, yielding (as a consequence) exponential correlation decay as formalized in {{< knowl id="exponential-decay-correlations-uniqueness" text="exponential decay of correlations in the uniqueness regime" >}}.

## Key hypotheses

- **Finite spin space:** $S$ finite (so single-site conditionals are uniformly well-behaved).
- **Quasilocal specification:** $\gamma$ is a genuine Gibbs specification arising from some {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}} (or at least satisfies the usual measurability/properness/consistency conditions).
- **Small interdependence:** $\alpha<1$ for the influence matrix $(C_{ij})$.

## Key conclusions

- **Uniqueness:** there is exactly one $\mu$ consistent with $\gamma$.
- **High-temperature regime:** for many concrete models (e.g. {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising" >}} with small $\beta J$), one can bound $C_{ij}$ explicitly and verify $\alpha<1$.
- **Quantitative mixing:** local expectations are stable under far-away boundary perturbations, with explicit bounds in terms of $(C_{ij})$.
## significance

One constructs a “single-site update” operator on the space of probability measures (or on the space of boundary conditions), and shows it is a contraction in an appropriate metric when $\alpha<1$. The coefficients $C_{ij}$ quantify how much flipping the spin at $j$ can change the conditional law at $i$; the condition $\sup_i\sum_j C_{ij}<1$ forces influence to die out under iteration.

This theorem is a standard, robust criterion for the **uniqueness** of equilibrium at high temperature and is often the entry point to analyticity and exponential mixing results.