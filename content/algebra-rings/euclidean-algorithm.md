---
title: "Euclidean algorithm yields gcd and Bézout identity"
description: "In a Euclidean domain, the Euclidean algorithm computes a gcd and expresses it as a linear combination."
---

**Euclidean algorithm yields gcd and Bézout identity**: Let $R$ be a Euclidean domain and let $a,b\in R$ be not both zero. The Euclidean algorithm produces $d\in R$ and $x,y\in R$ such that $d=\gcd(a,b)$ and $d=ax+by$. Equivalently, $(a,b)=(d)$ as ideals.

In a {{< knowl id="euclidean-domain" text="Euclidean domain" >}}, the algorithm computes a {{< knowl id="gcd" text="gcd" >}} and simultaneously shows that the ideal {{< knowl id="ideal-generated" text="generated" >}} by $a$ and $b$ is a {{< knowl id="principal-ideal" text="principal ideal" >}}. This is the core input for {{< knowl id="euclidean-implies-pid" text="Euclidean implies PID" >}}.