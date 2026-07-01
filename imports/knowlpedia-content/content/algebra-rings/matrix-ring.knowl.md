+++
id = "algebra-rings/matrix-ring"
title = "Matrix ring"
kind = "knowl"
summary = "The ring of n×n matrices over a ring with the usual addition and multiplication."
aliases = ["matrix-ring", "Matrix ring"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/matrix-ring.md"
+++

Let $R$ be a [[algebra-rings/ring|ring]] and let $n\ge 1$. The **matrix ring** $M_n(R)$ is the set of all $n\times n$ matrices with entries in $R$, with addition defined entrywise and multiplication defined by the usual row-by-column rule.

If $R$ is [[algebra-rings/unital-ring|unital]], then $M_n(R)$ is unital with identity matrix $I_n$. For many structural properties, matrix rings behave like “noncommutative polynomial extensions”: for instance, $M_n(D)$ over a division ring $D$ is [[algebra-rings/simple-ring|simple]] and has [[algebra-rings/center-of-ring|center]] given by scalar matrices from $Z(D)$.

**Examples:**
- $M_2(\mathbb{Z})$ is a noncommutative ring with identity $I_2$.
- For a prime $p$, $M_3(\mathbb{F}_p)$ is a finite ring of size $p^9$.
- $M_1(R)$ is canonically isomorphic to $R$.
