---
title: "Associated elements"
description: "Two elements that differ by multiplication by a unit."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}}. Elements $a,b\in R$ are **associates** if there exists a {{< knowl id="unit" text="unit" >}} $u\in R^\times$ such that $a=ub$.

Being associates is an equivalence relation capturing “the same divisor up to invertible scaling.” Uniqueness statements for {{< knowl id="gcd" text="gcds" >}}, {{< knowl id="prime-element" text="prime elements" >}}, and factorizations are typically only up to associates.

**Examples:**
- In $\mathbb{Z}$, $2$ and $-2$ are associates (multiply by the unit $-1$).
- In $k[x]$ with $k$ a field, $f$ and $cf$ are associates for any nonzero scalar $c\in k$.
- In $\mathbb{Z}$, $2$ and $4$ are not associates since the only units are $\pm 1$.