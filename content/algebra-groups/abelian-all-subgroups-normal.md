---
title: "Abelian implies all subgroups normal"
description: "In an abelian group every subgroup is normal"
---

**Proposition (Subgroups of abelian groups are normal).**
Let $G$ be an {{</* knowl id="abelian-group" text="abelian group" */>}} and let $H\le G$ be a {{</* knowl id="subgroup" text="subgroup" */>}}. Then $H$ is a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}} of $G$.

**Context.**
Normality is a conjugation-invariance condition. In an abelian group, conjugation is trivial: $ghg^{-1}=h$ for all $g,h$.

**Proof sketch.**
Fix $g\in G$ and $h\in H$. Since $G$ is abelian, $ghg^{-1}=h\in H$. Hence $gHg^{-1}\subseteq H$ for all $g$, so $H\lhd G$.
