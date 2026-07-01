+++
id = "real-analysis/reverse-triangle-inequality"
title = "Reverse triangle inequality"
kind = "knowl"
summary = "The difference of norms is bounded by the norm of the difference"
aliases = ["reverse-triangle-inequality", "Reverse triangle inequality"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/reverse-triangle-inequality.md"
+++

**Reverse triangle inequality**: In a normed vector space $(V,\|\cdot\|)$, for all $u,v\in V$,
$
\bigl|\|u\|-\|v\|\bigr|\le \|u-v\|.
$
Equivalently,
$
\|u\|\le \|v\|+\|u-v\|\quad\text{and}\quad \|v\|\le \|u\|+\|u-v\|.
$

This inequality is frequently used to show [[real-analysis/continuity-on-a-set|continuity]] of the norm map and to transfer [[topology/convergent-sequence|convergence]] of vectors to convergence of their norms.

**Examples:**
- In $\mathbb{R}$, the inequality becomes $\bigl||a|-|b|\bigr|\le |a-b|$.
- If $u_n\to u$ in a normed space, then $\|u_n\|\to \|u\|$ by the reverse [[real-analysis/triangle-inequality|triangle inequality]].
