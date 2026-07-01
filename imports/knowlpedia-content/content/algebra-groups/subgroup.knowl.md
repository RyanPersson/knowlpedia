+++
id = "algebra-groups/subgroup"
title = "Subgroup"
kind = "knowl"
summary = "A subset of a group that is itself a group under the same operation"
aliases = ["subgroup"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/subgroup.md"
+++

Let $G$ be a [[algebra-groups/group|group]] with operation $\cdot$. A **subgroup** of $G$ is a [[shared-foundations/subset|subset]] $H\subseteq G$ such that:

1. $e\in H$ (where $e$ is the identity of $G$),
2. for all $a,b\in H$ we have $a\cdot b\in H$,
3. for all $a\in H$ we have $a^{-1}\in H$.

Equivalently, $H$ is a subgroup iff it is nonempty and closed under the one-step test $ab^{-1}\in H$; see the [[algebra-groups/subgroup-test-one-step|subgroup test]]. Subgroups are the basic inputs for [[algebra-groups/coset|cosets]] and for size constraints in finite groups via [[algebra-groups/lagranges-theorem|Lagrange's theorem]].

**Examples:**
- For $n\in\mathbb{Z}$, the set $n\mathbb{Z}=\{nk:k\in\mathbb{Z}\}$ is a subgroup of $(\mathbb{Z},+)$.
- The alternating group $A_n$ is a subgroup of $S_n$.
- The set of diagonal invertible matrices is a subgroup of the group of invertible matrices under multiplication.
