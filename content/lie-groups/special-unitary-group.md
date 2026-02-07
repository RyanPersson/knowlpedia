---
title: "Special unitary group"
description: "The compact matrix Lie group SU(n) preserving a Hermitian form with determinant 1."
---

Let $\langle\cdot,\cdot\rangle$ be the standard Hermitian inner product on $\mathbb C^n$. The **special unitary group** is
\[
SU(n)=\{A\in GL(n,\mathbb C): A^*A=I,\ \det(A)=1\},
\]
a closed Lie subgroup of the {{< knowl id="unitary-group" text="unitary group" >}}, hence a Lie group (see {{< knowl id="closed-subgroup-lie-group" text="closed subgroup" >}}). The group $SU(n)$ is compact and connected, and for $n\ge 2$ it is simply connected (see {{< knowl id="simply-connected-lie-group" text="simply connected Lie group" >}}).

Its Lie algebra is the {{< knowl id="special-unitary-lie-algebra" text="special unitary Lie algebra" >}}
\[
\mathfrak{su}(n)=\{X\in M_n(\mathbb C): X^*+X=0,\ \mathrm{tr}(X)=0\},
\]
with bracket $[X,Y]=XY-YX$. Because $SU(n)$ is compact, many structural results apply cleanly, including existence of {{< knowl id="bi-invariant-metric" text="bi-invariant metrics" >}} (compare {{< knowl id="compact-lie-group-bi-invariant-metric" text="compact implies bi-invariant metric" >}}) and strong harmonic analysis statements such as the {{< knowl id="peter-weyl-theorem" text="Peter–Weyl theorem" >}} and {{< knowl id="schur-orthogonality-lie-groups" text="Schur orthogonality" >}}.

A notable low-rank case is $SU(2)$ (see {{< knowl id="example-su2" text="SU(2) example" >}}), which is isomorphic to the {{< knowl id="spin-group" text="Spin(3)" >}} double cover of $SO(3)$ (see {{< knowl id="example-so3" text="SO(3) example" >}}).
