+++
id = "algebra-groups/coset"
title = "Coset"
kind = "knowl"
summary = "A left or right translate of a subgroup by a group element"
aliases = ["coset"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/coset.md"
+++

A **left coset** of a [[algebra-groups/subgroup|subgroup]] $H$ in a [[algebra-groups/group|group]] $G$ is a subset of $G$ of the form
$$
gH := \{gh : h\in H\}
$$

for some $g\in G$. A **right coset** is a subset of the form
$$
Hg := \{hg : h\in H\}.
$$

Left cosets are the [[shared-foundations/equivalence-class|equivalence classes]] of the [[shared-foundations/equivalence-relation|equivalence relation]] on $G$ defined by $g\sim g'$ iff $g^{-1}g'\in H$ (equivalently, $gH=g'H$). In particular, the set of left cosets forms a [[shared-foundations/partition|partition]] of $G$, and the number of distinct left cosets is the [[algebra-groups/index-of-subgroup|index]] $[G:H]$. If $H$ is a [[algebra-groups/normal-subgroup|normal subgroup]], then $gH=Hg$ for all $g$, and the set of cosets is the underlying set of the [[algebra-groups/quotient-group|quotient group]] $G/H$.

**Examples:**
- In the additive group $\mathbb{Z}$ with $H=3\mathbb{Z}$, the cosets are $3\mathbb{Z}$, $1+3\mathbb{Z}$, and $2+3\mathbb{Z}$.
- In $S_3$ with $H=\{e,(12)\}$, the left cosets are $H$, $(13)H=\{(13),(123)\}$, and $(23)H=\{(23),(132)\}$.
- Left and right cosets can differ when $H$ is not normal: with the same $H\le S_3$, one has $(13)H=\{(13),(123)\}$ but $H(13)=\{(13),(132)\}$.
