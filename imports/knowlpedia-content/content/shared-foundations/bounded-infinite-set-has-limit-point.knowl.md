+++
id = "shared-foundations/bounded-infinite-set-has-limit-point"
title = "Every bounded infinite subset of R^k has a limit point"
kind = "knowl"
summary = "A bounded infinite set in Euclidean space has an accumulation point"
aliases = ["bounded-infinite-set-has-limit-point", "Every bounded infinite subset of R^k has a limit point"]
domains = ["shared-foundations"]
legacy_source_path = "shared-foundations/bounded-infinite-set-has-limit-point.md"
+++

**Corollary (Bolzano–Weierstrass, set form)**: Let $E\subseteq\mathbb{R}^k$ be [[topology/bounded-set|bounded]] and infinite. Then $E$ has a [[topology/limit-point|limit point]]; i.e., there exists $x\in\mathbb{R}^k$ such that every [[topology/open-set|open]] ball $B(x,\varepsilon)$ contains a point of $E$ different from $x$ (indeed, infinitely many points of $E$).

This is the set-theoretic form of [[topology/bolzano-weierstrass-theorem|Bolzano–Weierstrass]] and is a key [[topology/compact-set|compactness]] phenomenon: boundedness plus infinitude forces clustering.

**Connection to parent theorem**:
Choose a sequence of distinct points in $E$. By Bolzano–Weierstrass, it has a [[topology/convergent-sequence|convergent]] [[real-analysis/subsequence|subsequence]]. The subsequential limit is a limit point of $E$.
