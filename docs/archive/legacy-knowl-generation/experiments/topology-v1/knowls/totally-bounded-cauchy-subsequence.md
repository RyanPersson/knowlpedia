---
title: "Totally bounded Cauchy subsequence"
description: "In a totally bounded metric space, every sequence has a Cauchy subsequence"
---

**Totally bounded Cauchy subsequence**: If $E$ is a {{< knowl id="totally-bounded-set" text="totally bounded set" >}} in a {{< knowl id="metric-space" text="metric space" >}} $(X,d)$, then every sequence in $E$ has a {{< knowl id="cauchy-sequence" text="Cauchy subsequence" >}}.

**Proof sketch**: Cover $E$ by finitely many balls of radius $1$. One ball contains infinitely many terms; restrict to those terms. Then cover that ball’s intersection with $E$ by finitely many balls of radius $1/2$, pick one containing infinitely many remaining terms, and iterate. Choosing one term from each stage produces a subsequence that is Cauchy because its tail eventually lies in a ball of arbitrarily small radius.

**Examples:**
- Any bounded sequence in $\mathbb{R}^n$ has a Cauchy subsequence because bounded subsets of $\mathbb{R}^n$ are totally bounded.
- In a discrete metric space, the conclusion forces an infinite sequence to repeat values, matching that total boundedness implies finiteness there.
