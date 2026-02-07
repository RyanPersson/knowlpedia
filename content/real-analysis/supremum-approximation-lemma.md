---
title: "Supremum Approximation Lemma"
description: "A supremum can be approximated from below by elements of the set."
---

**Supremum approximation lemma:** Let $A \subseteq \mathbb{R}$ be nonempty and {{< knowl id="bounded-above" text="bounded above" >}}, and let $s=\sup A$ (see {{< knowl id="supremum" text="supremum" >}}). Then for every $\varepsilon>0$ there exists $a\in A$ such that
$s-\varepsilon < a \le s$.

Dually, if $A$ is nonempty and {{< knowl id="bounded-below" text="bounded below" >}} with $m=\inf A$, then for every $\varepsilon>0$ there exists $a\in A$ such that
$m \le a < m+\varepsilon$.

This lemma is the standard way to pass between statements involving $\sup A$ or $\inf A$ and $\varepsilon$-style inequalities used in limits and estimates.
