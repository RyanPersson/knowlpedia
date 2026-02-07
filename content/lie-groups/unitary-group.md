---
title: "Unitary group $U(n)$"
description: "The compact Lie group of complex matrices preserving the standard Hermitian inner product."
---

### Definition
The **unitary group** is
$$
U(n)=\{U\in GL(n,\mathbb C)\mid U^\ast U=I\},
$$

where $U^\ast=\overline{U}^{\,T}$. Equivalently, $U(n)$ is the group of complex-linear automorphisms of $\mathbb C^n$ preserving the standard Hermitian inner product $\langle v,w\rangle = v^\ast w$.

Since the defining equation $U^\ast U=I$ is closed, $U(n)$ is a closed subgroup of the {{< knowl id="general-linear-group" text="general linear group" >}}; thus it is a Lie subgroup by the {{< knowl id="closed-subgroup-theorem" text="closed subgroup theorem" >}}. It is also {{< knowl id="compact-lie-group" text="compact" >}}.

### Basic structure
The determinant map $\det:U(n)\to U(1)$ is a Lie group homomorphism with kernel the {{< knowl id="special-unitary-group" text="special unitary group $SU(n)$" >}}. For $n=1$, $U(1)$ is the circle group (see {{< knowl id="example-u1-circle" text="the $U(1)$ example" >}}).

### Lie algebra
The Lie algebra of $U(n)$ is the {{< knowl id="unitary-lie-algebra" text="unitary Lie algebra $\\mathfrak{u}(n)$" >}}, consisting of skew-Hermitian matrices, obtained by differentiating $U^\ast U=I$ at the identity (compare {{< knowl id="lie-algebra-of-a-lie-group" text="Lie algebras of Lie groups" >}}).

### Context
$U(n)$ is the prototype compact matrix Lie group; averaging over $U(n)$ is a standard way to construct invariant inner products and prove complete reducibility results for representations (compare {{< knowl id="weyls-theorem-complete-reducibility" text="Weyl’s theorem" >}}).
