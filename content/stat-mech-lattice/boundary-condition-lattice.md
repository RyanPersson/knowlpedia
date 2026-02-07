---
title: "Boundary condition (lattice spin system)"
description: "A prescription of spins outside a finite region that determines how the boundary interacts with the interior in finite-volume Gibbs measures."
---

Let $\Lambda \Subset \mathbb{Z}^d$ be a finite region and let $\Omega=\mathcal S^{\mathbb{Z}^d}$ be the full {{< knowl id="configuration-space-lattice" text="configuration space" >}}. A **boundary condition** is an exterior configuration
$$
\eta \in \Omega,
$$

used to define energies of interior configurations $\sigma_\Lambda \in \mathcal S^\Lambda$ through a finite-volume Hamiltonian
$$
H_\Lambda(\sigma_\Lambda \mid \eta),
$$

which includes interactions between sites in $\Lambda$ and sites in $\Lambda^c$ as prescribed by $\eta$ (see {{< knowl id="lattice-hamiltonian" text="lattice Hamiltonian" >}}).

Equivalently, one forms a full configuration $\sigma_\Lambda \eta_{\Lambda^c}$ that equals $\sigma$ on $\Lambda$ and $\eta$ outside, and evaluates the interaction energy terms that touch $\Lambda$.

## Cross-links
- Boundary conditions enter directly in the definition of the {{< knowl id="finite-volume-gibbs-measure" text="finite-volume Gibbs measure" >}} and hence the {{< knowl id="partition-function-lattice" text="partition function" >}}.
- They are central in the construction of {{< knowl id="gibbs-specification" text="Gibbs specifications" >}} and the {{< knowl id="dlr-equation" text="DLR equation" >}}.
- Different boundary conditions can select different {{< knowl id="pure-phase" text="pure phases" >}} in the thermodynamic limit (see {{< knowl id="phase-transition-gibbs" text="phase transitions" >}}).

## Key properties
1. **Local influence for finite-range interactions.** If the interaction is {{< knowl id="finite-range-interaction-lattice" text="finite-range" >}} with range $R$, then $\eta$ affects $H_\Lambda(\cdot\mid\eta)$ only through spins in a boundary layer of thickness $R$ around $\partial\Lambda$.
2. **Common examples.**
   - **Free boundary:** ignore interaction terms crossing from $\Lambda$ to $\Lambda^c$ (can be encoded by a particular choice of Hamiltonian convention).
   - **Fixed (plus/minus) boundary:** set $\eta_x$ to a constant value outside $\Lambda$ (e.g. all $+1$ for Ising).
   - **Periodic boundary:** identify opposite faces of $\Lambda$ (often implemented by changing the graph structure rather than specifying $\eta$).
3. **Finite-size effects.** Thermodynamic quantities in finite volume can depend strongly on the boundary condition, especially near criticality where the {{< knowl id="correlation-length" section="stat-mech" text="correlation length" >}} is large.
4. **Phase selection.** When multiple infinite-volume Gibbs measures exist, sequences of finite-volume Gibbs measures with different boundary conditions may converge to different limiting measures (e.g. plus vs minus phases).

## Physical interpretation
A boundary condition models the environment surrounding the observed finite region: a surface that prefers certain spin orientations, an external reservoir, or a “pinning” mechanism used to select a particular macroscopic state. In systems with phase coexistence, boundaries can nucleate and stabilize one phase inside the box, revealing the multiplicity structure of infinite-volume equilibrium states.
