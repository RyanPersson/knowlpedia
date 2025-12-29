---
title: "Exact Sequence of Groups"
description: "A sequence of homomorphisms where image equals kernel at each stage"
---

A sequence of {{< knowl id="group-homomorphism" text="group homomorphisms" >}}
$$
\cdots \longrightarrow G_{i-1}\xrightarrow{f_{i-1}} G_i \xrightarrow{f_i} G_{i+1} \longrightarrow \cdots
$$
is **exact at $G_i$** if
$$
\operatorname{im}(f_{i-1}) = \ker(f_i),
$$
where $\operatorname{im}(f_{i-1})$ is the {{< knowl id="image-group" text="image" >}} and $\ker(f_i)$ is the {{< knowl id="kernel-group" text="kernel" >}}. The sequence is **exact** if it is exact at every term.

A **short exact sequence** is an exact sequence of the form
$$
1 \longrightarrow N \xrightarrow{\iota} G \xrightarrow{\pi} Q \longrightarrow 1,
$$
which encodes that $\iota$ is injective, $\pi$ is surjective, and $N\cong \ker(\pi)$ is a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $G$, with $Q\cong$ the {{< knowl id="quotient-group" text="quotient group" >}} $G/N$.

Exact sequences package common situations in a "coordinate-free" way; for example, the {{< knowl id="first-isomorphism-theorem-groups" text="first isomorphism theorem" >}} can be read as saying every homomorphism fits into a natural short exact sequence.

**Examples:**
- For any homomorphism $\varphi:G\to H$, the sequence $1\to \ker(\varphi)\to G\to \operatorname{im}(\varphi)\to 1$ is short exact.
- The quotient map $G\to G/N$ fits into $1\to N\to G\to G/N\to 1$ when $N$ is normal.
- The sequence $\mathbb{Z}\xrightarrow{\times n}\mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}\to 0$ is exact (interpreting $0$ as the trivial group in additive notation).
