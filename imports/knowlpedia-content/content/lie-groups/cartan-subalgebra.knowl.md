+++
id = "lie-groups/cartan-subalgebra"
title = "Cartan subalgebra"
kind = "knowl"
summary = "A maximal nilpotent, self-normalizing subalgebra; in the semisimple case, a maximal toral subalgebra."
aliases = ["cartan-subalgebra", "Cartan subalgebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/cartan-subalgebra.md"
+++

Let $\mathfrak{g}$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over an algebraically closed field of characteristic $0$ (typically $\mathbb{C}$).

**Definition.** A subalgebra $\mathfrak{h}\subset \mathfrak{g}$ is a **Cartan subalgebra** if:
1. $\mathfrak{h}$ is [[lie-groups/nilpotent-lie-algebra|nilpotent]] as a Lie algebra, and
2. $\mathfrak{h}$ is self-normalizing in $\mathfrak{g}$, i.e. $N_{\mathfrak{g}}(\mathfrak{h})=\mathfrak{h}$ (compare [[lie-groups/cartan-subalgebra-self-normalizing-lemma|the self-normalizing lemma]]).

Here $N_{\mathfrak{g}}(\mathfrak{h})=\{X\in\mathfrak{g}:[X,\mathfrak{h}]\subset \mathfrak{h}\}$ is the normalizer Lie subalgebra.

**Semisimple refinement.** If $\mathfrak{g}$ is [[lie-groups/semisimple-lie-algebra|semisimple]], Cartan subalgebras can be characterized as maximal abelian subalgebras consisting of semisimple endomorphisms in the adjoint representation. With such an $\mathfrak{h}$, $\mathfrak{g}$ admits the [[lie-groups/root-space-decomposition|root space decomposition]]
$$
\mathfrak{g}=\mathfrak{h}\oplus \bigoplus_{\alpha\in \Phi}\mathfrak{g}_\alpha,
$$

where $\Phi\subset \mathfrak{h}^*$ is the [[lie-groups/root-lie-algebra|root set]] and $\mathfrak{g}_\alpha$ are the [[lie-groups/root-space|root spaces]].

**Motivation.** Cartan subalgebras are the “coordinate axes” for semisimple structure: weights of representations live in $\mathfrak{h}^*$ (see [[lie-groups/weights-in-dual-cartan|weights in the dual Cartan]]), and the choice of $\mathfrak{h}$ underlies Dynkin-diagram data such as the [[lie-groups/cartan-matrix|Cartan matrix]].
