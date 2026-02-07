---
title: "Free action"
description: "A Lie group action is free if all stabilizers are trivial."
---

Let $G$ be a {{< knowl id="lie-group" text="Lie group" section="fiber-bundles">}} acting smoothly on a manifold $M$ via a {{< knowl id="smooth-action-lie-group" text="smooth action" >}} $G\times M\to M$, $(g,p)\mapsto g\cdot p$.

**Definition (Free action).**  
The action is **free** if for every $p\in M$, the {{< knowl id="stabilizer-lie-group" text="stabilizer" >}}
\[
G_p=\{g\in G: g\cdot p=p\}
\]
is trivial, i.e. $G_p=\{e\}$.

Equivalently, for each $p\in M$, the orbit map $G\to M$, $g\mapsto g\cdot p$ is injective, so each {{< knowl id="orbit-lie-group" text="orbit" >}} is diffeomorphic to $G$ as a set. (For finer geometric conclusions, freeness is often paired with {{< knowl id="proper-action-lie" text="properness" >}}.)

**Motivation.**  
Free actions are the infinitesimal starting point for principal bundles: when an action is free and proper, the orbit space $M/G$ is a manifold and $M\to M/G$ becomes a principal $G$-bundle; in the special case when the action is also transitive, $M$ is a {{< knowl id="principal-homogeneous-space" text="principal homogeneous space" >}}.
