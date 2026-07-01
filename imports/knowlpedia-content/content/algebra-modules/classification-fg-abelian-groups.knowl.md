+++
id = "algebra-modules/classification-fg-abelian-groups"
title = "Classification of finitely generated abelian groups"
kind = "knowl"
summary = "Every finitely generated abelian group splits as a free part plus finite cyclic invariants."
aliases = ["classification-fg-abelian-groups", "Classification of finitely generated abelian groups"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/classification-fg-abelian-groups.md"
+++

**Classification of finitely generated abelian groups**: If $G$ is a finitely generated abelian group, then there exist integers $r\ge 0$ and $n_1,\dots,n_t\ge 2$ with $n_1\mid n_2\mid\cdots\mid n_t$ such that
\[
G \cong \mathbb Z^{\,r}\;\oplus\;\bigoplus_{i=1}^t \mathbb Z/n_i\mathbb Z.
\]
The integers $r$ and the invariant factors $n_i$ are uniquely determined by $G$.

This is obtained by applying the [[algebra-modules/structure-theorem-pid|structure theorem over a PID]] to the [[algebra-rings/pid|PID]] $\mathbb Z$: a finitely generated abelian group is a [[algebra-modules/finitely-generated-module|finitely generated module]] and decomposes as a [[algebra-modules/direct-sum-modules|direct sum]] of [[algebra-modules/cyclic-module|cyclic]] pieces.
