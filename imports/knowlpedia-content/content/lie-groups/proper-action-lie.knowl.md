+++
id = "lie-groups/proper-action-lie"
title = "Proper action"
kind = "knowl"
summary = "A smooth Lie group action is proper if the action graph map is proper; this guarantees good quotient behavior."
aliases = ["proper-action-lie", "Proper action"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/proper-action-lie.md"
+++

Let a Lie group $G$ act smoothly on a manifold $M$ (see [[lie-groups/smooth-action-lie-group|smooth Lie group action]]). The action is **proper** if the map
\[
\alpha: G\times M \longrightarrow M\times M,\qquad (g,m)\mapsto (g\cdot m,\, m)
\]
is a proper map (preimages of compact sets are compact).

A frequently used equivalent criterion is: for every pair of compact subsets $K_1,K_2\subset M$, the transporter set
\[
\{g\in G : gK_1\cap K_2\neq \varnothing\}
\]
is compact in $G$.

Properness is a key hypothesis for turning orbit spaces into reasonable geometric objects (compare [[lie-groups/orbit-space|orbit space]]). Standard consequences include:

- each stabilizer $G_m$ (see [[lie-groups/stabilizer-lie-group|stabilizer]]) is compact;
- each orbit is an embedded, closed submanifold of $M$ (see [[lie-groups/orbit-lie-group|orbits of Lie group actions]]);
- the quotient topology on $M/G$ is Hausdorff.

If, in addition, the action is free (see [[lie-groups/free-action-lie|free action]]), then $M\to M/G$ is a smooth submersion and the quotient inherits a smooth manifold structure; in many settings this is the first step toward principal bundle geometry (compare [[lie-groups/principal-homogeneous-space|principal homogeneous spaces]]).
