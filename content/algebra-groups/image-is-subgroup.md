---
title: "Image is a subgroup"
description: "The image of a group homomorphism is a subgroup of the codomain"
---

**Proposition (Image is a subgroup).**
Let $f:G\to H$ be a {{</* knowl id="group-homomorphism" text="group homomorphism" */>}}. Let $\mathrm{im}(f)$ be its {{</* knowl id="image-group" text="image" */>}}. Then $\mathrm{im}(f)$ is a {{</* knowl id="subgroup" text="subgroup" */>}} of $H$.

**Context.**
Together with "kernel is normal," this gives the basic structural picture of any homomorphism: it factors through a quotient of $G$ onto a subgroup of $H$.

**Proof sketch.**
$e_H=f(e_G)\in \mathrm{im}(f)$. If $x=f(g_1)$ and $y=f(g_2)$ lie in the image, then
$$
xy^{-1}=f(g_1)\,f(g_2)^{-1}=f(g_1)\,f(g_2^{-1})=f(g_1g_2^{-1})\in \mathrm{im}(f).
$$
Apply the one-step subgroup test in $H$.
