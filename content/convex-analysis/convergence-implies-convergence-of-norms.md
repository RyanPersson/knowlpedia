---
title: "Convergence implies convergence of norms"
description: "If x_n→x, then ||x_n||→||x||"
---

**Proposition.**
If $(x_n)$ {{< knowl id="convergence-in-normed-spaces" text="converges in norm" >}} to $x$ in a normed space, then
$$
\|x_n\|\to \|x\|.
$$

**Context.** This expresses continuity of the norm map $x\mapsto\|x\|$.

**Proof sketch.** By the {{< knowl id="reverse-triangle-inequality" section="real-analysis" text="reverse triangle inequality" >}},
$$
\big|\|x_n\|-\|x\|\big|\le \|x_n-x\|\to 0,
$$

hence $\|x_n\|\to \|x\|$.
