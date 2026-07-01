+++
id = "algebra-groups/p-group"
title = "p-group"
kind = "knowl"
summary = "A group whose elements have order a power of a fixed prime p"
aliases = ["p-group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/p-group.md"
+++

Fix a prime number $p$. A **$p$-group** is a [[algebra-groups/group|group]] $G$ such that every element $g\in G$ has order $p^k$ for some integer $k\ge 0$ (depending on $g$). If $G$ is finite, this is equivalent to saying that the [[shared-foundations/cardinality|cardinality]] of $G$ is a power of $p$, i.e. $|G|=p^n$ for some $n\ge 0$.

Finite $p$-groups have strong structure properties; for instance, they have nontrivial center (see [[algebra-groups/p-group-nontrivial-center|p-group has nontrivial center]]). Maximal $p$-subgroups of a finite group occur as [[algebra-groups/sylow-subgroup|Sylow p-subgroups]], central in Sylow theory.

**Examples:**
- The additive group $\mathbb{Z}/p^n\mathbb{Z}$ is a finite $p$-group of order $p^n$.
- The quaternion group $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$ is a $2$-group (every element has order $1$, $2$, or $4$).
- The trivial group $\{e\}$ is a $p$-group for every prime $p$ (it has order $p^0=1$).
