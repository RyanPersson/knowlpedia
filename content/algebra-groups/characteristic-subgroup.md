---
title: "Characteristic Subgroup"
description: "A subgroup fixed by every automorphism of the group"
---

Let $G$ be a {{< knowl id="group" text="group" >}} and let $H\le G$ be a {{< knowl id="subgroup" text="subgroup" >}}. The subgroup $H$ is **characteristic** in $G$ (written $H \operatorname{char} G$) if for every automorphism $\varphi:G\to G$ (i.e. a bijective {{< knowl id="group-homomorphism" text="group homomorphism" >}}), one has
$
\varphi(H)=H.
$

Equivalently, $H$ is invariant under the action of the {{< knowl id="automorphism-group" text="automorphism group" >}} $\mathrm{Aut}(G)$ on the underlying set of $G$. Every characteristic subgroup is {{< knowl id="normal-subgroup" text="normal" >}}, since conjugations are {{< knowl id="inner-automorphism" text="inner automorphisms" >}}.

**Examples:**
- The {{< knowl id="center-of-group" text="center" >}} $Z(G)$ is characteristic in $G$.
- The {{< knowl id="commutator-subgroup" text="commutator subgroup" >}} $[G,G]$ is characteristic in $G$.
- In a cyclic group of order $n$, the unique subgroup of each divisor $d\mid n$ is characteristic.
- *(Non-example)* In $(\mathbb{Z}/2\mathbb{Z})^2$, any subgroup of order $2$ is not characteristic (automorphisms permute the three such subgroups).
