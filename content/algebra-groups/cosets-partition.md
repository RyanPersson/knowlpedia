---
title: "Cosets Partition a Group"
description: "Left (or right) cosets of a subgroup form a partition of the ambient group"
---

**Cosets Partition a Group**: Let $G$ be a {{< knowl id="group" text="group" >}} and let $H\le G$ be a {{< knowl id="subgroup" text="subgroup" >}}. Then the set of left {{< knowl id="coset" text="cosets" >}} $\{gH : g\in G\}$ forms a {{< knowl id="partition" text="partition" >}} of $G$ (and similarly for right cosets $\{Hg:g\in G\}$).

More precisely: every $g\in G$ lies in the left coset $gH$, and any two left cosets are either equal or disjoint.

**Proof sketch**: If $x\in gH\cap g'H$, then $x=gh=g'h'$ for some $h,h'\in H$, hence $g^{-1}g'=hh'^{-1}\in H$ and so $g'H=gH$. Thus distinct cosets cannot intersect.
