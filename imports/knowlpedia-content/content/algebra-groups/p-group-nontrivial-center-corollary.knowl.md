+++
id = "algebra-groups/p-group-nontrivial-center-corollary"
title = "Finite p-Group Has Nontrivial Center"
kind = "knowl"
summary = "If |G|=p^n with n≥1 then p divides |Z(G)|, so Z(G) is nontrivial."
aliases = ["p-group-nontrivial-center-corollary", "Finite p-Group Has Nontrivial Center"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/p-group-nontrivial-center-corollary.md"
+++

**Finite p-Group Has Nontrivial Center**: Let $p$ be a prime and let $G$ be a finite [[algebra-groups/p-group|p-group]], i.e. $|G|=p^n$ for some integer $n\ge 1$. Then the [[algebra-groups/center-of-group|center]] $Z(G)$ is nontrivial. More precisely,
$$p\ \mid\ |Z(G)|,$$

so in particular $|Z(G)|\ge p$.

This is a direct consequence of the [[algebra-groups/class-equation|class equation]], which decomposes $|G|$ into $|Z(G)|$ plus sizes of non-central [[algebra-groups/conjugacy-class|conjugacy classes]], each of which has cardinality divisible by $p$ in a $p$-group.


**Examples:**
- If $G$ is abelian, then $Z(G)=G$, so the conclusion holds trivially (and $|Z(G)|=|G|=p^n$).
- In the dihedral group of order $8$, $D_8=\langle r,s \mid r^4=e,\ s^2=e,\ srs=r^{-1}\rangle$, the center is $Z(D_8)=\{e,r^2\}$, which has size $2$ (and $2\mid 8$).
- If $|G|=p$ then $G$ is cyclic (hence abelian), so again $Z(G)=G\neq \{e\}$.
