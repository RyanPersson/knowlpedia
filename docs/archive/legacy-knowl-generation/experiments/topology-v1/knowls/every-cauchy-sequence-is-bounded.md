---
title: "Every Cauchy sequence is bounded"
description: "A Cauchy sequence must remain within some finite radius."
---

**Every Cauchy sequence is bounded**: In any metric space, every {{< knowl id="cauchy-sequence" text="Cauchy sequence" >}} has bounded image as a subset of the space (in the sense of {{< knowl id="bounded-set" text="bounded sets" >}}).

This basic fact is often used to control sequences before applying completeness or compactness arguments.

**Proof sketch** *(optional, include for major theorems)*:  
Take $\varepsilon=1$ in the Cauchy condition to find an index $N$ such that all terms past $N$ lie within distance $1$ of $x_N$. The finitely many initial terms $\{x_1,\dots,x_{N-1}\}$ have finite maximum distance from $x_N$, so the entire sequence fits inside one sufficiently large ball.
