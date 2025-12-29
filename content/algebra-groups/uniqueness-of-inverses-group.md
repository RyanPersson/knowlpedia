---
title: "Uniqueness of inverses"
description: "Each element of a group has a unique two-sided inverse"
---

**Proposition (Uniqueness of inverses).**
Let $G$ be a {{< knowl id="group" text="group" >}}. For $g\in G$, an element $x\in G$ is an **inverse** of $g$ if $xg=e$ and $gx=e$, where $e$ is the identity element of $G$.
If $x$ and $y$ are both inverses of $g$, then $x=y$.

**Context.**
This justifies writing $g^{-1}$ for *the* inverse of $g$.

**Proof sketch.**
Using associativity and the defining equations,
$$
x = xe = x(gy) = (xg)y = ey = y.
$$
(Here $e$ denotes the identity in $G$.)
