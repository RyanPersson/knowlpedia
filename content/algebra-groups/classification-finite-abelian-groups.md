---
title: "Classification of Finite Abelian Groups"
description: "Every finite abelian group is a direct product of cyclic prime-power groups, uniquely up to isomorphism."
---

**Classification of Finite Abelian Groups**: Let $G$ be a finite {{< knowl id="abelian-group" text="abelian group" >}}. Then $G$ is isomorphic to a finite {{< knowl id="direct-product-groups" text="direct product" >}} of {{< knowl id="cyclic-subgroup" text="cyclic groups" >}} of prime-power order:
$$G \cong \prod_{i=1}^t \prod_{j=1}^{r_i} C_{p_i^{e_{ij}}},$$
where $p_1,\dots,p_t$ are primes, each $e_{ij}\ge 1$, and $C_{p^e}$ denotes a cyclic group of order $p^e$ (a finite {{< knowl id="p-group" text="p-group" >}}).

Equivalently (the **invariant factor form**), there exist integers $1<n_1\mid n_2\mid \cdots \mid n_r$ such that
$$G \cong C_{n_1}\times C_{n_2}\times \cdots \times C_{n_r}.$$
In either form, the invariants (prime powers in the first form, or the chain $n_1\mid\cdots\mid n_r$ in the second form) are uniquely determined by $G$ up to reordering of isomorphic factors.

This is the finite-group specialization of the {{< knowl id="fundamental-theorem-fg-abelian-groups" text="fundamental theorem of finitely generated abelian groups" >}} (since every finite group is finitely generated).

**Examples:**
- Order $8=2^3$: the abelian groups of order $8$ are, up to isomorphism,
  - $C_8$,
  - $C_4\times C_2$,
  - $C_2\times C_2\times C_2$.
- Order $12=2^2\cdot 3$: the abelian groups of order $12$ are, up to isomorphism,
  - $C_{12}\cong C_4\times C_3$,
  - $C_2\times C_2\times C_3 \cong C_2\times C_6$.
