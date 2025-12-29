---
title: "Sylow normality criterion"
description: "If the Sylow p-subgroup is unique then it is normal"
---

**Proposition (If $n_p=1$ then the Sylow p-subgroup is normal).**
Let $G$ be a finite {{</* knowl id="group" text="group" */>}} and let $p$ be a prime dividing $|G|$. Let $P$ be a {{</* knowl id="sylow-subgroup" text="Sylow p-subgroup" */>}} of $G$, and let $n_p$ denote the number of Sylow $p$-subgroups of $G$.
If $n_p=1$, then $P$ is a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}} of $G$.

**Context.**
Conjugation sends Sylow $p$-subgroups to Sylow $p$-subgroups (and in fact they are all conjugate by {{</* knowl id="sylows-second-theorem" text="Sylow's second theorem" */>}}). If there is only one, it must be fixed by conjugation.

**Proof sketch.**
For any $g\in G$, the subgroup $gPg^{-1}$ is again a Sylow $p$-subgroup (it has the same order as $P$). If $n_p=1$, then necessarily $gPg^{-1}=P$ for all $g\in G$. This is exactly the definition of normality: $P\lhd G$.
