---
title: "Torsion element"
description: "An element killed by a nonzero scalar in a module over an integral domain."
---

Let $R$ be an {{< knowl id="integral-domain" section="algebra-rings" text="integral domain" >}} and $M$ a (left) $R$-{{< knowl id="module" text="module" >}}. An element $m\in M$ is a **torsion element** if there exists a nonzero $r\in R$ such that $rm=0$. Equivalently, the {{< knowl id="annihilator-element" text="annihilator" >}}
$\operatorname{ann}(m)$ is a nonzero ideal of $R$.

Torsion detects “failure of cancellation” under scalar multiplication and is a central invariant in structure theorems over PIDs and Dedekind domains.

**Examples:**
- In the $\mathbb Z$-module $\mathbb Z/n\mathbb Z$, every element is torsion (killed by $n$).
- In the $\mathbb Z$-module $\mathbb Z$, the only torsion element is $0$.
- (Edge case) Over a field, every nonzero scalar is invertible, so the only torsion element in a vector space is $0$.
