---
title: "Lagrange's Theorem"
description: "In a finite group, the order of a subgroup divides the order of the group"
---

**Lagrange's Theorem.**
Let $G$ be a finite {{< knowl id="group" text="group" >}}, and let $H \le G$ be a {{< knowl id="subgroup" text="subgroup" >}}. Then all left {{< knowl id="coset" text="cosets" >}} of $H$ in $G$ have the same {{< knowl id="cardinality" section="shared-foundations" text="cardinality" >}} as $H$, the distinct left cosets form a {{< knowl id="partition" section="shared-foundations" text="partition" >}} of $G$, and
$$
|G| = [G:H]\cdot |H|,
$$
where $[G:H]$ is the {{< knowl id="index-of-subgroup" text="index" >}} of $H$ in $G$. In particular, $|H|$ divides $|G|$.

This is the basic divisibility theorem for finite groups and is the starting point for many counting arguments. A standard consequence is {{< knowl id="order-divides-group-order" text="the fact that the order of an element divides the order of the group" >}}.

**Proof sketch.**
Pick one representative from each left coset; multiplying by that representative gives a bijection $H \to gH$, so each coset has size $|H|$. Since cosets are disjoint and cover $G$, the total size of $G$ is (number of cosets)$\times |H|$.
