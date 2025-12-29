---
title: "Subgroup of Index 2 is Normal"
description: "Any subgroup with exactly two cosets is invariant under conjugation"
---

**Subgroup of Index 2 is Normal**: Let $G$ be a {{</* knowl id="group" text="group" */>}} and let $H\le G$ be a {{</* knowl id="subgroup" text="subgroup" */>}}. If the {{</* knowl id="index-of-subgroup" text="index" */>}} of $H$ in $G$ is $2$, then $H$ is {{</* knowl id="normal-subgroup" text="normal" */>}} in $G$.

Equivalently: if there are exactly two left {{</* knowl id="coset" text="cosets" */>}} of $H$ in $G$, then the left cosets equal the right cosets, so $gH=Hg$ for all $g\in G$.

**Proof sketch**: There are exactly two left cosets, namely $H$ and $G\setminus H$. For any $g\in G$, the right coset $Hg$ is a coset of the same size as $H$, hence must be either $H$ or $G\setminus H$. If $g\in H$ then $Hg=H=gH$. If $g\notin H$ then both $Hg$ and $gH$ are cosets distinct from $H$, hence both equal $G\setminus H$, so $Hg=gH$. Therefore $H$ is normal.
