+++
id = "algebra-groups/centralizer"
title = "Centralizer"
kind = "knowl"
summary = "The subgroup of elements commuting with a given subset"
aliases = ["centralizer"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/centralizer.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $S\subseteq G$ be a [[shared-foundations/subset|subset]]. The **centralizer of $S$ in $G$** is
$
C_G(S) \;=\; \{\,g\in G : gs=sg \text{ for all } s\in S\,\}.
$
This is a [[algebra-groups/subgroup|subgroup]] of $G$. For a single element $x\in G$, one writes $C_G(x)$ for $C_G(\{x\})$.

Centralizers organize commutation in a group and control [[algebra-groups/conjugacy-class|conjugacy classes]] (e.g. via orbit–stabilizer for the conjugation action). The center satisfies $Z(G)=C_G(G)$.

**Examples:**
- If $G$ is abelian, then $C_G(S)=G$ for every subset $S$.
- In $S_3$, $C_{S_3}((12))=\{e,(12)\}$.
- In $S_3$, $C_{S_3}((123))=\{e,(123),(132)\}$.
