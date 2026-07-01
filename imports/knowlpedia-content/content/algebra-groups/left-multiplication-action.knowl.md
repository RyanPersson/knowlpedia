+++
id = "algebra-groups/left-multiplication-action"
title = "Left multiplication action"
kind = "knowl"
summary = "A group acts on itself by left translation"
aliases = ["left-multiplication-action", "Left multiplication action"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/left-multiplication-action.md"
+++

**Proposition (Left multiplication action).**
Let $G$ be a [[algebra-groups/group|group]]. Define a map $G\times G\to G$ by
$$
g\cdot x := gx.
$$

Then this defines a [[algebra-groups/group-action|group action]] of $G$ on the underlying set of $G$.

Moreover, this action is:
- **transitive** (there is one orbit), and
- **free** (only the identity fixes any element),

hence it is a [[algebra-groups/regular-action|regular action]], often called the **left regular action**.

**Context.**
This action is the input for [[algebra-groups/cayleys-theorem|Cayley's theorem]]: it produces an injective homomorphism from $G$ into a symmetric group by viewing elements as permutations of $G$.
