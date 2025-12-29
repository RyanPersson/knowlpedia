---
title: "Kernels are Normal Subgroups"
description: "The kernel of a group homomorphism is invariant under conjugation"
---

**Kernels are Normal Subgroups**: Let $f:G\to H$ be a {{</* knowl id="group-homomorphism" text="group homomorphism" */>}} between groups. Then the {{</* knowl id="kernel-group" text="kernel" */>}} $\ker(f)$ is a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}} of $G$.

This fact is what makes {{</* knowl id="quotient-group" text="quotient groups" */>}} naturally arise from homomorphisms, and it underlies the {{</* knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" */>}}.

**Proof sketch**: First, $\ker(f)$ is a {{</* knowl id="subgroup" text="subgroup" */>}} by a subgroup test. For normality, if $k\in\ker(f)$ and $g\in G$, then
$f(gkg^{-1})=f(g)f(k)f(g)^{-1}=f(g)e f(g)^{-1}=e$,
so $gkg^{-1}\in\ker(f)$; apply the normality criterion.
