+++
id = "algebra-groups/burnsides-lemma"
title = "Burnside's Lemma"
kind = "knowl"
summary = "The number of orbits equals the average number of fixed points"
aliases = ["burnsides-lemma", "Burnside's Lemma"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/burnsides-lemma.md"
+++

**Burnside's Lemma (Cauchy–Frobenius).**
Let $G$ be a finite [[algebra-groups/group|group]] acting on a finite set $X$ via a [[algebra-groups/group-action|group action]]. For $g \in G$, let
$$
\operatorname{Fix}(g)=\{x\in X : g\cdot x = x\}
$$

be the [[algebra-groups/fixed-point-set|fixed-point set]] of $g$. Then the number of [[algebra-groups/orbit|orbits]] of the action is
$$
|X/G| = \frac{1}{|G|}\sum_{g\in G} |\operatorname{Fix}(g)|.
$$

Burnside's lemma is a standard counting tool: instead of counting orbits directly, it averages easily computed fixed-point counts. It is frequently used in enumeration problems involving symmetries.
