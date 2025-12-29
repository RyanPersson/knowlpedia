---
title: "Product of normal subgroups is normal"
description: "If N and M are normal in G then NM is a normal subgroup of G"
---

**Proposition (Product of normal subgroups).**
Let $G$ be a {{</* knowl id="group" text="group" */>}} and let $N,M \lhd G$ be {{</* knowl id="normal-subgroup" text="normal subgroups" */>}}. Define
$$
NM \;=\; \{nm : n\in N,\ m\in M\}\subseteq G.
$$
Then $NM$ is a normal subgroup of $G$. Moreover, $NM=MN$.

**Context.**
Products like $NM$ appear in building larger normal subgroups from smaller ones (e.g. in series and extensions). The equality $NM=MN$ is a typical "normality makes products commute setwise" phenomenon.

**Proof sketch.**
- **Subgroup:** If $n_1m_1,n_2m_2\in NM$, then
  $$
  (n_1m_1)(n_2m_2)^{-1}=n_1m_1m_2^{-1}n_2^{-1}.
  $$
  Since $M\lhd G$, conjugation by $n_2^{-1}$ preserves $M$, so $m_1m_2^{-1}n_2^{-1}=n_2^{-1}m'$ for some $m'\in M$. Hence the product lies in $NM$.
- **Normality:** For $g\in G$ and $nm\in NM$,
  $$
  g(nm)g^{-1}=(gng^{-1})(gmg^{-1})\in NM
  $$
  since $N$ and $M$ are normal.
- **Setwise commutativity:** For $n\in N,m\in M$, normality of $N$ gives $mnm^{-1}\in N$, so $nm=(mnm^{-1})m\in MN$, hence $NM\subseteq MN$; similarly $MN\subseteq NM$.
