---
title: "Finite cyclic group is isomorphic to ℤ/nℤ"
description: "A cyclic group of order n is (canonically) isomorphic to ℤ/nℤ"
---

**Proposition (Finite cyclic groups).**
Let $G$ be a {{</* knowl id="group" text="group" */>}}. Suppose $G$ is cyclic of finite order $n$, i.e. $G=\langle g\rangle$ and $|G|=n$. Then $G$ is {{</* knowl id="group-isomorphism" text="isomorphic" */>}} to the additive group $\mathbb Z/n\mathbb Z$. Concretely, the map
$$
\varphi:\mathbb Z/n\mathbb Z \longrightarrow G,\qquad \varphi(\overline{k})=g^k
$$
is a well-defined isomorphism.

**Context.**
This identifies finite cyclic groups up to unique isomorphism by their order. Many computations about cyclic groups can therefore be reduced to modular arithmetic in $\mathbb Z/n\mathbb Z$.

**Proof sketch.**
Well-definedness uses $g^{k+n}=g^k$ since $g^n=e$. The map is a homomorphism because $\varphi(\overline{k+\ell})=g^{k+\ell}=g^kg^\ell$. It is surjective because $G=\langle g\rangle$, and injective because the kernel is exactly $\overline{0}$ when $g$ has order $n$.
