---
title: "Refinement of an open cover"
description: "A new open cover whose sets each lie inside a set from the original cover"
---

Let $\mathcal{U}$ and $\mathcal{V}$ be open covers of a set $A$ (so each is an {{< knowl id="open-cover" text="open cover" >}} of $A$). We say that $\mathcal{V}$ is a **refinement** of $\mathcal{U}$ if for every $V\in\mathcal{V}$ there exists some $U\in\mathcal{U}$ such that
$$
V \subseteq U,
$$
i.e. each set in the new cover is a {{< knowl id="subset" text="subset" >}} of some set in the old cover.

Refinements let you replace a cover by a “finer” one while still covering the same set. This is used, for example, in the {{< knowl id="lebesgue-number-lemma" text="Lebesgue number lemma" >}} to pass from an arbitrary cover to a cover by small metric balls.

**Examples:**
- In $\mathbb{R}$, the cover $\{(-2,0),(0,2)\}$ refines $\{(-3,3)\}$.
- If $\mathcal{U}$ is an open cover of $A$, then $\mathcal{U}$ refines itself.
