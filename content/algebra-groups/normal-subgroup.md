---
title: "Normal Subgroup"
description: "A subgroup invariant under conjugation"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $H\le G$ be a {{< knowl id="subgroup" text="subgroup" >}}. The subgroup $H$ is **normal** in $G$ (written $H\trianglelefteq G$) if for every $g\in G$,
$
gHg^{-1} = H.
$

Normality says that $H$ is stable under the {{< knowl id="conjugation-action" text="conjugation action" >}} of $G$ on itself. Equivalently, $H$ is normal iff every left {{< knowl id="coset" text="coset" >}} of $H$ equals the corresponding right coset, and this is exactly the hypothesis needed to form the {{< knowl id="quotient-group" text="quotient group" >}} $G/H$.

**Examples:**
- The {{< knowl id="center-of-group" text="center" >}} $Z(G)$ is normal in $G$.
- $A_n$ is normal in $S_n$ for all $n\ge 2$.
- Any subgroup of index $2$ is normal (see {{< knowl id="index-2-normal" text="subgroup of index 2 is normal" >}}).
- *(Non-example)* In $S_3$, the subgroup $\{e,(12)\}$ is not normal.
