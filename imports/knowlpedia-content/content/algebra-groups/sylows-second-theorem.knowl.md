+++
id = "algebra-groups/sylows-second-theorem"
title = "Sylow's Second Theorem"
kind = "knowl"
summary = "All Sylow p-subgroups are conjugate, and every p-subgroup lies in one"
aliases = ["sylows-second-theorem", "Sylow's Second Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/sylows-second-theorem.md"
+++

**Sylow's Second Theorem.**
Let $G$ be a finite [[algebra-groups/group|group]], let $p$ be a prime, and let $P$ be a [[algebra-groups/sylow-subgroup|Sylow p-subgroup]] of $G$. If $Q \le G$ is any [[algebra-groups/p-group|p-group]] (equivalently, $|Q|$ is a power of $p$), then there exists $g\in G$ such that
$$
Q \subseteq gPg^{-1}.
$$

In particular, any two Sylow $p$-subgroups of $G$ are conjugate (they lie in the same orbit under the [[algebra-groups/conjugation-action|conjugation action]]).

Sylow's second theorem implies Sylow $p$-subgroups are "unique up to conjugacy," and it is the key input for the normality test [[algebra-groups/sylow-normal-criterion|n_p=1 implies the Sylow p-subgroup is normal]]. It is typically proved using [[algebra-groups/sylows-first-theorem|Sylow's first theorem]] plus an action on cosets.
