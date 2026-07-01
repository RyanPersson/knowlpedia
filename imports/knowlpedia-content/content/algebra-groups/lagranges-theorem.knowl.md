+++
id = "algebra-groups/lagranges-theorem"
title = "Lagrange's Theorem"
kind = "knowl"
summary = "In a finite group, the order of a subgroup divides the order of the group"
aliases = ["lagranges-theorem", "Lagrange's Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/lagranges-theorem.md"
+++

**Lagrange's Theorem.**
Let $G$ be a finite [[algebra-groups/group|group]], and let $H \le G$ be a [[algebra-groups/subgroup|subgroup]]. Then all left [[algebra-groups/coset|cosets]] of $H$ in $G$ have the same [[shared-foundations/cardinality|cardinality]] as $H$, the distinct left cosets form a [[shared-foundations/partition|partition]] of $G$, and
$$
|G| = [G:H]\cdot |H|,
$$

where $[G:H]$ is the [[algebra-groups/index-of-subgroup|index]] of $H$ in $G$. In particular, $|H|$ divides $|G|$.

This is the basic divisibility theorem for finite groups and is the starting point for many counting arguments. A standard consequence is [[algebra-groups/order-divides-group-order|the fact that the order of an element divides the order of the group]].
