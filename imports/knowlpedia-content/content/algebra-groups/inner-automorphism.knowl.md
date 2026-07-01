+++
id = "algebra-groups/inner-automorphism"
title = "Inner Automorphism"
kind = "knowl"
summary = "An automorphism given by conjugation by an element"
aliases = ["inner-automorphism", "Inner Automorphism"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/inner-automorphism.md"
+++

Let $G$ be a [[algebra-groups/group|group]]. For each $g\in G$, the map
$$
c_g:G\to G,\quad c_g(x)=gxg^{-1}
$$

is an automorphism, called the **inner automorphism** determined by $g$. The set of all inner automorphisms is a subgroup $\operatorname{Inn}(G)\le \operatorname{Aut}(G)$ of the [[algebra-groups/automorphism-group|automorphism group]].

The assignment $g\mapsto c_g$ is a homomorphism $G\to \operatorname{Inn}(G)$ whose kernel is the [[algebra-groups/center-of-group|center]]. Hence there is a natural isomorphism
$$
\operatorname{Inn}(G)\cong G/Z(G),
$$

a quotient [[algebra-groups/quotient-group|group]] measuring how far $G$ is from being abelian.

**Examples:**
- If $G$ is abelian, then $c_g=\mathrm{id}_G$ for all $g$, so $\operatorname{Inn}(G)$ is trivial.
- In $S_3$, the center is trivial, so $\operatorname{Inn}(S_3)\cong S_3$.
- Inner automorphisms are exactly the permutations of $G$ arising from the [[algebra-groups/conjugation-action|conjugation action]].
