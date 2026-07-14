---
title: "Totally bounded set"
description: "A set that can be covered by finitely many balls of any chosen radius"
---

A subset $E$ of a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$ is **totally bounded** if for every $\varepsilon>0$ there exists a finite family of radius-$\varepsilon$ balls that covers $E$ (equivalently, $E$ admits a finite {{< knowl id="total-boundedness-epsilon-nets" text="epsilon net" >}} for every $\varepsilon$).

Total boundedness is stronger than {{< knowl id="bounded-set" text="boundedness" >}}: it controls the set at every scale, not just globally. Along with completeness, it gives a practical compactness test via {{< knowl id="compact-iff-complete-totally-bounded" text="compact iff complete and totally bounded" >}}.

**Examples:**
- In $\mathbb{R}^n$, every bounded set is totally bounded (in particular, $[0,1]$ is totally bounded).
- In an infinite-dimensional {{< knowl id="banach-space" text="Banach space" >}}, the closed unit ball is bounded but not totally bounded.
- In a discrete metric space, a set is totally bounded iff it is finite.
