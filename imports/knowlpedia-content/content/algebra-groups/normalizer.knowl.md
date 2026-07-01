+++
id = "algebra-groups/normalizer"
title = "Normalizer"
kind = "knowl"
summary = "The largest subgroup in which a given subgroup becomes normal"
aliases = ["normalizer"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/normalizer.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $H\le G$ be a [[algebra-groups/subgroup|subgroup]]. The **normalizer of $H$ in $G$** is
$
N_G(H) \;=\; \{\,g\in G : gHg^{-1}=H\,\}.
$
It is a subgroup of $G$ containing $H$.

The normalizer is the largest subgroup $K\le G$ such that $H$ is a [[algebra-groups/normal-subgroup|normal subgroup]] of $K$ (indeed, $H\trianglelefteq N_G(H)$ by definition). Normalizers are a basic tool for controlling conjugacy and appear throughout finite group theory (e.g. in Sylow theory).

**Examples:**
- If $G$ is abelian, then $N_G(H)=G$ for every subgroup $H$.
- In $S_3$, if $H=\{e,(12)\}$ then $N_{S_3}(H)=H$ (so $H$ is not normal in $S_3$).
- In $S_3$, if $H=A_3$ then $N_{S_3}(H)=S_3$ (since $A_3$ is normal in $S_3$).
