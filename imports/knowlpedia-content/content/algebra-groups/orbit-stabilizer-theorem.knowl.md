+++
id = "algebra-groups/orbit-stabilizer-theorem"
title = "Orbit–Stabilizer Theorem"
kind = "knowl"
summary = "For a group action, an orbit is in bijection with a coset space G/Stab(x)"
aliases = ["orbit-stabilizer-theorem", "Orbit–Stabilizer Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/orbit-stabilizer-theorem.md"
+++

**Orbit–Stabilizer Theorem.**
Let $G$ be a [[algebra-groups/group|group]] acting on a set $X$ via a [[algebra-groups/group-action|group action]]. For $x \in X$, let $\operatorname{Orb}(x)$ be the [[algebra-groups/orbit|orbit]] of $x$ and let $\operatorname{Stab}(x)$ be the [[algebra-groups/stabilizer|stabilizer]] of $x$. Then the map
$$
G/\operatorname{Stab}(x) \to \operatorname{Orb}(x), \qquad g\,\operatorname{Stab}(x) \mapsto g\cdot x,
$$

is a bijection. In particular, if $G$ is finite then
$$
|\operatorname{Orb}(x)| = [G:\operatorname{Stab}(x)] \quad \text{and} \quad |G| = |\operatorname{Orb}(x)|\cdot |\operatorname{Stab}(x)|.
$$

This theorem converts problems about orbits into problems about [[algebra-groups/coset|cosets]] and [[algebra-groups/index-of-subgroup|index]]. It is the main input for the [[algebra-groups/class-equation|class equation]] and many counting arguments.
