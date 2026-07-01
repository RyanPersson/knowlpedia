+++
id = "lie-groups/derived-subalgebra"
title = "Derived subalgebra"
kind = "knowl"
summary = "The Lie subalgebra spanned by commutators; it measures how far is from abelian."
aliases = ["derived-subalgebra", "Derived subalgebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/derived-subalgebra.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]].

The **derived subalgebra** (or commutator subalgebra) of $\mathfrak g$ is
\[
[\mathfrak g,\mathfrak g] := \mathrm{span}\{[x,y] : x,y\in \mathfrak g\}\subseteq \mathfrak g.
\]
It is a Lie subalgebra, and in fact an [[lie-groups/ideal-lie-algebra|ideal]]; the ideal property is recorded explicitly in [[lie-groups/derived-subalgebra-is-ideal-lemma|the lemma that $[\mathfrak g,\mathfrak g]$ is an ideal]].

## Basic consequences
- $\mathfrak g$ is [[lie-groups/abelian-lie-algebra|abelian]] iff $[\mathfrak g,\mathfrak g]=0$.
- The quotient $\mathfrak g/[\mathfrak g,\mathfrak g]$ is the **abelianization** of $\mathfrak g$ (a special case of [[lie-groups/quotient-lie-algebra|quotient Lie algebra]]).
- $\mathfrak g$ is called **perfect** if $[\mathfrak g,\mathfrak g]=\mathfrak g$; for example, any [[lie-groups/simple-lie-algebra|simple Lie algebra]] is perfect.

## Context
The derived subalgebra is the first step in the [[lie-groups/derived-series-lie-algebra|derived series]], which detects solvability and organizes many structure theorems such as the [[lie-groups/levi-decomposition-theorem|Levi decomposition]].
