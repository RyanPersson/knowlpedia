+++
id = "lie-groups/root-space-decomposition"
title = "Root space decomposition"
kind = "knowl"
summary = "Decomposition of a semisimple Lie algebra into a Cartan subalgebra plus root spaces for the adjoint action."
aliases = ["root-space-decomposition", "Root space decomposition"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/root-space-decomposition.md"
+++

Let $\mathfrak g$ be a finite-dimensional complex semisimple Lie algebra (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]) and let $\mathfrak h\subset\mathfrak g$ be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]]. For each $\alpha\in\mathfrak h^*$ define the weight space
\[
\mathfrak g_\alpha=\{X\in\mathfrak g:[H,X]=\alpha(H)X\ \text{for all }H\in\mathfrak h\},
\]
and let $\Phi\subset\mathfrak h^*$ be the set of nonzero $\alpha$ with $\mathfrak g_\alpha\neq 0$ (the [[lie-groups/root-lie-algebra|roots]]).

The **root space decomposition** (sometimes called the Cartan decomposition of $\mathfrak g$) is the direct sum decomposition
\[
\mathfrak g \;=\; \mathfrak h \;\oplus\; \bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
Conceptually, it is the simultaneous eigenspace decomposition for the commuting family of endomorphisms $\{\mathrm{ad}(H)\}_{H\in\mathfrak h}$ coming from the [[lie-groups/adjoint-representation-of-a-lie-algebra|adjoint representation]].

Two structural bracket relations are fundamental:

- $[\mathfrak h,\mathfrak g_\alpha]\subseteq \mathfrak g_\alpha$ with the eigenvalue rule $[H,X]=\alpha(H)X$;
- $[\mathfrak g_\alpha,\mathfrak g_\beta]\subseteq \mathfrak g_{\alpha+\beta}$ (with the convention $\mathfrak g_{\gamma}=0$ if $\gamma$ is not a weight), as explained in [[lie-groups/root-space|root spaces]].

With the inner product induced by the [[lie-groups/killing-form|Killing form]], the set $\Phi$ satisfies the axioms of a [[lie-groups/root-system|root system]]. Choosing a [[lie-groups/positive-root|positive system]] refines this into a triangular decomposition and is the starting point for Dynkin diagram combinatorics (see [[lie-groups/dynkin-diagram|Dynkin diagrams]]).
