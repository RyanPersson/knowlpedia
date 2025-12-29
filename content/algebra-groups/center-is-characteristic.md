---
title: "Center is characteristic"
description: "The center of a group is invariant under all automorphisms"
---

**Proposition (Center is characteristic).**
Let $G$ be a {{< knowl id="group" text="group" >}} and let $Z(G)$ denote its {{< knowl id="center-of-group" text="center" >}}. Then $Z(G)$ is a {{< knowl id="characteristic-subgroup" text="characteristic subgroup" >}} of $G$; that is, for every automorphism $\varphi\in \mathrm{Aut}(G)$ one has $\varphi(Z(G))=Z(G)$.

**Context.**
"Characteristic" is stronger than normal: every characteristic subgroup is normal, but not conversely. The center is the basic example of a subgroup defined purely by the intrinsic multiplication structure of $G$, so it must be preserved by all automorphisms.

**Proof sketch.**
Take $z\in Z(G)$. For any $g\in G$, $zg=gz$. Apply $\varphi$ to get $\varphi(z)\varphi(g)=\varphi(g)\varphi(z)$. Since $\varphi$ is surjective, every element of $G$ equals $\varphi(g)$ for some $g$, so $\varphi(z)$ commutes with every element of $G$, i.e. $\varphi(z)\in Z(G)$. Thus $\varphi(Z(G))\subseteq Z(G)$; apply the same argument to $\varphi^{-1}$ for the reverse inclusion.
