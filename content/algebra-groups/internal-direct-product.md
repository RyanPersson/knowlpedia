---
title: "Internal Direct Product"
description: "A group built from two normal subgroups whose product is the whole group"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $N,H\le G$ be {{< knowl id="subgroup" text="subgroups" >}}. One says that **$G$ is the internal direct product of $N$ and $H$** if:
1. $N$ and $H$ are {{< knowl id="normal-subgroup" text="normal" >}},
2. $N\cap H$ is the {{< knowl id="trivial-subgroup" text="trivial subgroup" >}} $\{e\}$,
3. $NH = G$ (i.e. every $g\in G$ can be written as $g=nh$ with $n\in N$ and $h\in H$).

Under these hypotheses, the multiplication map $N\times H\to G$, $(n,h)\mapsto nh$, is a {{< knowl id="group-isomorphism" text="group isomorphism" >}}, so $G\cong N\times H$ as a {{< knowl id="direct-product-groups" text="direct product" >}}.

**Examples:**
- In any direct product $N\times H$, the subgroups $N\times\{e\}$ and $\{e\}\times H$ are normal, intersect trivially, and generate the whole group; thus $N\times H$ is an internal direct product in itself.
- In the cyclic group $C_6=\langle a\rangle$, the subgroups $\langle a^3\rangle$ (order $2$) and $\langle a^2\rangle$ (order $3$) satisfy the conditions, so $C_6\cong C_2\times C_3$.
- Non-example: in $S_3$, the subgroup $A_3$ is normal but a subgroup of order $2$ is not normal, so $S_3$ is not an internal direct product of those two subgroups (it is an {{< knowl id="internal-semidirect-product" text="internal semidirect product" >}} instead).
