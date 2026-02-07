---
title: "Upper central series"
description: "The ascending series built from successive centers of quotients"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. The **upper central series** of $G$ is the sequence of subgroups $(Z_n(G))_{n\ge 0}$ defined by
$
Z_0(G)=\{e\},\qquad Z_1(G)=Z(G),
$
where $Z(G)$ is the {{< knowl id="center-of-group" text="center" >}} of $G$, and for $n\ge 0$ one defines $Z_{n+1}(G)$ to be the preimage of the center of the {{< knowl id="quotient-group" text="quotient group" >}} $G/Z_n(G)$ under the natural projection $G\to G/Z_n(G)$. Equivalently,
$
Z_{n+1}(G)/Z_n(G)=Z\bigl(G/Z_n(G)\bigr).
$

Each $Z_n(G)$ is a {{< knowl id="characteristic-subgroup" text="characteristic subgroup" >}} of $G$ (hence normal). A group is {{< knowl id="nilpotent-group" text="nilpotent" >}} if and only if $Z_c(G)=G$ for some $c\ge 0$; the least such $c$ is the nilpotency class.

**Examples:**
- If $G$ is abelian, then $Z_1(G)=G$, so the upper central series reaches $G$ immediately.
- For $S_3$, the center is trivial, so $Z_n(S_3)=\{e\}$ for all $n$; hence $S_3$ is not nilpotent.
- For $D_8=\langle r,s\mid r^4=s^2=e,\ srs=r^{-1}\rangle$, one has $Z_1(D_8)=\{e,r^2\}$ and $Z_2(D_8)=D_8$, so $D_8$ is nilpotent of class $2$.
