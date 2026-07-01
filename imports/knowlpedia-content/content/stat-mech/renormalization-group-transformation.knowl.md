+++
id = "stat-mech/renormalization-group-transformation"
title = "Renormalization-group (RG) transformations"
kind = "knowl"
summary = "Coarse-graining maps of models to effective models at larger scales; fixed points, relevance/irrelevance, and extraction of critical exponents."
aliases = ["renormalization-group-transformation", "Renormalization-group (RG) transformations"]
domains = ["stat-mech"]
legacy_source_path = "stat-mech/renormalization-group-transformation.md"
+++

A **renormalization-group (RG) transformation** is a procedure that (i) coarse-grains microscopic degrees of freedom and (ii) rescales lengths so the system can be compared across scales. Iterating this transformation produces a flow in the space of Hamiltonians/couplings, organizing phases and critical behavior.

## Definition (conceptual)
An RG map at scale factor $b>1$ is a transformation
$$
R_b:\ \text{(microscopic model)}\ \longrightarrow\ \text{(effective model)}
$$
so that long-distance observables (correlations, free energy density, etc.) are approximately preserved after:
1. **Blocking / coarse-graining** (integrate out or average short-scale degrees of freedom),
2. **Rescaling** of lengths to restore the original lattice spacing,
3. **Parameter read-off** (express the coarse-grained model in the same family with new couplings).

In coupling coordinates $K=(K_1,K_2,\dots)$, one writes
$$
K' = R_b(K).
$$

## Fixed points and universality
A point $K^\star$ with
$$
R_b(K^\star)=K^\star
$$
is an [[stat-mech/rg-fixed-point|RG fixed point]]. Fixed points control scaling limits:
- **Stable** fixed points describe phases (attractive under iteration).
- **Critical** fixed points separate phases and control universal singularities.

This is the RG basis for [[stat-mech/universality-class|universality classes]].

## Linearization and critical exponents
Linearize near a fixed point:
$$
K' - K^\star \approx DR_b(K^\star)\,(K-K^\star).
$$

If $v_i$ is an eigenvector with eigenvalue $\lambda_i$, write $\lambda_i=b^{y_i}$:
- $y_i>0$: **relevant** direction (grows under coarse-graining),
- $y_i<0$: **irrelevant** direction (decays),
- $y_i=0$: **marginal** (needs higher-order analysis).

A standard identification is $\nu=1/y_t$, where $y_t$ is the eigenvalue exponent associated with the thermal perturbation (moving away from critical temperature). This links RG to [[stat-mech/critical-exponent|critical exponents]] and to [[stat-mech/scaling-relation-exponents|scaling relations]].

## Concrete example: block-spin RG (Ising-type intuition)
For the [[stat-mech-lattice/ising-model|Ising model]] on $\mathbb{Z}^d$, a block-spin map partitions the lattice into $b^d$-site blocks and defines a coarse spin (e.g., majority rule). Integrating out microscopic spins inside blocks produces effective couplings between block spins, generating the flow $K\mapsto K'$.

## Prerequisites
- [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonians]]
- [[stat-mech-lattice/phase-transition-gibbs|phase transitions (Gibbs perspective)]]
- [[stat-mech/critical-point-phase-diagram|critical points in phase diagrams]]
