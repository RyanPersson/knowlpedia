+++
id = "algebra-groups/stabilizer"
title = "Stabilizer"
kind = "knowl"
summary = "The subgroup of elements fixing a point under a group action"
aliases = ["stabilizer"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/stabilizer.md"
+++

Let a [[algebra-groups/group-action|group action]] of a group $G$ on a set $X$ be given. For $x\in X$, the **stabilizer** of $x$ is
$$
G_x := \{g\in G : g\cdot x = x\}.
$$

The stabilizer $G_x$ is always a [[algebra-groups/subgroup|subgroup]] of $G$. Together with the [[algebra-groups/orbit|orbit]] $G\cdot x$, it controls the action: the [[algebra-groups/orbit-stabilizer-theorem|orbit-stabilizer theorem]] gives a bijection between $G/G_x$ and $G\cdot x$, and in the finite case implies $|G\cdot x| = [G:G_x]$.

**Examples:**
- For the natural action of $S_n$ on $\{1,\dots,n\}$, the stabilizer of $1$ is the subgroup of permutations fixing $1$, which is isomorphic to $S_{n-1}$.
- For the left translation action of $G$ on itself, the stabilizer of any $x\in G$ is trivial.
- For the conjugation action of $G$ on itself, the stabilizer of an element $x$ is its [[algebra-groups/centralizer|centralizer]], $\{g\in G:gx=xg\}$.
