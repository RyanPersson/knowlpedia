---
title: "Subset"
description: "A set contained in another set, element by element."
---

A **subset** of a set $B$ is a set $A$ such that every element of $A$ is an element of $B$:
$$
A\subseteq B \;\;:\!\iff\;\; \forall x\,(x\in A \Rightarrow x\in B).
$$

The subset relation is a basic way to compare {{< knowl id="set" text="sets" >}} and is used to define operations like {{< knowl id="power-set" text="power set" >}} and {{< knowl id="set-difference" text="set difference" >}}. Note that $A=B$ holds exactly when both $A\subseteq B$ and $B\subseteq A$.

**Examples:**
- $\{1,2\}\subseteq \{1,2,3\}$.
- For any set $A$, $\varnothing\subseteq A$ (see {{< knowl id="empty-set" text="empty set" >}}).
