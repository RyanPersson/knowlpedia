+++
id = "algebra-groups/upper-central-series"
title = "Upper central series"
kind = "knowl"
summary = "The ascending series built from successive centers of quotients"
aliases = ["upper-central-series", "Upper central series"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/upper-central-series.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. The **upper central series** of $G$ is the sequence of subgroups $(Z_n(G))_{n\ge 0}$ defined by
$
Z_0(G)=\{e\},\qquad Z_1(G)=Z(G),
$
where $Z(G)$ is the [[algebra-groups/center-of-group|center]] of $G$, and for $n\ge 0$ one defines $Z_{n+1}(G)$ to be the preimage of the center of the [[algebra-groups/quotient-group|quotient group]] $G/Z_n(G)$ under the natural projection $G\to G/Z_n(G)$. Equivalently,
$
Z_{n+1}(G)/Z_n(G)=Z\bigl(G/Z_n(G)\bigr).
$

Each $Z_n(G)$ is a [[algebra-groups/characteristic-subgroup|characteristic subgroup]] of $G$ (hence normal). A group is [[algebra-groups/nilpotent-group|nilpotent]] if and only if $Z_c(G)=G$ for some $c\ge 0$; the least such $c$ is the nilpotency class.

**Examples:**
- If $G$ is abelian, then $Z_1(G)=G$, so the upper central series reaches $G$ immediately.
- For $S_3$, the center is trivial, so $Z_n(S_3)=\{e\}$ for all $n$; hence $S_3$ is not nilpotent.
- For $D_8=\langle r,s\mid r^4=s^2=e,\ srs=r^{-1}\rangle$, one has $Z_1(D_8)=\{e,r^2\}$ and $Z_2(D_8)=D_8$, so $D_8$ is nilpotent of class $2$.
