---
title: "Oscillation"
description: "The amount a function varies on a set or interval."
---

An **oscillation** of a bounded function $f$ on a set $A\subseteq\mathbb R$ is the number
\[
\operatorname{osc}(f;A)=\sup\{|f(x)-f(y)|:x,y\in A\}.
\]
If $A$ is an interval, this equals $\sup\{f(x):x\in A\}-\inf\{f(x):x\in A\}$.

Oscillation is used in the {{< knowl id="oscillation-criterion" text="oscillation criterion" >}} for {{< knowl id="riemann-integrable-function" text="Riemann integrability" >}}, and it also detects continuity: $x$ is a {{< knowl id="discontinuity-point" text="discontinuity point" >}} exactly when the oscillation over shrinking intervals around $x$ fails to go to $0$.

**Examples:**
- For $f(x)=x$ on $[0,1]$, one has $\operatorname{osc}(f;[0,1])=1$.
- If $f$ is the indicator function of $\mathbb Q\cap[a,b]$, then on every nontrivial subinterval $I\subseteq[a,b]$ one has $\operatorname{osc}(f;I)=1$.
