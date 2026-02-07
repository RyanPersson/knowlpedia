---
title: "Classification of finitely generated abelian groups"
description: "Every finitely generated abelian group splits as a free part plus finite cyclic invariants."
---

**Classification of finitely generated abelian groups**: If $G$ is a finitely generated abelian group, then there exist integers $r\ge 0$ and $n_1,\dots,n_t\ge 2$ with $n_1\mid n_2\mid\cdots\mid n_t$ such that
\[
G \cong \mathbb Z^{\,r}\;\oplus\;\bigoplus_{i=1}^t \mathbb Z/n_i\mathbb Z.
\]
The integers $r$ and the invariant factors $n_i$ are uniquely determined by $G$.

This is obtained by applying the {{< knowl id="structure-theorem-pid" text="structure theorem over a PID" >}} to the {{< knowl id="pid" section="algebra-rings" text="PID" >}} $\mathbb Z$: a finitely generated abelian group is a {{< knowl id="finitely-generated-module" text="finitely generated module" >}} and decomposes as a {{< knowl id="direct-sum-modules" text="direct sum" >}} of {{< knowl id="cyclic-module" text="cyclic" >}} pieces.
