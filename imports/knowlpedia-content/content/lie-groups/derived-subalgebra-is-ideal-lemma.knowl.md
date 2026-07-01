+++
id = "lie-groups/derived-subalgebra-is-ideal-lemma"
title = "Derived subalgebra is an ideal"
kind = "knowl"
summary = "For any Lie algebra , the commutator subalgebra is an ideal of ."
aliases = ["derived-subalgebra-is-ideal-lemma", "Derived subalgebra is an ideal"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/derived-subalgebra-is-ideal-lemma.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]].

## Lemma
The [[lie-groups/derived-subalgebra|derived subalgebra]] $[\mathfrak g,\mathfrak g]$ is an [[lie-groups/ideal-lie-algebra|ideal]] in $\mathfrak g$; equivalently,
\[
[\mathfrak g,\,[\mathfrak g,\mathfrak g]] \subseteq [\mathfrak g,\mathfrak g].
\]

## Proof
Take $x\in\mathfrak g$ and an element of $[\mathfrak g,\mathfrak g]$ of the form $[y,z]$. Using the Jacobi identity for the [[fiber-bundles/lie-bracket|Lie bracket]],
\[
[x,[y,z]] = [[x,y],z] + [y,[x,z]].
\]
Each term on the right is a commutator of two elements of $\mathfrak g$, hence lies in $[\mathfrak g,\mathfrak g]$. By linearity, $[x,w]\in[\mathfrak g,\mathfrak g]$ for all $w\in[\mathfrak g,\mathfrak g]$, proving the claim.

**Context.** This lemma ensures that iterating $[\cdot,\cdot]$ produces characteristic ideals (e.g. the [[lie-groups/derived-series-lie-algebra|derived series]]), making solvability a robust isomorphism-invariant notion.
