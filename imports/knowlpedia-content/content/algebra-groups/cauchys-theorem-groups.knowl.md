+++
id = "algebra-groups/cauchys-theorem-groups"
title = "Cauchy's Theorem (Finite Groups)"
kind = "knowl"
summary = "If a prime p divides |G|, then G contains an element (and subgroup) of order p"
aliases = ["cauchys-theorem-groups", "Cauchy's Theorem (Finite Groups)"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/cauchys-theorem-groups.md"
+++

**Cauchy's Theorem (Finite Groups).**
Let $G$ be a finite [[algebra-groups/group|group]], and let $p$ be a prime number such that $p \mid |G|$. Then there exists an element $g \in G$ with $g \ne e$ and $g^p = e$; equivalently, $G$ has a [[algebra-groups/cyclic-subgroup|cyclic subgroup]] of order $p$.

Cauchy's theorem is a partial converse to [[algebra-groups/lagranges-theorem|Lagrange's theorem]]: instead of saying "subgroup orders divide $|G|$," it guarantees the existence of elements of certain prime orders when that prime divides $|G|$. It is a key input for [[algebra-groups/sylows-first-theorem|Sylow's first theorem]].
