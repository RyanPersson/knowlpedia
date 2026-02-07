---
title: "Derived series of a Lie algebra"
description: "The descending chain , used to define solvability."
---

Let $\mathfrak g$ be a {{< knowl id="lie-algebra" text="Lie algebra" >}}.

## Definition (derived series)
The **derived series** of $\mathfrak g$ is the descending sequence of Lie subalgebras
\[
\mathfrak g^{(0)} := \mathfrak g,\qquad
\mathfrak g^{(k+1)} := [\mathfrak g^{(k)},\,\mathfrak g^{(k)}]
\]
where the bracket denotes the {{< knowl id="derived-subalgebra" text="derived subalgebra" >}} of $\mathfrak g^{(k)}$.

Each $\mathfrak g^{(k)}$ is an {{< knowl id="ideal-lie-algebra" text="ideal" >}} in $\mathfrak g$ (because $[\mathfrak g,\mathfrak g^{(k+1)}]\subseteq \mathfrak g^{(k+1)}$), so the series is well behaved under quotients.

## Solvability
A Lie algebra is **solvable** if $\mathfrak g^{(r)}=0$ for some $r\ge 0$; see {{< knowl id="solvable-lie-algebra" text="solvable Lie algebra" >}} and the equivalences summarized in {{< knowl id="tfae-solvability-lie-algebra" text="TFAE: solvability" >}}. The smallest such $r$ is the **derived length**.

## Relation to groups
For a connected Lie group $G$ with Lie algebra $\mathfrak g$, the derived series is the infinitesimal analog of the derived series of the {{< knowl id="commutator-subgroup-of-a-lie-group" text="commutator subgroup" >}}. Informally: iterated commutators in the group differentiate to iterated commutators in the Lie algebra.
