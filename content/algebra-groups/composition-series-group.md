---
title: "Composition series"
description: "A subnormal series with simple successive quotients"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. A **composition series** for $G$ is a finite chain of subgroups
$
\{e\}=G_0\lhd G_1\lhd \cdots \lhd G_n=G
$
such that:
1. each $G_{i-1}$ is normal in $G_i$ (so this is a {{< knowl id="subnormal-series" text="subnormal series" >}}), and
2. each factor {{< knowl id="quotient-group" text="quotient group" >}} $G_i/G_{i-1}$ is a {{< knowl id="simple-group" text="simple group" >}}.

The groups $G_i/G_{i-1}$ are called the **composition factors** of the series. A major structural result, the {{< knowl id="jordan-holder-theorem-groups" text="Jordan–Hölder theorem" >}}, says that although a composition series is not unique, the multiset of isomorphism types of composition factors is unique up to permutation.

**Examples:**
- For $S_3$, the chain $\{e\}\lhd A_3\lhd S_3$ is a composition series; the factors are $A_3/\{e\}\cong C_3$ and $S_3/A_3\cong C_2$.
- If $G\cong \mathbb{Z}/p^n\mathbb{Z}$, then the chain $p^n\mathbb{Z}/p^n\mathbb{Z}\lhd p^{n-1}\mathbb{Z}/p^n\mathbb{Z}\lhd\cdots\lhd p\mathbb{Z}/p^n\mathbb{Z}\lhd \mathbb{Z}/p^n\mathbb{Z}$ yields a composition series with all factors cyclic of order $p$.
- If $G$ is simple and nontrivial, then $\{e\}\lhd G$ is a composition series of length $1$.
