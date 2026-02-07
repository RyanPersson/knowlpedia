---
title: "Semidirect Product"
description: "A product of groups twisted by an action by automorphisms"
---

Let $N$ and $H$ be {{< knowl id="group" text="groups" >}}, and let
$$
\varphi: H \to \operatorname{Aut}(N)
$$

be a {{< knowl id="group-homomorphism" text="group homomorphism" >}}, where $\operatorname{Aut}(N)$ is the {{< knowl id="automorphism-group" text="automorphism group" >}}. The **semidirect product** of $N$ by $H$ with respect to $\varphi$, denoted $N\rtimes_{\varphi} H$, is the set $N\times H$ with multiplication
$$
(n_1,h_1)(n_2,h_2) := \bigl(n_1\,\varphi(h_1)(n_2),\; h_1h_2\bigr).
$$

(Equivalently, $\varphi$ encodes a {{< knowl id="group-action" text="group action" >}} of $H$ on $N$ by automorphisms.)

The subgroup $N\times\{e\}$ is normal in $N\rtimes_{\varphi}H$, and $(N\rtimes_{\varphi}H)/(N\times\{e\})\cong H$. If $\varphi$ is trivial (every $h$ acts as the identity automorphism), then $N\rtimes_{\varphi}H$ reduces to the {{< knowl id="direct-product-groups" text="direct product" >}} $N\times H$.

**Examples:**
- The dihedral group $D_{2n}$ is isomorphic to $C_n\rtimes C_2$, where the nontrivial element of $C_2$ acts on $C_n$ by inversion.
- The group of affine transformations $x\mapsto ax+b$ of a field is a semidirect product of the additive group (translations) by the multiplicative group (scalings).
- If $N$ is abelian and $\varphi$ is trivial, then $N\rtimes_{\varphi}H$ is just the usual product $N\times H$.
