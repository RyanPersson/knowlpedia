+++
id = "lie-groups/center-of-a-lie-group"
title = "Center of a Lie group"
kind = "knowl"
summary = "Elements commuting with all group elements; a closed normal subgroup."
aliases = ["center-of-a-lie-group", "Center of a Lie group"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/center-of-a-lie-group.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]].

**Definition.** The **center** of $G$ is the subgroup
$$
Z(G)=\{z\in G : zg=gz \text{ for all } g\in G\}.
$$

**Basic properties.**
- $Z(G)$ is a normal subgroup (indeed characteristic), hence a [[lie-groups/normal-lie-subgroup|normal Lie subgroup]] whenever it is an embedded Lie subgroup.
- $Z(G)$ is closed in $G$, since it is the intersection of the closed sets $\{z:zg=gz\}$ over all $g\in G$.

**Relation to adjoint/conjugation.** The [[lie-groups/conjugation-action-of-a-lie-group|conjugation action]] is trivial on $Z(G)$. For connected $G$, the kernel of the [[lie-groups/adjoint-action-of-a-lie-group|adjoint representation]] is exactly $Z(G)$, so discreteness of $Z(G)$ is equivalent to discreteness of $\ker(\mathrm{Ad})$; see [[lie-groups/adjoint-faithful-iff-discrete-center|Ad has discrete kernel iff the center is discrete]].

**Context.** The quotient $G/Z(G)$ is called the adjoint form in semisimple settings; modding out by the center removes precisely the elements invisible to conjugation.
