---
title: "Every bounded infinite subset of R^k has a limit point"
description: "A bounded infinite set in Euclidean space has an accumulation point"
---

**Corollary (Bolzano–Weierstrass, set form)**: Let $E\subseteq\mathbb{R}^k$ be {{< knowl id="bounded-set" section="topology" text="bounded" >}} and infinite. Then $E$ has a {{< knowl id="limit-point" section="topology" text="limit point" >}}; i.e., there exists $x\in\mathbb{R}^k$ such that every {{< knowl id="open-set" section="topology" text="open" >}} ball $B(x,\varepsilon)$ contains a point of $E$ different from $x$ (indeed, infinitely many points of $E$).

This is the set-theoretic form of {{< knowl id="bolzano-weierstrass-theorem" section="topology" text="Bolzano–Weierstrass" >}} and is a key {{< knowl id="compact-set" section="topology" text="compactness" >}} phenomenon: boundedness plus infinitude forces clustering.

**Connection to parent theorem**:
Choose a sequence of distinct points in $E$. By Bolzano–Weierstrass, it has a {{< knowl id="convergent-sequence" section="topology" text="convergent" >}} {{< knowl id="subsequence" section="real-analysis" text="subsequence" >}}. The subsequential limit is a limit point of $E$.
