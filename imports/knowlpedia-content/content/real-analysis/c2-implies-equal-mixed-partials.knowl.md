+++
id = "real-analysis/c2-implies-equal-mixed-partials"
title = "C^2 implies equal mixed partials"
kind = "knowl"
summary = "If f has continuous second partial derivatives, then mixed partials commute"
aliases = ["c2-implies-equal-mixed-partials", "C^2 implies equal mixed partials"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/c2-implies-equal-mixed-partials.md"
+++

Let $U\subseteq\mathbb{R}^n$ be [[topology/open-set|open]] and let $f:U\to\mathbb{R}$ be of [[real-analysis/class-ck-map|class $C^2$]].

**Corollary**: For all $a\in U$ and all indices $i\neq j$,
$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$

**Connection to parent theorem**:
Apply [[real-analysis/mixed-partial-derivative|Schwarz's theorem]] at each point $a\in U$. The $C^2$ hypothesis guarantees the [[real-analysis/partial-derivative|mixed partial derivatives]] exist in a [[topology/neighborhood|neighborhood]] and are [[real-analysis/continuity-on-a-set|continuous]], which is exactly the hypothesis of Schwarz's theorem.
