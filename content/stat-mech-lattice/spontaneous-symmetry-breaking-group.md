---
title: "Spontaneous symmetry breaking and symmetry groups"
description: "A symmetry of the Hamiltonian (given by a group action) can fail to be a symmetry of an infinite-volume equilibrium state, producing multiple pure phases and nonzero order parameters."
---

## Symmetry group of a model

Let a group $G$ act on configurations $\sigma$ (spins, particle configurations, fields). A Hamiltonian $H$ is **$G$-invariant** if
$$
H(g\cdot \sigma)=H(\sigma)\quad\text{for all }g\in G.
$$
Examples:
- Ising model: $G=\mathbb{Z}_2$ acts by global spin flip $\sigma_i\mapsto -\sigma_i$.
- $O(n)$ models: $G=O(n)$ acts by rotating vector spins.

This invariance induces a corresponding symmetry of finite-volume Gibbs measures when boundary conditions and external fields are also symmetric; see {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measures" >}}.

## Definition: spontaneous symmetry breaking (SSB)

**Spontaneous symmetry breaking** occurs when:
1. the Hamiltonian is $G$-invariant (and there is no explicit symmetry-breaking field), but
2. there exists an **infinite-volume equilibrium state** (Gibbs measure) that is *not* invariant under $G$.

Formally, let $\mu$ be an infinite-volume Gibbs measure (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}} and {{< knowl id="dlr-equation" section="stat-mech-lattice" text="DLR equation" >}}). Then SSB means there exists $g\in G$ such that
$$
\mu\circ g^{-1}\neq \mu.
$$

## Order parameters and symmetry breaking

SSB is detected by a **symmetry-breaking order parameter** (see {{< knowl id="order-parameter" section="stat-mech-lattice" text="order parameter" >}}), i.e., an observable $O(\sigma)$ whose expectation changes under $G$:
- In an Ising ferromagnet, a canonical choice is the magnetization density, leading to {{< knowl id="spontaneous-magnetization" section="stat-mech-lattice" text="spontaneous magnetization" >}} in the ordered phase.

A symmetric Gibbs state can often be expressed as a mixture of symmetry-broken extremal states (pure phases). This is one way to connect SSB to the structure of phase coexistence; see {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions via Gibbs measures" >}}.

## Example: Ising $\mathbb{Z}_2$ symmetry below critical temperature

For the ferromagnetic Ising model at zero field ($h=0$), the Hamiltonian is invariant under global spin flip. In dimensions $d\ge 2$ and at low temperature, there are distinct infinite-volume Gibbs states selected by boundary conditions:
- a “plus” phase with positive magnetization,
- a “minus” phase with negative magnetization.

These two states are exchanged by the $\mathbb{Z}_2$ action, so each breaks the symmetry even though the model is symmetric.

## Continuous symmetries and the role of dimension

For continuous symmetry groups (e.g., $O(n)$), long-range order can be obstructed in low dimensions by fluctuations:
- In many short-range lattice systems with continuous symmetry, SSB is ruled out in $d\le 2$ under suitable hypotheses; see {{< knowl id="mermin-wagner-theorem" section="stat-mech" text="Mermin–Wagner theorem" >}} and {{< knowl id="continuous-symmetry-on-spins" section="stat-mech" text="continuous symmetries on spins" >}}.

## Connection to Landau theory

Landau theory encodes SSB via the symmetry of the Landau free energy:
- If symmetry forces $f(m)$ to be even in $m$ at zero field, symmetry breaking occurs when the global minimizers become nonzero and come in group-related families; see {{< knowl id="landau-free-energy-functional" section="stat-mech" text="Landau free-energy functional" >}}.
