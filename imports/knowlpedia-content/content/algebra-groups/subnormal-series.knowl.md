+++
id = "algebra-groups/subnormal-series"
title = "Subnormal series"
kind = "knowl"
summary = "A finite chain of subgroups where each is normal in the next"
aliases = ["subnormal-series", "Subnormal series"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/subnormal-series.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. A **subnormal series** of $G$ is a finite chain of subgroups
$
\{e\}=G_0 \lhd G_1 \lhd \cdots \lhd G_n = G
$
such that each $G_{i-1}$ is a [[algebra-groups/normal-subgroup|normal subgroup]] of $G_i$.

Subnormal series are used to organize inductive arguments on group structure. Important special cases include the [[algebra-groups/derived-series|derived series]] and the [[algebra-groups/lower-central-series|lower central series]]. A subnormal series whose factors satisfy additional properties can be a [[algebra-groups/composition-series-group|composition series]].

**Examples:**
- The two-step chain $\{e\}\lhd G$ is a subnormal series for every group $G$.
- In $S_4$, the chain $\{e\}\lhd V_4\lhd A_4\lhd S_4$ is a subnormal series (here $V_4$ is the Klein four subgroup).
- In $S_3$, the chain $\{e\}<\langle (12)\rangle<S_3$ is *not* a subnormal series because $\langle(12)\rangle$ is not normal in $S_3$.
