---
title: "Quotient Lie group"
description: "If N is a closed normal Lie subgroup of G, then G/N carries a natural Lie group structure."
---

Let $G$ be a Lie group (see {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}) and let $N\trianglelefteq G$ be a **closed normal Lie subgroup** (see {{< knowl id="normal-lie-subgroup" text="normal Lie subgroup" >}} and {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}). The quotient set $G/N$ carries a natural smooth manifold structure such that:

- the quotient map $q:G\to G/N$ is a smooth submersion,
- the group operation induced from $G$ is smooth,
- and $q$ is a Lie group homomorphism (see {{< knowl id="lie-group-homomorphism" text="Lie group homomorphism" >}}).

The closedness of $N$ is essential: if $N$ is not closed, then $G/N$ may fail to be Hausdorff and need not admit a Lie group structure.

Infinitesimally, if $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak n=\mathrm{Lie}(N)$ (see {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebra of a Lie group" >}}), then $\mathfrak n$ is an ideal in $\mathfrak g$ and the induced map on Lie algebras identifies
\[
\mathrm{Lie}(G/N)\;\cong\;\mathfrak g/\mathfrak n
\]
as a {{< knowl id="quotient-lie-algebra" text="quotient Lie algebra" >}}.

This construction is the global counterpart of “modding out by an ideal,” and it is fundamental in building new Lie groups from old ones (compare {{< knowl id="covering-lie-group" text="covering Lie groups" >}} and {{< knowl id="universal-covering-group" text="universal covering groups" >}}).
