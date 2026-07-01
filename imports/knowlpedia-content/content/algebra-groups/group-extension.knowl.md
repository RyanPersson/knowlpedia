+++
id = "algebra-groups/group-extension"
title = "Group Extension"
kind = "knowl"
summary = "A group fitting into a short exact sequence 1→N→E→Q→1"
aliases = ["group-extension", "Group Extension"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/group-extension.md"
+++

Let $N$ and $Q$ be groups. An **extension of $Q$ by $N$** is a group $E$ together with a [[algebra-groups/exact-sequence-groups|short exact sequence of groups]]
$$
1 \longrightarrow N \xrightarrow{\;\iota\;} E \xrightarrow{\;\pi\;} Q \longrightarrow 1.
$$

Exactness means $\iota$ is injective, $\pi$ is surjective, and $\iota(N)=\ker(\pi)$.

In particular, $N$ identifies with a [[algebra-groups/normal-subgroup|normal subgroup]] of $E$, and $Q$ is (canonically) isomorphic to the [[algebra-groups/quotient-group|quotient group]] $E/N$. Extensions organize the ways a group can be built from a normal subgroup and a quotient.

**Examples:**
- For any $n\ge 1$, there is an extension $1\to n\mathbb{Z}\to \mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}\to 1$.
- The dihedral group fits into $1\to C_n\to D_{2n}\to C_2\to 1$.
- Direct products give extensions too: $1\to N\to N\times Q\to Q\to 1$.
