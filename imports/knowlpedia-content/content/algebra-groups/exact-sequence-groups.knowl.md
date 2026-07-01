+++
id = "algebra-groups/exact-sequence-groups"
title = "Exact Sequence of Groups"
kind = "knowl"
summary = "A sequence of homomorphisms where image equals kernel at each stage"
aliases = ["exact-sequence-groups", "Exact Sequence of Groups"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/exact-sequence-groups.md"
+++

A sequence of [[algebra-groups/group-homomorphism|group homomorphisms]]
$$
\cdots \longrightarrow G_{i-1}\xrightarrow{f_{i-1}} G_i \xrightarrow{f_i} G_{i+1} \longrightarrow \cdots
$$

is **exact at $G_i$** if
$$
\operatorname{im}(f_{i-1}) = \ker(f_i),
$$

where $\operatorname{im}(f_{i-1})$ is the [[algebra-groups/image-group|image]] and $\ker(f_i)$ is the [[algebra-groups/kernel-group|kernel]]. The sequence is **exact** if it is exact at every term.

A **short exact sequence** is an exact sequence of the form
$$
1 \longrightarrow N \xrightarrow{\iota} G \xrightarrow{\pi} Q \longrightarrow 1,
$$

which encodes that $\iota$ is injective, $\pi$ is surjective, and $N\cong \ker(\pi)$ is a [[algebra-groups/normal-subgroup|normal subgroup]] of $G$, with $Q\cong$ the [[algebra-groups/quotient-group|quotient group]] $G/N$.

Exact sequences package common situations in a "coordinate-free" way; for example, the [[algebra-groups/first-isomorphism-theorem-groups|first isomorphism theorem]] can be read as saying every homomorphism fits into a natural short exact sequence.

**Examples:**
- For any homomorphism $\varphi:G\to H$, the sequence $1\to \ker(\varphi)\to G\to \operatorname{im}(\varphi)\to 1$ is short exact.
- The quotient map $G\to G/N$ fits into $1\to N\to G\to G/N\to 1$ when $N$ is normal.
- The sequence $\mathbb{Z}\xrightarrow{\times n}\mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}\to 0$ is exact (interpreting $0$ as the trivial group in additive notation).
