+++
id = "lie-groups/cartan-subalgebra-self-normalizing-lemma"
title = "Cartan subalgebras are self-normalizing"
kind = "knowl"
summary = "If h is a Cartan subalgebra, then its normalizer in g equals h."
aliases = ["cartan-subalgebra-self-normalizing-lemma", "Cartan subalgebras are self-normalizing"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/cartan-subalgebra-self-normalizing-lemma.md"
+++

Let $\mathfrak{g}$ be a finite-dimensional [[lie-groups/lie-algebra|Lie algebra]] over an algebraically closed field of characteristic $0$, and let $\mathfrak{h}\subset \mathfrak{g}$ be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]].

**Lemma.** The normalizer of $\mathfrak{h}$ in $\mathfrak{g}$ is $\mathfrak{h}$ itself:
$$
N_{\mathfrak{g}}(\mathfrak{h})=\{X\in\mathfrak{g}:[X,\mathfrak{h}]\subset \mathfrak{h}\}=\mathfrak{h}.
$$

Equivalently, if $X\in\mathfrak{g}$ satisfies $[X,H]\in \mathfrak{h}$ for every $H\in\mathfrak{h}$, then $X\in \mathfrak{h}$.

**Context.** This property ensures that $\mathfrak{h}$ is as large as possible among nilpotent subalgebras compatible with its own adjoint action: anything that stabilizes $\mathfrak{h}$ by commutators is already inside $\mathfrak{h}$. In semisimple Lie theory, self-normalizing is what makes the [[lie-groups/root-space-decomposition|root decomposition]] relative to $\mathfrak{h}$ behave rigidly, and it underlies the definition of the [[lie-groups/weyl-group|Weyl group]] as a quotient of a group normalizer by a centralizer.
