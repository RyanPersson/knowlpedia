---
title: "Connectedness criteria in R"
description: "Equivalent ways to recognize when a subset of the real line is connected."
---

**Connectedness criteria in $\mathbb{R}$:** Let $E\subseteq \mathbb{R}$ with the usual topology. The following are equivalent:

1. $E$ is {{< knowl id="connected-set" text="connected" >}}.
2. $E$ is an {{< knowl id="interval" section="real-analysis" text="interval" >}}.
3. (Intermediate-point property) If $a,b\in E$ with $a<b$ and $c\in\mathbb{R}$ satisfies $a<c<b$, then $c\in E$.
4. (No gap) There do not exist real numbers $a<b$ such that $E\cap(-\infty,a)$ and $E\cap(b,\infty)$ are both nonempty while $E\cap(a,b)=\varnothing$.

These criteria are all manifestations of the same phenomenon: in $\mathbb{R}$, connectedness is completely controlled by order. They are often paired with {{< knowl id="continuous-image-of-connected-set-is-connected" text="continuity preserves connectedness" >}} to pin down real-valued images.
