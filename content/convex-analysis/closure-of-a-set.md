---
title: "Closure"
description: "The smallest closed set containing a given set"
---

Let $(X,d)$ be a metric space and let $E\subset X$.

The **closure** of $E$, denoted $\overline{E}$, is defined as
$$
\overline{E}:=\bigcap\{\,F\subset X \mid F \text{ is closed and } E\subset F\,\}.
$$

Equivalently, $\overline{E}$ is the **smallest** {{< knowl id="closed-subset" text="closed set" >}} containing $E$.

A useful pointwise characterization is given by {{< knowl id="closure-characterized-by-ball-intersections" text="ball intersections" >}}, and in metric spaces there is also a sequence characterization (see {{< knowl id="closure-characterized-by-convergent-sequences" text="closure via sequences" >}}).

**Examples:**
- In $\mathbb{R}$, $\overline{(0,1)}=[0,1]$.
- If $E$ is closed, then $\overline{E}=E$.
- If $E$ is dense in $X$ (e.g., $\mathbb{Q}$ in $\mathbb{R}$), then $\overline{E}=X$.
