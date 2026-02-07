---
title: "Correspondence Theorem (Groups)"
description: "Subgroups of G containing N correspond to subgroups of the quotient G/N"
---

**Correspondence Theorem (Groups).**
Let $G$ be a {{< knowl id="group" text="group" >}} and let $N \trianglelefteq G$ be a {{< knowl id="normal-subgroup" text="normal subgroup" >}}. Let $\pi: G \to G/N$ be the canonical projection. Then the assignments
- $A \mapsto A/N := \{aN : a \in A\}$, for {{< knowl id="subgroup" text="subgroups" >}} $A$ with $N \subseteq A \subseteq G$, and
- $B \mapsto \pi^{-1}(B)$ (the {{< knowl id="preimage" section="shared-foundations" text="preimage" >}}) for subgroups $B \le G/N$,

are inverse, inclusion-preserving bijections between:
1. subgroups $A$ of $G$ with $N \subseteq A$, and
2. subgroups of $G/N$.

Moreover:
- $A \trianglelefteq G$ if and only if $A/N \trianglelefteq G/N$, and
- if $[G:A]$ is finite, then $[G:A] = [G/N : A/N]$.

This theorem explains how the subgroup lattice of a {{< knowl id="quotient-group" text="quotient group" >}} $G/N$ is "the same as" the lattice of subgroups of $G$ containing $N$. It is a standard tool for building and comparing chains of subgroups, especially in the study of normal series.
