---
title: "DLR existence theorem"
description: "For a lattice interaction defining a Gibbs specification, there exists at least one infinite-volume Gibbs measure satisfying the DLR equations."
---

## Statement

Let $\Phi$ be a translation-invariant interaction (potential) on $\mathbb{Z}^d$ with finite single-spin space $S$ (e.g. $S=\{\pm 1\}$) and assume $\Phi$ is **uniformly absolutely summable** (in particular, any finite-range interaction qualifies). Let $\gamma^\Phi$ be the associated {{< knowl id="gibbs-specification" section="stat-mech-lattice" text="Gibbs specification" >}} constructed from the {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}.

Then the set of {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} consistent with $\gamma^\Phi$ is nonempty. Equivalently, there exists at least one probability measure $\mu$ on $\Omega=S^{\mathbb{Z}^d}$ such that $\mu$ satisfies the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}} for every finite $\Lambda\Subset\mathbb{Z}^d$.

Moreover, for any fixed boundary condition $\eta$ and any increasing sequence of finite volumes $\Lambda_n\uparrow\mathbb{Z}^d$, every weak limit point of the corresponding {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}} $\mu_{\Lambda_n}^{\eta}$ is an infinite-volume Gibbs measure for $\Phi$.

## Key hypotheses

- **Configuration space:** $\Omega=S^{\mathbb{Z}^d}$ with $S$ finite (or more generally compact Polish).
- **Interaction:** $\Phi$ is translation-invariant and uniformly absolutely summable (e.g. finite range).
- **Specification:** $\gamma^\Phi$ is the Gibbs specification induced by $\Phi$ (quasilocal, consistent, proper).

(Probability-theoretic background: $\mu$ is a {{< knowl id="probability-measure" section="probability" text="probability measure" >}} on $(\Omega,\mathcal{F})$.)

## Key conclusions

- **Existence:** $\mathcal{G}(\gamma^\Phi)\neq\varnothing$, where $\mathcal{G}(\gamma^\Phi)$ denotes the set of $\mu$ satisfying the {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}.
- **Compactness mechanism:** the family $\{\mu_{\Lambda}^{\eta}\}_{\Lambda\Subset\mathbb{Z}^d}$ has weakly convergent subnet/subsequence along any exhaustion, and each limit point is in $\mathcal{G}(\gamma^\Phi)$.
- **Equilibrium exists at all parameters:** for every inverse temperature (absorbed into $\Phi$) and external parameters appearing in $\Phi$, at least one infinite-volume equilibrium state exists.

