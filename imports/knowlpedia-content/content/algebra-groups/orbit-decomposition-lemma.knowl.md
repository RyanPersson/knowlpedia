+++
id = "algebra-groups/orbit-decomposition-lemma"
title = "Orbit Decomposition Lemma"
kind = "knowl"
summary = "Orbits of a group action form a partition of the underlying set"
aliases = ["orbit-decomposition-lemma", "Orbit Decomposition Lemma"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/orbit-decomposition-lemma.md"
+++

**Orbit Decomposition Lemma**: Let $G$ be a [[algebra-groups/group|group]] acting on a [[shared-foundations/set|set]] $X$ via a [[algebra-groups/group-action|group action]]. Then the set of [[algebra-groups/orbit|orbits]] $\{G\cdot x : x\in X\}$ is a [[shared-foundations/partition|partition]] of $X$.

Equivalently, define a [[shared-foundations/relation|relation]] $\sim$ on $X$ by $x\sim y$ if there exists $g\in G$ with $g\cdot x=y$. Then $\sim$ is an [[shared-foundations/equivalence-relation|equivalence relation]], and its [[shared-foundations/equivalence-class|equivalence classes]] are exactly the orbits.
