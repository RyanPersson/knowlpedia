---
title: "Conjugation preserves order"
description: "Conjugate elements have the same order in a group"
---

**Proposition (Conjugation preserves order).**
Let $G$ be a {{</* knowl id="group" text="group" */>}}. For $x\in G$, the **order** of $x$, denoted $\mathrm{ord}(x)$, is the least positive integer $n$ such that $x^n=e$ (if such an $n$ exists), and $\mathrm{ord}(x)=\infty$ otherwise.
If $x,y\in G$ are {{</* knowl id="conjugate-element" text="conjugate" */>}}, i.e. $y=gxg^{-1}$ for some $g\in G$, then $\mathrm{ord}(y)=\mathrm{ord}(x)$.

**Context.**
Many group-theoretic invariants are constant on conjugacy classes. Order is the first basic example and is used, for instance, in the class equation and Sylow theory.

**Proof sketch.**
For every integer $n\ge 1$ one has
$$
(gxg^{-1})^n = g x^n g^{-1}.
$$
Hence $(gxg^{-1})^n=e$ iff $x^n=e$, so the minimal such $n$ (or lack thereof) agrees for $x$ and its conjugate.
