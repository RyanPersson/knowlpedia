+++
id = "stat-mech-lattice/spontaneous-symmetry-breaking"
title = "Spontaneous symmetry breaking"
kind = "knowl"
summary = "Failure of the equilibrium (Gibbs) state at zero field to inherit a global symmetry of the Hamiltonian, manifested by multiple symmetry-related pure phases."
aliases = ["spontaneous-symmetry-breaking", "Spontaneous symmetry breaking"]
domains = ["stat-mech-lattice"]
legacy_source_path = "stat-mech-lattice/spontaneous-symmetry-breaking.md"
+++

Let a lattice model have a global symmetry group $G$ acting on spins (e.g. spin flip $\sigma\mapsto -\sigma$ for the [[stat-mech-lattice/ising-model|Ising model]] at zero field). This induces an action on [[stat-mech-lattice/spin-configuration|spin configurations]] and hence on [[stat-mech-lattice/infinite-volume-gibbs-measure|infinite-volume Gibbs measures]] by pushforward.

We say the model exhibits **spontaneous symmetry breaking (SSB)** at parameters (e.g. inverse temperature $\beta$) if:
1. the interaction (or [[stat-mech-lattice/lattice-hamiltonian|Hamiltonian]]) is $G$-invariant (typically at $h=0$), but
2. there exists at least one infinite-volume Gibbs measure $\mu$ that is *not* $G$-invariant, i.e. $g\mu\neq \mu$ for some $g\in G$.

Equivalently (and commonly), SSB is present when there are multiple [[stat-mech-lattice/extremal-gibbs-measure|extremal]] ([[stat-mech-lattice/pure-phase|pure-phase]]) Gibbs measures related by symmetry, and the symmetric state is a nontrivial [[stat-mech-lattice/mixture-gibbs-measures|mixture]] of them.

## Key properties
- **Multiplicity of phases:** SSB implies non-uniqueness of solutions to the [[stat-mech-lattice/dlr-equation|DLR equation]] (or, equivalently, non-uniqueness of the [[stat-mech-lattice/gibbs-specification|Gibbs specification]]-consistent measures).
- **Order parameters:** SSB is detected by a nonzero [[stat-mech-lattice/order-parameter|order parameter]] that transforms nontrivially under $G$ (e.g. magnetization for $\mathbb{Z}_2$ symmetry).
- **Selection by symmetry-breaking fields:** Introducing a small symmetry-breaking [[stat-mech-lattice/external-field-coupling|external field]] and taking $h\downarrow 0$ often selects an extremal phase, leading to quantities such as [[stat-mech-lattice/spontaneous-magnetization|spontaneous magnetization]].
- **Not every phase transition breaks symmetry:** Non-analyticity in thermodynamic functions (a [[stat-mech-lattice/phase-transition-gibbs|phase transition]]) may occur with or without breaking a given symmetry; conversely, SSB typically entails a phase transition for models with short-range interactions, but the precise relationship can be model-dependent.

## Physical interpretation
The Hamiltonian may be perfectly symmetric, yet the macroscopic system “chooses” one of several symmetry-related ordered states in the thermodynamic limit. Each ordered state is stable and reproducible (a pure phase), but the choice is not dictated by the symmetric microscopic rules—hence the symmetry is broken *spontaneously* by the state, not explicitly by the dynamics or Hamiltonian.
