+++
id = "algebra-groups/semidirect-product"
title = "Semidirect Product"
kind = "knowl"
summary = "A product of groups twisted by an action by automorphisms"
aliases = ["semidirect-product", "Semidirect Product"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/semidirect-product.md"
+++

Let $N$ and $H$ be [[algebra-groups/group|groups]], and let
$$
\varphi: H \to \operatorname{Aut}(N)
$$

be a [[algebra-groups/group-homomorphism|group homomorphism]], where $\operatorname{Aut}(N)$ is the [[algebra-groups/automorphism-group|automorphism group]]. The **semidirect product** of $N$ by $H$ with respect to $\varphi$, denoted $N\rtimes_{\varphi} H$, is the set $N\times H$ with multiplication
$$
(n_1,h_1)(n_2,h_2) := \bigl(n_1\,\varphi(h_1)(n_2),\; h_1h_2\bigr).
$$

(Equivalently, $\varphi$ encodes a [[algebra-groups/group-action|group action]] of $H$ on $N$ by automorphisms.)

The subgroup $N\times\{e\}$ is normal in $N\rtimes_{\varphi}H$, and $(N\rtimes_{\varphi}H)/(N\times\{e\})\cong H$. If $\varphi$ is trivial (every $h$ acts as the identity automorphism), then $N\rtimes_{\varphi}H$ reduces to the [[algebra-groups/direct-product-groups|direct product]] $N\times H$.

**Examples:**
- The dihedral group $D_{2n}$ is isomorphic to $C_n\rtimes C_2$, where the nontrivial element of $C_2$ acts on $C_n$ by inversion.
- The group of affine transformations $x\mapsto ax+b$ of a field is a semidirect product of the additive group (translations) by the multiplicative group (scalings).
- If $N$ is abelian and $\varphi$ is trivial, then $N\rtimes_{\varphi}H$ is just the usual product $N\times H$.
