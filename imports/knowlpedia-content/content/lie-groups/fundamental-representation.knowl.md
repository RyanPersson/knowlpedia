+++
id = "lie-groups/fundamental-representation"
title = "Fundamental representation"
kind = "knowl"
summary = "An irreducible highest-weight representation whose highest weight is a fundamental weight."
aliases = ["fundamental-representation", "Fundamental representation"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/fundamental-representation.md"
+++

Let $\mathfrak g$ be a complex semisimple [[lie-groups/lie-algebra|Lie algebra]] with a fixed [[lie-groups/cartan-subalgebra|Cartan subalgebra]] $\mathfrak h$ and a choice of positive roots (see [[lie-groups/positive-root|positive roots]]). Let $\{\alpha_1,\dots,\alpha_r\}$ be the set of [[lie-groups/simple-root|simple roots]], and let $\{\omega_1,\dots,\omega_r\}\subset \mathfrak h^*$ be the corresponding **fundamental weights**, characterized by
\[
\langle \omega_i,\alpha_j^\vee\rangle=\delta_{ij},
\]
where $\alpha_j^\vee$ are the simple coroots.

**Definition (Fundamental representation).**
A **fundamental representation** of $\mathfrak g$ is a finite-dimensional irreducible [[lie-groups/highest-weight-representation|highest-weight representation]] whose [[lie-groups/highest-weight|highest weight]] is one of the fundamental weights $\omega_i$.

**Example (type $A_{n-1}$).**
For $\mathfrak{sl}_n(\mathbb C)$ (see [[lie-groups/special-linear-lie-algebra|special linear Lie algebra]]), the fundamental representations are the exterior powers of the defining representation:
\[
\Lambda^k(\mathbb C^n),\qquad 1\le k\le n-1.
\]
With the standard choice of $\mathfrak h$ as diagonal trace-zero matrices, the highest weight of $\Lambda^k(\mathbb C^n)$ is $\omega_k$ (in the usual convention where weights record the eigenvalues of $\mathfrak h$ on weight vectors; compare [[lie-groups/weight-of-a-representation|weights]] and [[lie-groups/weight-space|weight spaces]]). In particular, $\Lambda^1(\mathbb C^n)=\mathbb C^n$ has highest weight $\omega_1$, while $\Lambda^{n-1}(\mathbb C^n)\cong (\mathbb C^n)^*$ has highest weight $\omega_{n-1}$.

**Context.**
Fundamental representations correspond to the nodes of the [[lie-groups/dynkin-diagram|Dynkin diagram]] and generate the representation ring in many settings; the classification of all irreducibles proceeds via the [[lie-groups/highest-weight-theorem|highest-weight theorem]].
