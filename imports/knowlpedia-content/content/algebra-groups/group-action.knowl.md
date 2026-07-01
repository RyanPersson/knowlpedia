+++
id = "algebra-groups/group-action"
title = "Group Action"
kind = "knowl"
summary = "A homomorphism from a group to permutations of a set, equivalently a compatible map G×X→X"
aliases = ["group-action", "Group Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-action.md"
+++

Let $G$ be a [[algebra-groups/group|group]] and let $X$ be a [[shared-foundations/set|set]]. A **(left) group action** of $G$ on $X$ is a [[shared-foundations/function|function]] $\alpha:G\times X\to X$ (usually written $\alpha(g,x)=g\cdot x$) such that:
1. $e\cdot x = x$ for all $x\in X$, where $e$ is the identity of $G$;
2. $(gh)\cdot x = g\cdot(h\cdot x)$ for all $g,h\in G$ and all $x\in X$.

Equivalently, an action is the same data as a [[algebra-groups/group-homomorphism|group homomorphism]] from $G$ into the group of [[shared-foundations/bijective-function|bijective]] self-maps of $X$ (permutations), i.e. a [[algebra-groups/permutation-representation|permutation representation]]. Actions organize many constructions (e.g. actions on cosets) and lead to the notions of [[algebra-groups/orbit|orbits]] and [[algebra-groups/stabilizer|stabilizers]]

**Examples:**
- (Left translation) $G$ acts on itself by $g\cdot x := gx$.
- (Action on cosets) If $H\le G$, then $G$ acts on the set of left cosets $G/H$ by $g\cdot (xH):=(gx)H$.
- (Conjugation) $G$ acts on itself by $g\cdot x := gxg^{-1}$.
