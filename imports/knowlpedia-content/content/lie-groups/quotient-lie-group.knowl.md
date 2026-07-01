+++
id = "lie-groups/quotient-lie-group"
title = "Quotient Lie group"
kind = "knowl"
summary = "If N is a closed normal Lie subgroup of G, then G/N carries a natural Lie group structure."
aliases = ["quotient-lie-group", "Quotient Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/quotient-lie-group.md"
+++

Let $G$ be a Lie group (see [[fiber-bundles/lie-group|Lie group]]) and let $N\trianglelefteq G$ be a **closed normal Lie subgroup** (see [[lie-groups/normal-lie-subgroup|normal Lie subgroup]] and [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]). The quotient set $G/N$ carries a natural smooth manifold structure such that:

- the quotient map $q:G\to G/N$ is a smooth submersion,
- the group operation induced from $G$ is smooth,
- and $q$ is a Lie group homomorphism (see [[lie-groups/lie-group-homomorphism|Lie group homomorphism]]).

The closedness of $N$ is essential: if $N$ is not closed, then $G/N$ may fail to be Hausdorff and need not admit a Lie group structure.

Infinitesimally, if $\mathfrak g=\mathrm{Lie}(G)$ and $\mathfrak n=\mathrm{Lie}(N)$ (see [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of a Lie group]]), then $\mathfrak n$ is an ideal in $\mathfrak g$ and the induced map on Lie algebras identifies
\[
\mathrm{Lie}(G/N)\;\cong\;\mathfrak g/\mathfrak n
\]
as a [[lie-groups/quotient-lie-algebra|quotient Lie algebra]].

This construction is the global counterpart of “modding out by an ideal,” and it is fundamental in building new Lie groups from old ones (compare [[lie-groups/covering-lie-group|covering Lie groups]] and [[lie-groups/universal-covering-group|universal covering groups]]).
