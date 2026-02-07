---
title: "Spontaneous symmetry breaking"
description: "Failure of the equilibrium (Gibbs) state at zero field to inherit a global symmetry of the Hamiltonian, manifested by multiple symmetry-related pure phases."
---

Let a lattice model have a global symmetry group $G$ acting on spins (e.g. spin flip $\sigma\mapsto -\sigma$ for the {{< knowl id="ising-model" text="Ising model" >}} at zero field). This induces an action on {{< knowl id="spin-configuration" text="spin configurations" >}} and hence on {{< knowl id="infinite-volume-gibbs-measure" text="infinite-volume Gibbs measures" >}} by pushforward.

We say the model exhibits **spontaneous symmetry breaking (SSB)** at parameters (e.g. inverse temperature $\beta$) if:
1. the interaction (or {{< knowl id="lattice-hamiltonian" text="Hamiltonian" >}}) is $G$-invariant (typically at $h=0$), but
2. there exists at least one infinite-volume Gibbs measure $\mu$ that is *not* $G$-invariant, i.e. $g\mu\neq \mu$ for some $g\in G$.

Equivalently (and commonly), SSB is present when there are multiple {{< knowl id="extremal-gibbs-measure" text="extremal" >}} ({{< knowl id="pure-phase" text="pure-phase" >}}) Gibbs measures related by symmetry, and the symmetric state is a nontrivial {{< knowl id="mixture-gibbs-measures" text="mixture" >}} of them.

## Key properties
- **Multiplicity of phases:** SSB implies non-uniqueness of solutions to the {{< knowl id="dlr-equation" text="DLR equation" >}} (or, equivalently, non-uniqueness of the {{< knowl id="gibbs-specification" text="Gibbs specification" >}}-consistent measures).
- **Order parameters:** SSB is detected by a nonzero {{< knowl id="order-parameter" text="order parameter" >}} that transforms nontrivially under $G$ (e.g. magnetization for $\mathbb{Z}_2$ symmetry).
- **Selection by symmetry-breaking fields:** Introducing a small symmetry-breaking {{< knowl id="external-field-coupling" text="external field" >}} and taking $h\downarrow 0$ often selects an extremal phase, leading to quantities such as {{< knowl id="spontaneous-magnetization" text="spontaneous magnetization" >}}.
- **Not every phase transition breaks symmetry:** Non-analyticity in thermodynamic functions (a {{< knowl id="phase-transition-gibbs" text="phase transition" >}}) may occur with or without breaking a given symmetry; conversely, SSB typically entails a phase transition for models with short-range interactions, but the precise relationship can be model-dependent.

## Physical interpretation
The Hamiltonian may be perfectly symmetric, yet the macroscopic system “chooses” one of several symmetry-related ordered states in the thermodynamic limit. Each ordered state is stable and reproducible (a pure phase), but the choice is not dictated by the symmetric microscopic rules—hence the symmetry is broken *spontaneously* by the state, not explicitly by the dynamics or Hamiltonian.
