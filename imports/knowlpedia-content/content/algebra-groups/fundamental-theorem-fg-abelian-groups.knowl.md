+++
id = "algebra-groups/fundamental-theorem-fg-abelian-groups"
title = "Fundamental Theorem of Finitely Generated Abelian Groups"
kind = "knowl"
summary = "Every finitely generated abelian group is a direct sum of copies of Z and finite cyclic groups"
aliases = ["fundamental-theorem-fg-abelian-groups", "Fundamental Theorem of Finitely Generated Abelian Groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/fundamental-theorem-fg-abelian-groups.md"
+++

**Fundamental Theorem of Finitely Generated Abelian Groups.**
Let $G$ be a finitely generated [[algebra-groups/abelian-group|abelian group]] (i.e. $G$ has a finite [[algebra-groups/generating-set|generating set]]). Then there exist integers $r\ge 0$ and $n_1,\dots,n_k \ge 2$ with $n_1 \mid n_2 \mid \cdots \mid n_k$ such that
$$
G \cong \mathbb{Z}^r \oplus \mathbb{Z}/n_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/n_k\mathbb{Z},
$$

where $\oplus$ denotes the [[algebra-groups/direct-sum-groups|direct sum]] of groups. The integer $r$ (the free rank) and the invariant factors $n_1,\dots,n_k$ are uniquely determined by $G$.

Equivalently, $G$ decomposes as a direct sum of [[algebra-groups/cyclic-subgroup|cyclic]] groups of prime-power order (the "elementary divisor" form). This theorem is the group-theoretic specialization of [[algebra-modules/structure-theorem-pid|the structure theorem for finitely generated modules over a PID]] with the PID $\mathbb{Z}$.
