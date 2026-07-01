+++
id = "algebra-groups/group"
title = "Group"
kind = "knowl"
summary = "A monoid in which every element has an inverse"
aliases = ["group"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group.md"
+++

A **group** is a [[shared-foundations/set|set]] $G$ together with a [[shared-foundations/binary-operation|binary operation]] $\cdot : G\times G\to G$ such that:

1. (**Associativity**) For all $a,b,c\in G$, $(a\cdot b)\cdot c = a\cdot(b\cdot c)$.
2. (**Identity**) There exists an element $e\in G$ such that for all $a\in G$, $e\cdot a=a$ and $a\cdot e=a$.
3. (**Inverses**) For every $a\in G$ there exists an element $a^{-1}\in G$ such that $a\cdot a^{-1}=e$ and $a^{-1}\cdot a=e$.

Equivalently, a group is a [[algebra-groups/monoid|monoid]] in which every element is invertible. Much of group theory studies [[algebra-groups/subgroup|subgroups]] and structure-preserving maps called [[algebra-groups/group-homomorphism|group homomorphisms]].

**Examples:**
- $(\mathbb{Z},+)$ is a group (identity $0$, inverse of $n$ is $-n$).
- $(\mathbb{Q}^{\times},\times)$ is a group (nonzero rationals under multiplication).
- The symmetric group $S_n$ of permutations of $\{1,\dots,n\}$ is a group under composition.
- The set of invertible $n\times n$ real matrices is a group under multiplication (often denoted $GL_n(\mathbb{R})$).
