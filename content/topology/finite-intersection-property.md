---
title: "Finite intersection property"
description: "A property of a family of sets where every finite subfamily has nonempty intersection."
---

A family $\mathcal F$ of subsets of a set $X$ has the **finite intersection property** if for every finite choice $F_1,\dots,F_n\in\mathcal F$ one has
\[
F_1\cap\cdots\cap F_n \neq \varnothing,
\]
where $\varnothing$ is the {{< knowl id="empty-set" section="shared-foundations" text="empty set" >}}.

In topology, the finite intersection property is especially useful for families of {{< knowl id="closed-set" text="closed sets" >}}: {{< knowl id="compact-set" text="compactness" >}} can be characterized by requiring that every family of closed sets with this property has nonempty total intersection.

**Examples:**
- In $\mathbb{R}$, the family $F_n=[n,\infty)$ has the finite intersection property (any finite intersection is nonempty), but $\bigcap_{n\ge 1}F_n=\varnothing$.
- In a set $X=\{1,2,3,4\}$, the family $\{\{1,2\},\{2,3\},\{2,4\}\}$ has the finite intersection property, since every finite intersection contains $2$.
