---
title: "Cayley's Theorem"
description: "Every group embeds into a permutation group via the left regular action"
---

**Cayley's Theorem.**
Let $G$ be a {{< knowl id="group" text="group" >}}. Let $\operatorname{Sym}(G)$ denote the group of all bijections $\sigma: G \to G$ under composition. For each $g \in G$, define the left translation map $L_g: G \to G$ by $L_g(x)=gx$. Then the map
$$
\lambda: G \to \operatorname{Sym}(G), \qquad \lambda(g)=L_g,
$$
is an injective {{< knowl id="group-homomorphism" text="homomorphism" >}} (i.e. a {{< knowl id="group-monomorphism" text="monomorphism" >}}). Equivalently, $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$.

Cayley's theorem says every abstract group can be realized concretely as a group of permutations. The construction comes from the {{< knowl id="left-multiplication-action" text="left multiplication action" >}} of $G$ on itself, which is {{< knowl id="faithful-action" text="faithful" >}} and hence yields a {{< knowl id="permutation-representation" text="permutation representation" >}}.

**Proof sketch.**
The rule $g \mapsto L_g$ respects multiplication because $L_{gh} = L_g \circ L_h$. Injectivity follows from $L_g = \mathrm{id}$ implying $g = L_g(e)=e$.
