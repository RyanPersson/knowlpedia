+++
id = "real-analysis/finite-subcover-lemma"
title = "Finite subcover lemma"
kind = "knowl"
summary = "A compact set has a finite subcover for every open cover"
aliases = ["finite-subcover-lemma", "Finite subcover lemma"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/finite-subcover-lemma.md"
+++

**Finite subcover lemma**: Let $(X,d)$ be a [[topology/metric-space|metric space]] and let $K\subseteq X$ be [[topology/compact-set|compact]]. If $\{U_\alpha\}_{\alpha\in A}$ is an [[topology/open-set|open]] cover of $K$, meaning
$
K\subseteq \bigcup_{\alpha\in A} U_\alpha,
$
then there exist $\alpha_1,\dots,\alpha_N\in A$ such that
$
K\subseteq U_{\alpha_1}\cup\cdots\cup U_{\alpha_N}.
$

This is the defining operational feature of compactness and is used as a "black box" step in many arguments: convert infinitely many local pieces into finitely many.

**Examples:**
- The [[real-analysis/interval|interval]] $[0,1]$ is compact, so any open cover of $[0,1]$ contains a finite subcover.
- The open interval $(0,1)$ is not compact: the cover $\{(1/n,1):n\in\mathbb{N}\}$ has no finite subcover.
