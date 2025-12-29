---
title: "Group Extension"
description: "A group fitting into a short exact sequence 1→N→E→Q→1"
---

Let $N$ and $Q$ be groups. An **extension of $Q$ by $N$** is a group $E$ together with a {{< knowl id="exact-sequence-groups" text="short exact sequence of groups" >}}
$$
1 \longrightarrow N \xrightarrow{\;\iota\;} E \xrightarrow{\;\pi\;} Q \longrightarrow 1.
$$
Exactness means $\iota$ is injective, $\pi$ is surjective, and $\iota(N)=\ker(\pi)$.

In particular, $N$ identifies with a {{< knowl id="normal-subgroup" text="normal subgroup" >}} of $E$, and $Q$ is (canonically) isomorphic to the {{< knowl id="quotient-group" text="quotient group" >}} $E/N$. Extensions organize the ways a group can be built from a normal subgroup and a quotient.

**Examples:**
- For any $n\ge 1$, there is an extension $1\to n\mathbb{Z}\to \mathbb{Z}\to \mathbb{Z}/n\mathbb{Z}\to 1$.
- The dihedral group fits into $1\to C_n\to D_{2n}\to C_2\to 1$.
- Direct products give extensions too: $1\to N\to N\times Q\to Q\to 1$.
