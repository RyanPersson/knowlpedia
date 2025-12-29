---
title: "Fundamental Theorem of Finitely Generated Abelian Groups"
description: "Every finitely generated abelian group is a direct sum of copies of Z and finite cyclic groups"
---

**Fundamental Theorem of Finitely Generated Abelian Groups.**
Let $G$ be a finitely generated {{< knowl id="abelian-group" text="abelian group" >}} (i.e. $G$ has a finite {{< knowl id="generating-set" text="generating set" >}}). Then there exist integers $r\ge 0$ and $n_1,\dots,n_k \ge 2$ with $n_1 \mid n_2 \mid \cdots \mid n_k$ such that
$$
G \cong \mathbb{Z}^r \oplus \mathbb{Z}/n_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/n_k\mathbb{Z},
$$
where $\oplus$ denotes the {{< knowl id="direct-sum-groups" text="direct sum" >}} of groups. The integer $r$ (the free rank) and the invariant factors $n_1,\dots,n_k$ are uniquely determined by $G$.

Equivalently, $G$ decomposes as a direct sum of {{< knowl id="cyclic-subgroup" text="cyclic" >}} groups of prime-power order (the "elementary divisor" form). This theorem is the group-theoretic specialization of {{< knowl id="structure-theorem-pid" text="the structure theorem for finitely generated modules over a PID" >}} with the PID $\mathbb{Z}$.

**Proof sketch.**
One reduces to a presentation of $G$ as $\mathbb{Z}^n/R$ for a subgroup $R \le \mathbb{Z}^n$ and then diagonalizes the relations using integer row/column operations (Smith normal form). The diagonal entries give the invariant factors, and the number of zero diagonal entries gives the rank $r$.
