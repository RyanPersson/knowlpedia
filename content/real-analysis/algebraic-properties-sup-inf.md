---
title: "Algebraic properties of sup and inf"
description: "Supremum and infimum behave predictably under inclusion, translation, scaling, and unions"
---

Let $E,F\subseteq\mathbb{R}$ be nonempty and {{< knowl id="bounded-set" section="topology" text="bounded" >}} above/below where needed, and let $c\in\mathbb{R}$.

**Order properties**:
- If $E\subseteq F$ and both are bounded above, then $\sup E\le \sup F$ (see {{< knowl id="supremum" text="supremum" >}}).
- If $E\subseteq F$ and both are bounded below, then $\inf E\ge \inf F$ (see {{< knowl id="infimum" text="infimum" >}}).

**Translation**:
- If $E+c=\{x+c:x\in E\}$, then
  $
  \sup(E+c)=\sup E + c,\qquad \inf(E+c)=\inf E + c.
  $

**Scaling**:
- If $\lambda\ge 0$ and $\lambda E=\{\lambda x:x\in E\}$, then
  $
  \sup(\lambda E)=\lambda\,\sup E,\qquad \inf(\lambda E)=\lambda\,\inf E.
  $
- If $\lambda<0$, then
  $
  \sup(\lambda E)=\lambda\,\inf E,\qquad \inf(\lambda E)=\lambda\,\sup E.
  $
In particular,
$
\sup(-E)=-\inf E,\qquad \inf(-E)=-\sup E.
$

**Finite unions**:
- If $E$ and $F$ are bounded above, then $E\cup F$ is bounded above and
  $
  \sup(E\cup F)=\max\{\sup E,\sup F\}.
  $
Similarly, if bounded below then
$
\inf(E\cup F)=\min\{\inf E,\inf F\}.
$
Here {{< knowl id="maximum" text="max" >}} and {{< knowl id="minimum" text="min" >}} denote the maximum and minimum of a finite set.

These rules are used constantly to manipulate bounds and to compare limiting processes.
