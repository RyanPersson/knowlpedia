---
title: "Cover"
description: "A family of sets whose union contains a given set."
---

Let $A\subseteq X$ be a {{{< knowl id="subset" section="shared-foundations" text="subset" >}}}. A **cover** of $A$ is a family of subsets $\{U_i\}_{i\in I}$ of $X$ such that
\[
A \subseteq \bigcup_{i\in I} U_i.
\]
If each $U_i$ is an {{{< knowl id="open-set" text="open set" >}}} (in a given topology on $X$), then the family is an {{{< knowl id="open-cover" section="topology-compactness" text="open cover" >}}}.

Covers are used to formulate compactness and related finiteness properties, often by asking whether a cover admits a smaller cover with additional structure (for example, a finite subcover).
