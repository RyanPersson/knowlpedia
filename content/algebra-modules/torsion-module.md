---
title: "Torsion module"
description: "A module in which every element is torsion (over an integral domain)."
---

Let $R$ be an {{< knowl id="integral-domain" section="algebra-rings" text="integral domain" >}} and $M$ an $R$-{{< knowl id="module" text="module" >}}. The module $M$ is a **torsion module** if every element of $M$ is a {{< knowl id="torsion-element" text="torsion element" >}}; equivalently, for each $m\in M$ there exists $0\ne r\in R$ with $rm=0$.

Torsion modules sit opposite to {{< knowl id="torsion-free-module" text="torsion-free modules" >}} and often decompose into primary pieces over suitable rings.

**Examples:**
- Any finite abelian group, viewed as a $\mathbb Z$-module, is torsion.
- For $R=k[x]$ and nonzero $f\in R$, the module $R/(f)$ is torsion as an $R$-module (every class is killed by $f$).
- (Nonexample) $\mathbb Z$ is not a torsion $\mathbb Z$-module.
