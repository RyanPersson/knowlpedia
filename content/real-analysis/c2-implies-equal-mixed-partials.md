---
title: "C^2 implies equal mixed partials"
description: "If f has continuous second partial derivatives, then mixed partials commute"
---

Let $U\subseteq\mathbb{R}^n$ be {{< knowl id="open-set" section="topology" text="open" >}} and let $f:U\to\mathbb{R}$ be of {{< knowl id="class-ck-map" text="class $C^2$" >}}.

**Corollary**: For all $a\in U$ and all indices $i\neq j$,
$
\frac{\partial^2 f}{\partial x_i\partial x_j}(a)=\frac{\partial^2 f}{\partial x_j\partial x_i}(a).
$

**Connection to parent theorem**:
Apply {{< knowl id="mixed-partial-derivative" text="Schwarz's theorem" >}} at each point $a\in U$. The $C^2$ hypothesis guarantees the {{< knowl id="partial-derivative" text="mixed partial derivatives" >}} exist in a {{< knowl id="neighborhood" section="topology" text="neighborhood" >}} and are {{< knowl id="continuity-on-a-set" text="continuous" >}}, which is exactly the hypothesis of Schwarz's theorem.
