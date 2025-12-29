---
title: "Split Extension"
description: "An extension admitting a homomorphic section, equivalently a semidirect product"
---

An extension
$$
1 \to N \xrightarrow{\iota} E \xrightarrow{\pi} Q \to 1
$$
is **split** if there exists a {{< knowl id="group-homomorphism" text="group homomorphism" >}} $s:Q\to E$ (a section) such that $\pi\circ s=\mathrm{id}_Q$. Equivalently, $E$ contains a subgroup isomorphic to $Q$ that maps isomorphically onto $Q$ under $\pi$.

Split extensions are precisely those coming from {{< knowl id="semidirect-product" text="semidirect products" >}}: if the extension splits, then $E\cong N\rtimes Q$ for a suitable action of $Q$ on $N$. In particular, a direct product corresponds to the split case with trivial action.

**Examples:**
- $1\to C_n\to D_{2n}\to C_2\to 1$ is split: a reflection subgroup maps isomorphically onto $C_2$.
- $1\to N\to N\times Q\to Q\to 1$ is split via the section $q\mapsto (e,q)$.
- More generally, any internal semidirect product yields a split extension $1\to N\to G\to G/N\to 1$.
