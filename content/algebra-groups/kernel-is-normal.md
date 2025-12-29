---
title: "Kernel is normal"
description: "The kernel of a group homomorphism is a normal subgroup"
---

**Proposition (Kernel is normal).**
Let $f:G\to H$ be a {{</* knowl id="group-homomorphism" text="group homomorphism" */>}}. Let $\ker(f)$ be its {{</* knowl id="kernel-group" text="kernel" */>}}. Then $\ker(f)$ is a {{</* knowl id="normal-subgroup" text="normal subgroup" */>}} of $G$.

**Context.**
Normal subgroups arise naturally as kernels; conversely, every normal subgroup is the kernel of a canonical map to a quotient group.

**Proof sketch.**
Let $k\in \ker(f)$ and $g\in G$. Then
$$
f(gkg^{-1})=f(g)f(k)f(g)^{-1}=f(g)\,e\,f(g)^{-1}=e,
$$
so $gkg^{-1}\in \ker(f)$. Hence $\ker(f)\lhd G$.
