---
title: "Subring"
description: "A subset of a ring that is itself a ring under the inherited operations."
---

A **subring** of a {{< knowl id="ring" text="ring" >}} $R$ is a nonempty {{< knowl id="subset" text="subset" >}} $S\subseteq R$ such that, with the operations induced from $R$, the triple $(S,+,\cdot)$ is a ring. Equivalently, $S$ is closed under addition, additive inverses, and multiplication (and hence contains $0$).

If $R$ is {{< knowl id="unital-ring" text="unital" >}}, one sometimes distinguishes *unital subrings* by additionally requiring $1_R\in S$; unless stated, “subring” need not contain the identity. Subrings often appear as images of homomorphisms and as ambient structures for ideal theory.

**Examples:**
- $\mathbb Z$ is a subring of $\mathbb Q$.
- The diagonal matrices form a subring of $M_n(\mathbb Z)$.
- $2\mathbb Z$ is a subring of $\mathbb Z$, but it is not a unital subring.