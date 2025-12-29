---
title: "Cauchy's Theorem (Finite Groups)"
description: "If a prime p divides |G|, then G contains an element (and subgroup) of order p"
---

**Cauchy's Theorem (Finite Groups).**
Let $G$ be a finite {{< knowl id="group" text="group" >}}, and let $p$ be a prime number such that $p \mid |G|$. Then there exists an element $g \in G$ with $g \ne e$ and $g^p = e$; equivalently, $G$ has a {{< knowl id="cyclic-subgroup" text="cyclic subgroup" >}} of order $p$.

Cauchy's theorem is a partial converse to {{< knowl id="lagranges-theorem" text="Lagrange's theorem" >}}: instead of saying "subgroup orders divide $|G|$," it guarantees the existence of elements of certain prime orders when that prime divides $|G|$. It is a key input for {{< knowl id="sylows-first-theorem" text="Sylow's first theorem" >}}.

**Proof sketch.**
Let $X=\{(g_1,\dots,g_p)\in G^p : g_1g_2\cdots g_p=e\}$, so $|X|=|G|^{p-1}$, hence $p \mid |X|$. Let a cyclic group of order $p$ act on $X$ by cyclically permuting coordinates; every orbit has size $1$ or $p$. Therefore the number of fixed points is divisible by $p$; fixed points are exactly tuples $(g,\dots,g)$ with $g^p=e$, giving a nontrivial solution and hence an element of order $p$.
