+++
id = "lie-groups/lie-algebra-compact-is-reductive"
title = "Compact Lie algebra is reductive"
kind = "knowl"
summary = "The Lie algebra of a compact Lie group splits as center ⊕ semisimple part."
aliases = ["lie-algebra-compact-is-reductive", "Compact Lie algebra is reductive"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/lie-algebra-compact-is-reductive.md"
+++

Let $G$ be a compact [[fiber-bundles/lie-group|Lie group]] with Lie algebra $\mathfrak g$.

**Theorem (Compact implies reductive).**
The Lie algebra $\mathfrak g$ is **reductive**: it decomposes as a direct sum of ideals
\[
\mathfrak g \cong Z(\mathfrak g)\oplus [\mathfrak g,\mathfrak g],
\]
where $Z(\mathfrak g)$ is the [[lie-groups/center-of-a-lie-algebra|center]] (an abelian ideal, compare [[lie-groups/abelian-lie-algebra|abelian Lie algebras]]) and $[\mathfrak g,\mathfrak g]$ is semisimple (see [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]]). In particular, $[\mathfrak g,\mathfrak g]$ has nondegenerate Killing form, while the Killing form of $\mathfrak g$ is negative semidefinite with kernel $Z(\mathfrak g)$ (compare [[lie-groups/killing-form|Killing form]] and [[lie-groups/killing-form-nondegenerate-iff-semisimple|nondegeneracy vs semisimplicity]]).

**Idea of proof.**
Compactness gives an $\mathrm{Ad}(G)$-invariant inner product on $\mathfrak g$ by averaging any inner product over $G$; equivalently, compact $G$ admits a [[lie-groups/compact-lie-group-bi-invariant-metric|bi-invariant metric]]. With such an inner product, $\mathrm{ad}_x$ is skew-adjoint for all $x$, forcing strong structural constraints that split off the center and make the derived ideal semisimple.

**Context.**
Reductivity is the Lie-algebra reflection of robust representation theory for compact groups: finite-dimensional representations are completely reducible (compare [[lie-groups/weyls-theorem-complete-reducibility|complete reducibility]] and [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]]).
