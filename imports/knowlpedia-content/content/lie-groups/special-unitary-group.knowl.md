+++
id = "lie-groups/special-unitary-group"
title = "Special unitary group"
kind = "knowl"
summary = "The compact matrix Lie group SU(n) preserving a Hermitian form with determinant 1."
aliases = ["special-unitary-group", "Special unitary group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/special-unitary-group.md"
+++

Let $\langle\cdot,\cdot\rangle$ be the standard Hermitian inner product on $\mathbb C^n$. The **special unitary group** is
\[
SU(n)=\{A\in GL(n,\mathbb C): A^*A=I,\ \det(A)=1\},
\]
a closed Lie subgroup of the [[lie-groups/unitary-group|unitary group]], hence a Lie group (see [[lie-groups/closed-subgroup-lie-group|closed subgroup]]). The group $SU(n)$ is compact and connected, and for $n\ge 2$ it is simply connected (see [[lie-groups/simply-connected-lie-group|simply connected Lie group]]).

Its Lie algebra is the [[lie-groups/special-unitary-lie-algebra|special unitary Lie algebra]]
\[
\mathfrak{su}(n)=\{X\in M_n(\mathbb C): X^*+X=0,\ \mathrm{tr}(X)=0\},
\]
with bracket $[X,Y]=XY-YX$. Because $SU(n)$ is compact, many structural results apply cleanly, including existence of [[lie-groups/bi-invariant-metric|bi-invariant metrics]] (compare [[lie-groups/compact-lie-group-bi-invariant-metric|compact implies bi-invariant metric]]) and strong harmonic analysis statements such as the [[lie-groups/peter-weyl-theorem|Peter–Weyl theorem]] and [[lie-groups/schur-orthogonality-lie-groups|Schur orthogonality]].

A notable low-rank case is $SU(2)$ (see [[lie-groups/example-su2|SU(2) example]]), which is isomorphic to the [[lie-groups/spin-group|Spin(3)]] double cover of $SO(3)$ (see [[lie-groups/example-so3|SO(3) example]]).
