+++
id = "algebra-groups/cayleys-theorem"
title = "Cayley's Theorem"
kind = "knowl"
summary = "Every group embeds into a permutation group via the left regular action"
aliases = ["cayleys-theorem", "Cayley's Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/cayleys-theorem.md"
+++

**Cayley's Theorem.**
Let $G$ be a [[algebra-groups/group|group]]. Let $\operatorname{Sym}(G)$ denote the group of all bijections $\sigma: G \to G$ under composition. For each $g \in G$, define the left translation map $L_g: G \to G$ by $L_g(x)=gx$. Then the map
$$
\lambda: G \to \operatorname{Sym}(G), \qquad \lambda(g)=L_g,
$$

is an injective [[algebra-groups/group-homomorphism|homomorphism]] (i.e. a [[algebra-groups/group-monomorphism|monomorphism]]). Equivalently, $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$.

Cayley's theorem says every abstract group can be realized concretely as a group of permutations. The construction comes from the [[algebra-groups/left-multiplication-action|left multiplication action]] of $G$ on itself, which is [[algebra-groups/faithful-action|faithful]] and hence yields a [[algebra-groups/permutation-representation|permutation representation]].
