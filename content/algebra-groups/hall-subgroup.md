---
title: "Hall subgroup"
description: "A subgroup whose order is coprime to its index in the ambient finite group"
---

Let $G$ be a finite {{< knowl id="group" text="group" >}}. A {{< knowl id="subgroup" text="subgroup" >}} $H\le G$ is called a **Hall subgroup** if the order of $H$ is relatively prime to its {{< knowl id="index-of-subgroup" text="index" >}} in $G$, i.e.
$
\gcd(|H|,[G:H])=1,
$
where $\gcd$ denotes the greatest common divisor.

Hall subgroups generalize {{< knowl id="sylow-subgroup" text="Sylow subgroups" >}}: if $|G|=p^n m$ with $p\nmid m$ and $P$ is a Sylow $p$-subgroup, then $[G:P]=m$ is coprime to $|P|=p^n$, so $P$ is a Hall subgroup. In finite {{< knowl id="solvable-group" text="solvable" >}} groups, Hall subgroups for prescribed sets of primes exist and enjoy conjugacy properties (Hall's theorem).

**Examples:**
- In $S_3$ (order $6$), any subgroup of order $3$ is a Hall subgroup (index $2$), and any subgroup of order $2$ is also a Hall subgroup (index $3$).
- In $A_4$ (order $12$), the Klein four subgroup $V_4$ (order $4$) is a Hall subgroup because $[A_4:V_4]=3$ and $\gcd(4,3)=1$.
- Not every finite group has a Hall subgroup of every possible "coprime index" order; for instance, $A_5$ has no subgroup of order $15$ (so it has no Hall $\{3,5\}$-subgroup).
