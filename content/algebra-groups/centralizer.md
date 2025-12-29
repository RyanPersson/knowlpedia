---
title: "Centralizer"
description: "The subgroup of elements commuting with a given subset"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $S\subseteq G$ be a {{< knowl id="subset" text="subset" >}}. The **centralizer of $S$ in $G$** is
$
C_G(S) \;=\; \{\,g\in G : gs=sg \text{ for all } s\in S\,\}.
$
This is a {{< knowl id="subgroup" text="subgroup" >}} of $G$. For a single element $x\in G$, one writes $C_G(x)$ for $C_G(\{x\})$.

Centralizers organize commutation in a group and control {{< knowl id="conjugacy-class" text="conjugacy classes" >}} (e.g. via orbit–stabilizer for the conjugation action). The center satisfies $Z(G)=C_G(G)$.

**Examples:**
- If $G$ is abelian, then $C_G(S)=G$ for every subset $S$.
- In $S_3$, $C_{S_3}((12))=\{e,(12)\}$.
- In $S_3$, $C_{S_3}((123))=\{e,(123),(132)\}$.
