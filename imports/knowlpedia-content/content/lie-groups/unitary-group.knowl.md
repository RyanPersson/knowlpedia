+++
id = "lie-groups/unitary-group"
title = "Unitary group $U(n)$"
kind = "knowl"
summary = "The compact Lie group of complex matrices preserving the standard Hermitian inner product."
aliases = ["unitary-group", "Unitary group $U(n)$"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/unitary-group.md"
+++

### Definition
The **unitary group** is
$$
U(n)=\{U\in GL(n,\mathbb C)\mid U^\ast U=I\},
$$

where $U^\ast=\overline{U}^{\,T}$. Equivalently, $U(n)$ is the group of complex-linear automorphisms of $\mathbb C^n$ preserving the standard Hermitian inner product $\langle v,w\rangle = v^\ast w$.

Since the defining equation $U^\ast U=I$ is closed, $U(n)$ is a closed subgroup of the [[lie-groups/general-linear-group|general linear group]]; thus it is a Lie subgroup by the [[lie-groups/closed-subgroup-theorem|closed subgroup theorem]]. It is also [[lie-groups/compact-lie-group|compact]].

### Basic structure
The determinant map $\det:U(n)\to U(1)$ is a Lie group homomorphism with kernel the [[lie-groups/special-unitary-group|special unitary group $SU(n)$]]. For $n=1$, $U(1)$ is the circle group (see [[lie-groups/example-u1-circle|the $U(1)$ example]]).

### Lie algebra
The Lie algebra of $U(n)$ is the [[lie-groups/unitary-lie-algebra|unitary Lie algebra $\\mathfrak{u}(n)$]], consisting of skew-Hermitian matrices, obtained by differentiating $U^\ast U=I$ at the identity (compare [[lie-groups/lie-algebra-of-a-lie-group|Lie algebras of Lie groups]]).

### Context
$U(n)$ is the prototype compact matrix Lie group; averaging over $U(n)$ is a standard way to construct invariant inner products and prove complete reducibility results for representations (compare [[lie-groups/weyls-theorem-complete-reducibility|Weyl’s theorem]]).
