---
title: "Group isomorphism"
description: "A bijective group homomorphism"
---

Let $G,H$ be groups. A **group isomorphism** is a {{< knowl id="group-homomorphism" text="group homomorphism" >}} $\varphi\colon G\to H$ that is bijective as a {{< knowl id="bijective-function" section="shared-foundations" text="bijective function" >}}.

If $\varphi$ is an isomorphism, then its {{< knowl id="inverse-function" section="shared-foundations" text="inverse function" >}} $\varphi^{-1}\colon H\to G$ is also a group homomorphism, so $\varphi$ gives a structure-preserving identification between $G$ and $H$. One writes $G\cong H$ to denote that there exists a group isomorphism between them.

**Examples:**
- The map $\mathbb{Z}\to 2\mathbb{Z}$ given by $n\mapsto 2n$ is a group isomorphism (additive groups).
- For each $n\ge 1$, any cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$.
- The map $G\to G$ given by $g\mapsto xgx^{-1}$ (for fixed $x\in G$) is an isomorphism (an inner automorphism).
