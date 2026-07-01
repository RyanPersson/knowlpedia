+++
id = "lie-groups/derived-series-lie-algebra"
title = "Derived series of a Lie algebra"
kind = "knowl"
summary = "The descending chain , used to define solvability."
aliases = ["derived-series-lie-algebra", "Derived series of a Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/derived-series-lie-algebra.md"
+++

Let $\mathfrak g$ be a [[lie-groups/lie-algebra|Lie algebra]].

## Definition (derived series)
The **derived series** of $\mathfrak g$ is the descending sequence of Lie subalgebras
\[
\mathfrak g^{(0)} := \mathfrak g,\qquad
\mathfrak g^{(k+1)} := [\mathfrak g^{(k)},\,\mathfrak g^{(k)}]
\]
where the bracket denotes the [[lie-groups/derived-subalgebra|derived subalgebra]] of $\mathfrak g^{(k)}$.

Each $\mathfrak g^{(k)}$ is an [[lie-groups/ideal-lie-algebra|ideal]] in $\mathfrak g$ (because $[\mathfrak g,\mathfrak g^{(k+1)}]\subseteq \mathfrak g^{(k+1)}$), so the series is well behaved under quotients.

## Solvability
A Lie algebra is **solvable** if $\mathfrak g^{(r)}=0$ for some $r\ge 0$; see [[lie-groups/solvable-lie-algebra|solvable Lie algebra]] and the equivalences summarized in [[lie-groups/tfae-solvability-lie-algebra|TFAE: solvability]]. The smallest such $r$ is the **derived length**.

## Relation to groups
For a connected Lie group $G$ with Lie algebra $\mathfrak g$, the derived series is the infinitesimal analog of the derived series of the [[lie-groups/commutator-subgroup-of-a-lie-group|commutator subgroup]]. Informally: iterated commutators in the group differentiate to iterated commutators in the Lie algebra.
