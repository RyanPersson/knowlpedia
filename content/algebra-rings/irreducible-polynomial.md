---
title: "Irreducible polynomial"
description: "A nonconstant polynomial that cannot be factored into lower-degree nonunits."
---

Let $R$ be an {{< knowl id="integral-domain" text="integral domain" >}}. A polynomial $f\in R[x]$ is **irreducible** if $f$ is nonzero, not a {{< knowl id="unit" text="unit" >}}, has positive degree, and whenever $f=gh$ with $g,h\in R[x]$, then either $g$ or $h$ is a unit.

Over a field, irreducible polynomials generate maximal ideals in $R[x]$ and define finite field extensions. Practical tests include {{< knowl id="eisensteins-criterion" text="Eisenstein’s criterion" >}}, and {{< knowl id="primitive-polynomial" text="primitive" >}} hypotheses are often used to compare factorization in $R[x]$ and in $\mathrm{Frac}(R)[x]$.

**Examples:**
- In $\mathbb{R}[x]$, the polynomial $x^2+1$ is irreducible.
- In $\mathbb{Q}[x]$, $x^3-2$ is irreducible (Eisenstein at $2$).
- In any $R[x]$, $x^2-1=(x-1)(x+1)$ is reducible.