---
title: "Subnormal series"
description: "A finite chain of subgroups where each is normal in the next"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. A **subnormal series** of $G$ is a finite chain of subgroups
$
\{e\}=G_0 \lhd G_1 \lhd \cdots \lhd G_n = G
$
such that each $G_{i-1}$ is a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G_i$.

Subnormal series are used to organize inductive arguments on group structure. Important special cases include the {{< knowl id="derived-series" text="derived series" >}} and the {{< knowl id="lower-central-series" text="lower central series" >}}. A subnormal series whose factors satisfy additional properties can be a {{< knowl id="composition-series-group" text="composition series" >}}.

**Examples:**
- The two-step chain $\{e\}\lhd G$ is a subnormal series for every group $G$.
- In $S_4$, the chain $\{e\}\lhd V_4\lhd A_4\lhd S_4$ is a subnormal series (here $V_4$ is the Klein four subgroup).
- In $S_3$, the chain $\{e\}<\langle (12)\rangle<S_3$ is *not* a subnormal series because $\langle(12)\rangle$ is not normal in $S_3$.
