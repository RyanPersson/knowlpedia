+++
id = "stat-mech-lattice/dlr-existence-theorem"
title = "DLR existence theorem"
kind = "knowl"
summary = "For a lattice interaction defining a Gibbs specification, there exists at least one infinite-volume Gibbs measure satisfying the DLR equations."
aliases = ["dlr-existence-theorem", "DLR existence theorem"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/dlr-existence-theorem.md"
+++

## Statement

Let $\Phi$ be a translation-invariant interaction (potential) on $\mathbb{Z}^d$ with finite single-spin space $S$ (e.g. $S=\{\pm 1\}$) and assume $\Phi$ is **uniformly absolutely summable** (in particular, any finite-range interaction qualifies). Let $\gamma^\Phi$ be the associated [[stat-mech-lattice/gibbs-specification|Gibbs specification]] constructed from the [[stat-mech-lattice/lattice-hamiltonian|lattice Hamiltonian]].

Then the set of [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] consistent with $\gamma^\Phi$ is nonempty. Equivalently, there exists at least one probability measure $\mu$ on $\Omega=S^{\mathbb{Z}^d}$ such that $\mu$ satisfies the [[stat-mech-lattice/dlr-equation|DLR equation]] for every finite $\Lambda\Subset\mathbb{Z}^d$.

Moreover, for any fixed boundary condition $\eta$ and any increasing sequence of finite volumes $\Lambda_n\uparrow\mathbb{Z}^d$, every weak limit point of the corresponding [[stat-mech-lattice/finite-volume-gibbs-measure|finite-volume Gibbs measures]] $\mu_{\Lambda_n}^{\eta}$ is an infinite-volume Gibbs measure for $\Phi$.

## Key hypotheses

- **Configuration space:** $\Omega=S^{\mathbb{Z}^d}$ with $S$ finite (or more generally compact Polish).
- **Interaction:** $\Phi$ is translation-invariant and uniformly absolutely summable (e.g. finite range).
- **Specification:** $\gamma^\Phi$ is the Gibbs specification induced by $\Phi$ (quasilocal, consistent, proper).

(Probability-theoretic background: $\mu$ is a [[probability/probability-measure|probability measure]] on $(\Omega,\mathcal{F})$.)

## Key conclusions

- **Existence:** $\mathcal{G}(\gamma^\Phi)\neq\varnothing$, where $\mathcal{G}(\gamma^\Phi)$ denotes the set of $\mu$ satisfying the [[stat-mech-lattice/dlr-equation|DLR equation]].
- **Compactness mechanism:** the family $\{\mu_{\Lambda}^{\eta}\}_{\Lambda\Subset\mathbb{Z}^d}$ has weakly convergent subnet/subsequence along any exhaustion, and each limit point is in $\mathcal{G}(\gamma^\Phi)$.
- **Equilibrium exists at all parameters:** for every inverse temperature (absorbed into $\Phi$) and external parameters appearing in $\Phi$, at least one infinite-volume equilibrium state exists.
