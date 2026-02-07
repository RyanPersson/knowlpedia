---
title: "Inner Automorphism"
description: "An automorphism given by conjugation by an element"
---

Let $G$ be a {{< knowl id="group" text="group" >}}. For each $g\in G$, the map
$$
c_g:G\to G,\quad c_g(x)=gxg^{-1}
$$

is an automorphism, called the **inner automorphism** determined by $g$. The set of all inner automorphisms is a subgroup $\operatorname{Inn}(G)\le \operatorname{Aut}(G)$ of the {{< knowl id="automorphism-group" text="automorphism group" >}}.

The assignment $g\mapsto c_g$ is a homomorphism $G\to \operatorname{Inn}(G)$ whose kernel is the {{< knowl id="center-of-group" text="center" >}}. Hence there is a natural isomorphism
$$
\operatorname{Inn}(G)\cong G/Z(G),
$$

a quotient {{< knowl id="quotient-group" text="group" >}} measuring how far $G$ is from being abelian.

**Examples:**
- If $G$ is abelian, then $c_g=\mathrm{id}_G$ for all $g$, so $\operatorname{Inn}(G)$ is trivial.
- In $S_3$, the center is trivial, so $\operatorname{Inn}(S_3)\cong S_3$.
- Inner automorphisms are exactly the permutations of $G$ arising from the {{< knowl id="conjugation-action" text="conjugation action" >}}.
