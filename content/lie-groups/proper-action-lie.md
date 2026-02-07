---
title: "Proper action"
description: "A smooth Lie group action is proper if the action graph map is proper; this guarantees good quotient behavior."
---

Let a Lie group $G$ act smoothly on a manifold $M$ (see {{< knowl id="smooth-action-lie-group" text="smooth Lie group action" >}}). The action is **proper** if the map
\[
\alpha: G\times M \longrightarrow M\times M,\qquad (g,m)\mapsto (g\cdot m,\, m)
\]
is a proper map (preimages of compact sets are compact).

A frequently used equivalent criterion is: for every pair of compact subsets $K_1,K_2\subset M$, the transporter set
\[
\{g\in G : gK_1\cap K_2\neq \varnothing\}
\]
is compact in $G$.

Properness is a key hypothesis for turning orbit spaces into reasonable geometric objects (compare {{< knowl id="orbit-space" text="orbit space" >}}). Standard consequences include:

- each stabilizer $G_m$ (see {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}) is compact;
- each orbit is an embedded, closed submanifold of $M$ (see {{< knowl id="orbit-lie-group" text="orbits of Lie group actions" >}});
- the quotient topology on $M/G$ is Hausdorff.

If, in addition, the action is free (see {{< knowl id="free-action-lie" text="free action" >}}), then $M\to M/G$ is a smooth submersion and the quotient inherits a smooth manifold structure; in many settings this is the first step toward principal bundle geometry (compare {{< knowl id="principal-homogeneous-space" text="principal homogeneous spaces" >}}).
