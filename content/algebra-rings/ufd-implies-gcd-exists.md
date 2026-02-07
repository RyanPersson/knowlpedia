---
title: "UFD implies GCDs exist"
description: "In a unique factorization domain, any two elements admit a gcd unique up to associates."
---

**UFD implies GCDs exist**: Let $R$ be a UFD and let $a,b\in R$ be not both zero. Then there exists $d\in R$ such that (i) $d\mid a$ and $d\mid b$, and (ii) if $c\mid a$ and $c\mid b$ then $c\mid d$. Any two such $d$ differ by multiplication by a unit; one writes $d=\gcd(a,b)$.

In a {{< knowl id="ufd" text="unique factorization domain" >}}, write $a$ and $b$ as products of {{< knowl id="prime-element" text="prime elements" >}} and take the product of the common primes with minimal exponents to obtain a {{< knowl id="gcd" text="greatest common divisor" >}}. Uniqueness is up to {{< knowl id="associated-elements" text="associates" >}}, and in a UFD prime elements coincide with {{< knowl id="irreducible-element" text="irreducible elements" >}}.