+++
id = "topology/lebesgue-number-lemma"
title = "Lebesgue number lemma"
kind = "knowl"
summary = "Every open cover of a compact metric space has a uniform scale that fits inside the cover."
aliases = ["lebesgue-number-lemma", "Lebesgue number lemma"]
domains = ["topology"]
legacy_source_path = "topology/lebesgue-number-lemma.md"
+++

**Lebesgue number lemma:** Let $(X,d)$ be a [[topology/metric-space|metric space]] and assume $X$ is [[topology/compact-set|compact]]. For every [[topology/open-cover|open cover]] $\mathcal{U}$ of $X$, there exists a number $\delta>0$ (a Lebesgue number for $\mathcal{U}$) such that for every $x\in X$ there is some $U\in\mathcal{U}$ with
\[
B(x,\delta)\subseteq U,
\]
where $B(x,\delta)$ is the [[topology/open-ball|open ball]]. Equivalently, every subset of $X$ with [[topology/diameter|diameter]] less than $\delta$ is contained in some member of the cover.

This lemma turns qualitative compactness (existence of finite subcovers) into a quantitative uniform scale, and it is a key tool in results about [[topology/uniformly-continuous-map|uniform continuity]] and [[topology/refinement-of-open-cover|refinements of open covers]].
