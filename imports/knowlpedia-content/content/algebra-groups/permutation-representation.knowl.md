+++
id = "algebra-groups/permutation-representation"
title = "Permutation Representation"
kind = "knowl"
summary = "A homomorphism from a group into bijections of a set"
aliases = ["permutation-representation", "Permutation Representation"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/permutation-representation.md"
+++

A **permutation representation** of a [[algebra-groups/group|group]] $G$ on a set $X$ is a [[algebra-groups/group-homomorphism|group homomorphism]]
$$
\rho: G \to \mathrm{Sym}(X),
$$

where $\mathrm{Sym}(X)$ denotes the group of all [[shared-foundations/bijective-function|bijective]] maps $X\to X$ under composition. Giving such a homomorphism is equivalent to giving a [[algebra-groups/group-action|group action]] via $g\cdot x := \rho(g)(x)$.

The kernel of $\rho$ is exactly the [[algebra-groups/kernel-of-action|kernel of the action]]. In particular, $\rho$ is injective iff the action is [[algebra-groups/faithful-action|faithful]], and [[algebra-groups/cayleys-theorem|Cayley's theorem]] says every group has a faithful permutation representation (on itself by left multiplication).

**Examples:**
- (Left regular representation) $\rho(g)$ is the permutation $x\mapsto gx$ of the underlying set of $G$.
- (Action on cosets) For $H\le G$, the action on $G/H$ gives a homomorphism $G\to \mathrm{Sym}(G/H)$.
- (Conjugation) The conjugation action gives a homomorphism $G\to \mathrm{Sym}(G)$.
