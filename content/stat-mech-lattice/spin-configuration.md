---
title: "Spin configuration"
description: "A specification of spin values at each site of a lattice region (finite or infinite)."
---

Let $S$ be the {{< knowl id="spin-space" text="spin space" >}} and let $\Lambda$ be a set of lattice sites (often a finite box; see {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite box" >}} in the {{< knowl id="lattice-zd" section="discrete-structures" text="integer lattice" >}}).

A **spin configuration on** $\Lambda$ is a function
$$
\sigma_\Lambda : \Lambda \to S,
$$

assigning a spin value $\sigma_i \in S$ to each site $i\in\Lambda$. The set of all such configurations is $S^\Lambda$ (see {{< knowl id="configuration-space-lattice" text="configuration space" >}} for the infinite-volume analogue).

If $\Omega = S^{\mathbb{Z}^d}$ denotes the full configuration space, then:
- the **restriction** of a full configuration $\sigma\in\Omega$ to $\Lambda$ is denoted $\sigma_\Lambda$;
- given a boundary condition $\eta$ outside $\Lambda$ (see {{< knowl id="boundary-condition-lattice" text="boundary condition" >}}), one forms a combined configuration $\sigma_\Lambda \eta_{\Lambda^c}$ on the whole lattice by using $\sigma_\Lambda$ inside and $\eta$ outside.

## Key properties
- **Locality:** Many observables and energies depend only on finitely many coordinates of $\sigma$ (e.g. nearest-neighbor models; see {{< knowl id="nearest-neighbor-zd" section="discrete-structures" text="nearest-neighbor structure" >}}).
- **Gluing with boundary conditions:** Finite-volume energies and probabilities are naturally defined for $\sigma_\Lambda$ together with an exterior configuration $\eta_{\Lambda^c}$. This is central in the definition of the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} and in the {{< knowl id="dlr-equation" text="DLR equation" >}}.
- **Coordinate maps:** For each site $i$, the map $\sigma \mapsto \sigma_i$ is a basic random variable when $\sigma$ is distributed according to a Gibbs measure (see {{< knowl id="random-variable" section="probability" text="random variable" >}}).

## Physical interpretation
A spin configuration is the **microscopic state** of the lattice degrees of freedom at a fixed time (or in equilibrium sampling). In equilibrium statistical mechanics, configurations are weighted by Boltzmann factors built from the {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}}, producing a probability distribution (a Gibbs measure) over configurations (see {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}}).
