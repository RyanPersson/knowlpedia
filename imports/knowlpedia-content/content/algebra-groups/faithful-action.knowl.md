+++
id = "algebra-groups/faithful-action"
title = "Faithful Action"
kind = "knowl"
summary = "An action with trivial kernel, equivalently an injective permutation representation"
aliases = ["faithful-action", "Faithful Action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/faithful-action.md"
+++

A [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ is **faithful** if its [[algebra-groups/kernel-of-action|kernel]] is the [[algebra-groups/trivial-subgroup|trivial subgroup]]. Equivalently, the associated homomorphism $G\to \mathrm{Sym}(X)$ is a [[algebra-groups/group-monomorphism|monomorphism]], i.e. injective.

Faithful actions are exactly those that realize $G$ as a subgroup of a permutation group; this viewpoint underlies [[algebra-groups/cayleys-theorem|Cayley's theorem]].

**Examples:**
- The left translation action of $G$ on itself is faithful (and in fact regular).
- The conjugation action of $G$ on itself is faithful iff $Z(G)=\{e\}$.
- If $G$ is abelian and nontrivial, the conjugation action is not faithful (every element acts trivially).
