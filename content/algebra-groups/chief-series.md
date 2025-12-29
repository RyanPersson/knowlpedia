---
title: "Chief series"
description: "A normal series with no intermediate normal subgroups between successive terms"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. A **chief series** of $G$ is a finite chain of subgroups
$
\{e\}=N_0 \lhd N_1 \lhd \cdots \lhd N_r = G
$
such that:
1. each $N_i$ is a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G$, and
2. for each $i$, there is no normal subgroup $K\lhd G$ with $N_{i-1}<K<N_i$.

Equivalently, each factor {{< knowl id="quotient-group" text="quotient group" >}} $N_i/N_{i-1}$ is a **minimal normal subgroup** of $G/N_{i-1}$ (meaning it is nontrivial and contains no proper nontrivial normal subgroup of $G/N_{i-1}$). Chief series are related to refinement theorems such as the {{< knowl id="schreier-refinement-theorem" text="Schreier refinement theorem" >}} and connect to composition factors (though chief factors need not be {{< knowl id="simple-group" text="simple" >}}).

**Examples:**
- In $S_3$, the only nontrivial proper normal subgroup is $A_3$, so $\{e\}\lhd A_3\lhd S_3$ is a chief series.
- In $A_4$, the Klein four subgroup $V_4$ is normal and there is no nontrivial normal subgroup properly contained in $V_4$, so $\{e\}\lhd V_4\lhd A_4$ is a chief series.
- If $G$ is simple and nontrivial, then $\{e\}\lhd G$ is a chief series (there are no intermediate normal subgroups).
