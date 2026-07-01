+++
id = "algebra-groups/correspondence-theorem-groups"
title = "Correspondence Theorem (Groups)"
kind = "knowl"
summary = "Subgroups of G containing N correspond to subgroups of the quotient G/N"
aliases = ["correspondence-theorem-groups", "Correspondence Theorem (Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/correspondence-theorem-groups.md"
+++

**Correspondence Theorem (Groups).**
Let $G$ be a [[algebra-groups/group|group]] and let $N \trianglelefteq G$ be a [[algebra-groups/normal-subgroup|normal subgroup]]. Let $\pi: G \to G/N$ be the canonical projection. Then the assignments
- $A \mapsto A/N := \{aN : a \in A\}$, for [[algebra-groups/subgroup|subgroups]] $A$ with $N \subseteq A \subseteq G$, and
- $B \mapsto \pi^{-1}(B)$ (the [[shared-foundations/preimage|preimage]]) for subgroups $B \le G/N$,

are inverse, inclusion-preserving bijections between:
1. subgroups $A$ of $G$ with $N \subseteq A$, and
2. subgroups of $G/N$.

Moreover:
- $A \trianglelefteq G$ if and only if $A/N \trianglelefteq G/N$, and
- if $[G:A]$ is finite, then $[G:A] = [G/N : A/N]$.

This theorem explains how the subgroup lattice of a [[algebra-groups/quotient-group|quotient group]] $G/N$ is "the same as" the lattice of subgroups of $G$ containing $N$. It is a standard tool for building and comparing chains of subgroups, especially in the study of normal series.
