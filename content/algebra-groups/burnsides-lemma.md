---
title: "Burnside's Lemma"
description: "The number of orbits equals the average number of fixed points"
---

**Burnside's Lemma (Cauchy–Frobenius).**
Let $G$ be a finite {{< knowl id="group" text="group" >}} acting on a finite set $X$ via a {{< knowl id="group-action" text="group action" >}}. For $g \in G$, let
$$
\operatorname{Fix}(g)=\{x\in X : g\cdot x = x\}
$$

be the {{< knowl id="fixed-point-set" text="fixed-point set" >}} of $g$. Then the number of {{< knowl id="orbit" text="orbits" >}} of the action is
$$
|X/G| = \frac{1}{|G|}\sum_{g\in G} |\operatorname{Fix}(g)|.
$$

Burnside's lemma is a standard counting tool: instead of counting orbits directly, it averages easily computed fixed-point counts. It is frequently used in enumeration problems involving symmetries.
