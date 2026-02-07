---
title: "Matrix ring"
description: "The ring of n×n matrices over a ring with the usual addition and multiplication."
---

Let $R$ be a {{< knowl id="ring" text="ring" >}} and let $n\ge 1$. The **matrix ring** $M_n(R)$ is the set of all $n\times n$ matrices with entries in $R$, with addition defined entrywise and multiplication defined by the usual row-by-column rule.

If $R$ is {{< knowl id="unital-ring" text="unital" >}}, then $M_n(R)$ is unital with identity matrix $I_n$. For many structural properties, matrix rings behave like “noncommutative polynomial extensions”: for instance, $M_n(D)$ over a division ring $D$ is {{< knowl id="simple-ring" text="simple" >}} and has {{< knowl id="center-of-ring" text="center" >}} given by scalar matrices from $Z(D)$.

**Examples:**
- $M_2(\mathbb{Z})$ is a noncommutative ring with identity $I_2$.
- For a prime $p$, $M_3(\mathbb{F}_p)$ is a finite ring of size $p^9$.
- $M_1(R)$ is canonically isomorphic to $R$.