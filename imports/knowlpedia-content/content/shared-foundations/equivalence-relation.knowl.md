+++
id = "shared-foundations/equivalence-relation"
title = "Equivalence relation"
kind = "knowl"
summary = "A relation that formalizes when two elements should be regarded as the same type."
aliases = ["equivalence-relation", "Equivalence relation"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/equivalence-relation.md"
+++

An **equivalence relation** on a set $A$ is a [[shared-foundations/relation|relation]] $\sim\,\subseteq A\times A$ satisfying the following three properties for all $a,b,c\in A$:

- **Reflexive:** $a\sim a$.
- **Symmetric:** if $a\sim b$, then $b\sim a$.
- **Transitive:** if $a\sim b$ and $b\sim c$, then $a\sim c$.

Equivalence relations partition $A$ into [[shared-foundations/equivalence-class|equivalence classes]], and the set of all classes forms a [[shared-foundations/quotient-set|quotient set]].

**Examples:**
- On $\mathbb{Z}$, define $a\sim b$ iff $a-b$ is divisible by a fixed $n\in\mathbb{N}$ (congruence modulo $n$).
- On any set $A$, the equality relation $a\sim b \iff a=b$ is an equivalence relation.
