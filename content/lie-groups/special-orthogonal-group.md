---
title: "Special orthogonal group"
description: "The determinant-1 subgroup of the orthogonal group preserving a quadratic form."
---

Let $\langle\cdot,\cdot\rangle$ be the standard inner product on $\mathbb R^n$. The **special orthogonal group** is
\[
SO(n)=\{A\in GL(n,\mathbb R): A^T A=I,\ \det(A)=1\}.
\]
It is a closed Lie subgroup of the {{< knowl id="orthogonal-group" text="orthogonal group" >}}, hence a Lie group (see {{< knowl id="closed-subgroup-lie-group" text="closed subgroup" >}}). For $n\ge 2$, $SO(n)$ is connected, and for $n\ge 3$ it is not simply connected; its universal cover is the {{< knowl id="spin-group" text="spin group" >}}.

More generally, one defines $SO(p,q)$ as the determinant-1 subgroup of the group preserving a nondegenerate bilinear form of signature $(p,q)$; these are basic noncompact matrix Lie groups (compare {{< knowl id="lorentz-group" text="Lorentz group" >}} for the $(n-1,1)$ case).

The Lie algebra of $SO(n)$ is
the {{< knowl id="orthogonal-lie-algebra" text="orthogonal Lie algebra" >}} $\mathfrak{so}(n)$, consisting of skew-symmetric matrices:
\[
\mathfrak{so}(n)=\{X\in M_n(\mathbb R): X^T+X=0\},
\]
with bracket given by commutator. The group $SO(n)$ is compact, making it a key example in {{< knowl id="compact-lie-group" text="compact Lie group" >}} theory.
