---
title: "Outer Automorphism Group"
description: "Automorphisms modulo inner automorphisms"
---

For a group $G$, the **outer automorphism group** is the quotient
$$
\operatorname{Out}(G) := \operatorname{Aut}(G)\big/\operatorname{Inn}(G),
$$

where $\operatorname{Aut}(G)$ is the {{< knowl id="automorphism-group" text="automorphism group" >}} and $\operatorname{Inn}(G)$ is the subgroup of {{< knowl id="inner-automorphism" text="inner automorphisms" >}}. This is a {{< knowl id="quotient-group" text="quotient group" >}}, and it measures the "new" automorphisms not coming from conjugation.

Saying $\operatorname{Out}(G)$ is trivial means every automorphism of $G$ is inner.

**Examples:**
- If $G$ is abelian, then $\operatorname{Inn}(G)$ is trivial, so $\operatorname{Out}(G)=\operatorname{Aut}(G)$.
- If $\operatorname{Aut}(G)=\operatorname{Inn}(G)$, then $\operatorname{Out}(G)$ is the trivial group.
- For many groups, $\operatorname{Out}(G)$ is small even when $\operatorname{Aut}(G)$ is large, reflecting that "most" automorphisms are induced by conjugation.
