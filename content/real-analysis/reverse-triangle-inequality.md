---
title: "Reverse triangle inequality"
description: "The difference of norms is bounded by the norm of the difference"
---

**Reverse triangle inequality**: In a normed vector space $(V,\|\cdot\|)$, for all $u,v\in V$,
$
\bigl|\|u\|-\|v\|\bigr|\le \|u-v\|.
$
Equivalently,
$
\|u\|\le \|v\|+\|u-v\|\quad\text{and}\quad \|v\|\le \|u\|+\|u-v\|.
$

This inequality is frequently used to show {{< knowl id="continuity-on-a-set" text="continuity" >}} of the norm map and to transfer {{< knowl id="convergent-sequence" section="topology" text="convergence" >}} of vectors to convergence of their norms.

**Examples:**
- In $\mathbb{R}$, the inequality becomes $\bigl||a|-|b|\bigr|\le |a-b|$.
- If $u_n\to u$ in a normed space, then $\|u_n\|\to \|u\|$ by the reverse {{< knowl id="triangle-inequality" text="triangle inequality" >}}.
