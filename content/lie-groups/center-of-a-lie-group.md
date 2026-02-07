---
title: "Center of a Lie group"
description: "Elements commuting with all group elements; a closed normal subgroup."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}}.

**Definition.** The **center** of $G$ is the subgroup
$$
Z(G)=\{z\in G : zg=gz \text{ for all } g\in G\}.
$$

**Basic properties.**
- $Z(G)$ is a normal subgroup (indeed characteristic), hence a {{< knowl id="normal-lie-subgroup" text="normal Lie subgroup" >}} whenever it is an embedded Lie subgroup.
- $Z(G)$ is closed in $G$, since it is the intersection of the closed sets $\{z:zg=gz\}$ over all $g\in G$.

**Relation to adjoint/conjugation.** The {{< knowl id="conjugation-action-of-a-lie-group" text="conjugation action" >}} is trivial on $Z(G)$. For connected $G$, the kernel of the {{< knowl id="adjoint-action-of-a-lie-group" text="adjoint representation" >}} is exactly $Z(G)$, so discreteness of $Z(G)$ is equivalent to discreteness of $\ker(\mathrm{Ad})$; see {{< knowl id="adjoint-faithful-iff-discrete-center" text="Ad has discrete kernel iff the center is discrete" >}}.

**Context.** The quotient $G/Z(G)$ is called the adjoint form in semisimple settings; modding out by the center removes precisely the elements invisible to conjugation.
