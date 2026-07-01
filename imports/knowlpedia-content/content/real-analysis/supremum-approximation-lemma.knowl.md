+++
id = "real-analysis/supremum-approximation-lemma"
title = "Supremum Approximation Lemma"
kind = "knowl"
summary = "A supremum can be approximated from below by elements of the set."
aliases = ["supremum-approximation-lemma", "Supremum Approximation Lemma"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/supremum-approximation-lemma.md"
+++

**Supremum approximation lemma:** Let $A \subseteq \mathbb{R}$ be nonempty and [[real-analysis/bounded-above|bounded above]], and let $s=\sup A$ (see [[real-analysis/supremum|supremum]]). Then for every $\varepsilon>0$ there exists $a\in A$ such that
$s-\varepsilon < a \le s$.

Dually, if $A$ is nonempty and [[real-analysis/bounded-below|bounded below]] with $m=\inf A$, then for every $\varepsilon>0$ there exists $a\in A$ such that
$m \le a < m+\varepsilon$.

This lemma is the standard way to pass between statements involving $\sup A$ or $\inf A$ and $\varepsilon$-style inequalities used in limits and estimates.
